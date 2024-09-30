from setuptools import find_packages,setup 

setup(
  name='mlproject',
  version='0.0.1',
  author='Dhirendra',
  author_email='shindedhirendra780@gmail.com',
  packages=find_packages(),
  install_requires=['pandas', 'numpy','seaborn']
)