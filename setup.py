from setuptools import setup, find_packages

setup(
    name = 'team_3_analyse_package',
    version = '0.1',
    packages = find_packages(),
    license = 'MIT',
    description ='Analyse predict for team 3',
    long_description = open('readme.MD').read(),
    install_requires = ['numpy', 'pandas'],
    url = 'https://github.com/Mph33hz/Team_3_analyse.git'
    author = ['Mpho Mokhokane','Kgauhelo Mokgawa','Sorel Ketcha ','Warren Mnisi','Lazola Javu']
    author_email = 'Mphomokhokane@gmail.com'
)
