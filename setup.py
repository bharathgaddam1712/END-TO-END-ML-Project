### SETUP.py --> Is used to make our project into package and deploy it at PYPI(Python packaging Index)

## We have to build and distribute package


from setuptools import find_packages,setup
from typing import List





Hypen_dot_e ="-e ."
def get_requirements(file_path : str) -> list[str]:

    ## THIS function return a list(str)

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if Hypen_dot_e in requirements:
            requirements.remove(Hypen_dot_e)

    return requirements




setup( 
    name='END-TO-END Project', 
    version='0.0.1', 
    author='Bharath Gaddam', 
    author_email='bharathgaddam06@gmail.com', 
    packages= find_packages(), ### Once this run it checks for the file __int__.py which is in src and then builds the package
    install_requires= get_requirements('requirements.txt') 
) 


    
