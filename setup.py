#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
    'pytest',
]

setup(
    name='Hermes',
    version='0.1.0',
    description="The Hermes project uses a zigbee network, hence it works with zigbee protocol, and this requires interacting with low-level hardware.",
    long_description=readme + '\n\n' + history,
    author="Pedro Renan",
    author_email='pedro.renan@gmail.com',
    url='https://github.com/somosprte/Hermes',
    packages=[
        'hermes',
    ],
    package_dir={'hermes':
                 'hermes'},
    entry_points={
        'console_scripts': [
            'hermes=hermes.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='Hermes',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    setup_requires=['pytest-runner'],
    test_suite='tests',
    tests_require=test_requirements
)
