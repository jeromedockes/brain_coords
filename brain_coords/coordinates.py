import pathlib

import numpy as np
from nilearn import image
from nilearn.input_data import NiftiMasker
from nilearn.datasets import load_mni152_brain_mask


def load_coords(coords_file=None):
    if coords_file is None:
        coords_file = pathlib.Path(__file__).parent / "data" / "dmn_coords.txt"
    coords_file = pathlib.Path(coords_file)
    if (ext := coords_file.suffix) != ".txt":
        print(f"We expect numpy text format but your file extension is {ext}")
    return np.loadtxt(str(coords_file))


def coords_to_img(coords, fwhm=9.0):
    mask = load_mni152_brain_mask()
    masker = NiftiMasker(mask).fit()
    voxels = np.asarray(
        image.coord_transform(*coords.T, np.linalg.pinv(mask.affine)),
        dtype=int,
    ).T
    peaks = np.zeros(mask.shape)
    np.add.at(peaks, tuple(voxels.T), 1.0)
    peaks_img = image.new_img_like(mask, peaks)
    img = image.smooth_img(peaks_img, fwhm=fwhm)
    img = masker.inverse_transform(masker.transform(img).squeeze())
    return img
