from setuptools import setup, find_packages
import sys, os
from babel.messages import frontend as babel

version = '0.1.1-SNAPSHOT'

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
    namespace_packages=['ckanext', 'ckanext.odn_theme', 'ckanext.extras'],
    package_data={'': [
            'i18n/*/LC_MESSAGES/*.po',
            'public/base/images/*.css',
            'public/base/images/*.html',
            'public/base/images/*.png',
            'public/base/images/*.jpg',
            'public/base/images/*.ico',
            'public/base/images/*.gif',
            'public/css/*.css',
            'templates/*.html',
            'templates/home/*.html',
            'templates/home/snippets/*.html',
            'templates/snippets/*.html',
            'templates/package/snippets/*.html'
    ]},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    cmdclass = {'compile_catalog': babel.compile_catalog,
                'extract_messages': babel.extract_messages,
                'init_catalog': babel.init_catalog,
                'update_catalog': babel.update_catalog}, # babel
    message_extractors={
        'ckanext': [
            ('**.py', 'python', None),
            ('**.html', 'ckan', None),
        ]
    }, # for babel.extract_messages, says which are source files for translating
    entry_points='''
    [ckan.plugins]
    odn_theme=ckanext.odn_theme.plugin:OdnThemePlugin
    odn_package_extras=ckanext.extras.plugin:PackageExtrasPlugin
    ''',
)
