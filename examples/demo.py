from nilearn import plotting
from brain_coords.coordinates import coords_to_img, load_dmn_coords

img = coords_to_img(load_dmn_coords())
plotting.plot_stat_map(img, display_mode="z", output_file="dmn_img.pdf")
