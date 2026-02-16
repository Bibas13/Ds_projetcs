from setuptools import find_packages,setup
from typing import List


def get_requirement(fiel_path:str)-> List[str]:

    #this function will return the list of requirement because of '-> List[str]'
    requirements = []

    with open(fiel_path) as file_obj :
        requirements = file_obj.readlines()
        requirements = [req.replace("/n","") for req in requirements]
    
    return requirements




setup(
    name='mlprojects',
    version='0.0.2',
    author='Bibas',
    packages= find_packages(),
    #install_requires = ['pandas','numpy'] instead of this we can read the whole requirement.txt  
    install_requires = get_requirement('requirement.txt')

)


