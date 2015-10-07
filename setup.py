from setuptools import setup, find_packages
import sys, os

version = '1.2.1-SNAPSHOT'

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
    namespace_packages=['ckanext',
                        'ckanext.odn_theme',
                        'ckanext.odn_theme_ic',
                        'ckanext.odn_theme_pc',
                        'ckanext.extras'],
    package_data={'': [
            'i18n/*/LC_MESSAGES/*.po',
            'i18n/*/base/images/*.jpg',
            'i18n/*/base/images/*.png',
            'i18n/*/base/images/*.ico',
            'i18n/*/base/images/*.gif',
            'public/base/images/*.css',
            'public/base/images/*.html',
            'public/base/images/*.png',
            'public/base/images/*.jpg',
            'public/base/images/*.ico',
            'public/base/images/*.gif',
            'public/css/*.css',
            'templates/*.html',
            'templates/admin/*.html',
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
    message_extractors={
        'ckanext': [
            ('**.py', 'python', None),
            ('**.html', 'ckan', None),
        ]
    }, # for babel.extract_messages, says which are source files for translating
    entry_points='''
    [ckan.plugins]
    odn_theme=ckanext.odn_theme.plugin:OdnThemePlugin
    odn_theme_ic=ckanext.odn_theme_ic.plugin:OdnThemeICPlugin
    odn_theme_pc=ckanext.odn_theme_pc.plugin:OdnThemePCPlugin
    odn_package_extras=ckanext.extras.plugin:PackageExtrasPlugin
    ''',
)
