from setuptools import find_packages, setup
from typing import List
import os

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns a list of requirements from the given file.
    '''
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Requirements file not found at {file_path}")
    
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Anup',
    author_email='tganup@icloud.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
