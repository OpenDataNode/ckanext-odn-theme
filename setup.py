from setuptools import setup, find_packages
import sys, os

version = '0.1.0-SNAPSHOT'

setup(
    name='ckanext-odn-theme',
    version=version,
    description="Open Data Node CKAN Theme",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='',
    author_email='',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.odn_theme'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
    [ckan.plugins]
        odn_theme=ckanext.odn_theme.plugin:OdnThemePlugin
    ''',
)
