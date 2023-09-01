from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT ='-e .'

def get_requirments(fil_path:str) -> List[str]:
   
   'this function will return the list of requirments'
  
   requirments=[]

   with open(fil_path) as file_obj:
       requirments = file_obj.readlines()
       requirments = [ req.replace('\n',"") for req in requirments]


       if HYPEN_E_DOT in requirments:
           requirments.remove(HYPEN_E_DOT)


   return requirments

setup (
    name='mlproject',
    version='0.0.1',
    author='saurabh',
    author_email='saurabhshinde1231@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments('requirments.txt')

)
