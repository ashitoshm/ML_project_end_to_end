from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements from the requirements.txt file,
    excluding any '-e .' entry meant for editable installs.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        # Remove '-e .' if it exists in the requirements list
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='ml_project',
    version='0.0.1',
    author='Ashitosh',
    author_email='ashitoshmalwade@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
