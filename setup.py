from setuptools import find_packages,setup 

def get_req(file):
    req = []
    hpdot='-e .'
    with open(file, 'r', encoding='utf-16') as f:
        lines = f.readlines()
        
        for line in lines:
            stripped_line = line.strip() 
            req.append(stripped_line) 
    if hpdot in req:
      req.remove(hpdot)
    print(req)
    return req 


setup(
  name='mlproject',
  version='0.0.1',
  author='Dhirendra',
  author_email='shindedhirendra780@gmail.com',
  packages=find_packages(),
  install_requires=get_req('requirements.txt')
)
get_req('requirements.txt')