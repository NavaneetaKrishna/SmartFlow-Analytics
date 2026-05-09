from setuptools import setup, find_packages
from typing import List
HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]: 
    requirements = []
    with open(file_path) as file_obj:
        # 1. Read all lines
        lines = file_obj.readlines()
        
        # 2. Clean lines (remove newlines and extra spaces)
        requirements = [req.strip() for req in lines]

        # 3. Filter out the '-e .' trigger 
        # This creates a new list without the offending string
        requirements = [req for req in requirements if req != HYPHEN_E_DOT]
            
    return requirements
setup(
    name='SmartFlow-Analytics',
    version='1.0.0',
    author='Navaneeta Krishna',
    author_email='navaneetakrishna10d@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)