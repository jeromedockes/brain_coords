import numpy as np
from nilearn import image

from brain_coords import coordinates


def test_load_coords(tmp_path):
    coords = coordinates.load_coords()
    assert coords.shape == (4, 3)
    assert np.allclose(coords[0], [0, -52, 18])
    new_file = tmp_path / "coords"
    np.savetxt(str(new_file), coords)
    new_coords = coordinates.load_coords(str(new_file))
    assert np.allclose(coords, new_coords)


def test_coords_to_img():
    coords = coordinates.load_coords()
    img = coordinates.coords_to_img(coords)
    data = image.get_data(img)
    assert np.allclose(np.sum(data), 3.9, atol=.1)
