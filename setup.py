#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version(*file_paths):
    """Retrieves the version from phenotype_ontologies/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


def parse_requirements():
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open('requirements.txt'))
    return [line for line in lineiter if line and not line.startswith("#")]


version = get_version("phenotype_ontologies", "__init__.py")


if sys.argv[-1] == 'publish':
    try:
        import wheel
        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on git:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-phenotype-ontologies',
    version=version,
    description="""Django app to parse/load phenotype ontologies (OncoTree, HPO, MONDO, etc)""",
    long_description=readme + '\n\n' + history,
    author='Michael A. Gonzalez',
    author_email='GonzalezMA@email.chop.edu',
    url='https://github.com/chopdgd/django-phenotype-ontologies',
    packages=[
        'phenotype_ontologies',
    ],
    include_package_data=True,
    install_requires=parse_requirements(),
    license="MIT",
    zip_safe=False,
    keywords='django-phenotype-ontologies',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
