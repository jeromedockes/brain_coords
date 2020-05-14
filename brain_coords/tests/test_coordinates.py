import hashlib
import numpy as np
from nilearn import image

from brain_coords import coordinates


def test_load_dmn_coords():
    coords = coordinates.load_dmn_coords()
    assert coords.shape == (4, 3)
    assert np.allclose(coords[0], [0, -52, 18])


def test_coords_to_img():
    coords = coordinates.load_dmn_coords()
    img = coordinates.coords_to_img(coords)
    data = image.get_data(img)
    assert np.allclose(np.sum(data), 3.9, atol=.1)
