#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = [ ]

setup(
    author="Matthew Langley",
    author_email='matthew.langley@tufts.edu',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Venmo escrow service used in backend for poker application.",
    entry_points={
        'console_scripts': [
            'venmo_escrow=venmo_escrow.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='venmo_escrow',
    name='venmo_escrow',
    packages=find_packages(include=['venmo_escrow', 'venmo_escrow.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/mattlangl/venmo_escrow',
    version='0.1.0',
    zip_safe=False,
)
