import pathlib
from setuptools import setup, find_packages


root_path = pathlib.Path(__file__).parent
requirements_path = root_path / "requirements.txt"
install_requires = []
if requirements_path.is_file():
    with open(requirements_path) as f:
        install_requires = f.read().splitlines()
setup(
    name="tnyml",
    version="0.0.1",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=install_requires,
)
