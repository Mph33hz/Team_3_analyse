from setuptools import setup, find_packages

setup(
    name = 'team_3_analyse_package',
    version = '0.1',
    packages = find_packages(),
    license = 'MIT',
    description ='Analyse predict for team 3',
    long_description = open('readme.MD').read(),
    install_requires = ['numpy', 'pandas'],
    author = 'team_3'
)