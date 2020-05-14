from setuptools import setup, find_packages

setup(
    name="brain_coords",
    description="transformation from coordinates to brain images",
    packages=find_packages(),
    package_data={"brain_coords": ["data/*"]},
    install_requires=["nilearn",],
    python_requires=">=3",
)
