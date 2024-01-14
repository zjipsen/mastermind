# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='mastermind',
    version='0.1.0',
    description='Play the game mastermind with command line visualization',
    long_description=readme,
    author='Zana Jipsen',
    author_email='zjipsen@gmail.com',
    url='https://github.com/zjipsen/mastermind',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
