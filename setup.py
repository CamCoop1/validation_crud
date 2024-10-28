#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()


setup(
    name='validation_app',
    version='0.1.0',
    description="Validation app",
    long_description=readme,
    author="Cameron Harris",
    author_email='cam.cooper.harris@gmail.com',
    url='https://github.com/CamCoop1/validation_app',
    packages=['./'],
    entry_points={
        'console_scripts': [
            'validation_app=validation_app.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='validation_app',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
