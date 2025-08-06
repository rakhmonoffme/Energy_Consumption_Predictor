from setuptools import find_packages, setup


def get_requirements(file_path):
    """
    This function reads a requirements file and returns a list of requirements.
    """
    with open(file_path, 'r') as file:
        requirements = file.readlines()
    
    # Remove any leading/trailing whitespace characters
    requirements = [req.strip() for req in requirements if req.strip()]
    
    return requirements

setup(
    name = 'Energy Consumption',
    version = '0.1.0',
    author = 'Boburjon',
    author_email='rakhmonovbb@gmail.com',
    packages=find_packages(),
    install_requirements= get_requirements('requirements.txt')
    
)