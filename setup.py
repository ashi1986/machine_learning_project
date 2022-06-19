from setuptools import find_packages, setup
from typing import List,Dict,OrderedDict


PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Ashish"
DESCRIPTION="This is first FSDS Machine learning project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    this function return the list which contains name of libraries mentioned in requiremnts.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),#[in this case housing which is a package]
    install_requirements=get_requirements_list()
)