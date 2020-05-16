import pathlib

import numpy as np
from nilearn import image
from nilearn.input_data import NiftiMasker
from nilearn.datasets import load_mni152_brain_mask


def load_dmn_coords():
    coords_file = pathlib.Path(__file__).parent / "data" / "dmn_coords.txt"
    return np.loadtxt(str(coords_file))


def coords_to_img(coords, fwhm=9.0):
    coords = np.atleast2d(coords)
    mask = load_mni152_brain_mask()
    masker = NiftiMasker(mask).fit()
    voxels = np.asarray(
        image.coord_transform(*coords.T, np.linalg.pinv(mask.affine)),
        dtype=int,
    ).T
    peaks = np.zeros(mask.shape)
    np.add.at(peaks, tuple(voxels.T), 1.0)
    peaks_img = image.new_img_like(mask, peaks)
    if fwhm is not None and fwhm >= 0:
        img = image.smooth_img(peaks_img, fwhm=fwhm)
    else:
        print("not smoothing image")
    img = masker.inverse_transform(masker.transform(img).squeeze())
    return img
