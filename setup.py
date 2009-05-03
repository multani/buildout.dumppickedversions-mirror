# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = "0.5"

long_description = (
    read('README.txt')
    + '\n' + 
    'Detailed Documentation\n'
    '======================\n'
    + '\n' +
    read('src', 'buildout', 'dumppickedversions', 'pickedversions.txt')
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
    read('CONTRIBUTORS.txt')
    )
entry_point = 'buildout.dumppickedversions:install'
entry_points = {"zc.buildout.extension": ["default = %s" % entry_point]}

tests_require=['zc.buildout', 'zope.testing', 'zc.recipe.egg']

setup(name='buildout.dumppickedversions',
      version=version,
      description="Dump buildout picked versions.",
      long_description=long_description,
      classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
      license='GPL',
      keywords='buildout extension dump picked versions',
      author='Mustapha Benali',
      author_email='mustapha@headnet.dk',
      url='http://svn.plone.org/svn/collective/buildout/buildout.dumppickedversions',
      packages = find_packages('src'),
      package_dir = {'':'src'},
      namespace_packages=['buildout'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'zc.buildout'
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite = 'buildout.dumppickedversions.tests.test_suite',
      entry_points=entry_points,
      )
