#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
setup.py
"""

from setuptools import setup
from world_time_buddy import get_version

REQUIREMENTS = [
    'pytz',
    'tabulate',
    'termcolor',
    'PyYAML',
]

setup(
    name='world_time_buddy',
    version=get_version(),
    description="Display timezones and times",
    author="Mike Christof",
    author_email='mhristof@gmail.com',
    url='https://github.com/serialdoom/world_time_buddy',
    packages=[
        'world_time_buddy',
    ],
    package_dir={'world_time_buddy':
                 'world_time_buddy'},
    entry_points={
        'console_scripts': [
            'wtb=world_time_buddy:main'
        ]
    },
    include_package_data=True,
    install_requires=REQUIREMENTS,
    zip_safe=False,
    keywords='world_time_buddy',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
)
