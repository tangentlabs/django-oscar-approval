#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='django-oscar-approval',
    version='0.1',
    url='https://github.com/tangentlabs/django-oscar-approval',
    author="Tangentlabs",
    author_email="tangentlabs@tangentlabs.co.uk",
    description="Order approval module for django-oscar",
    license='BSD',
    keywords="order approval, order authorisation",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python',
    ],
    install_requires=[
        'django-oscar>=0.4,<0.6',
    ])
