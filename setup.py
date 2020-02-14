from setuptools import setup, find_packages

setup(
    name='Analyze Function',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA Analyse Predict',
    long_description=open('README.md').read(),
    install_requires=['numpy','pandas'],
    url = 'https://github.com/KeletsoM/Predict-Team-7',
    author='Team 7',
    author_email='u14062552@tuks.co.za'
)