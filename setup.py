#!/usr/bin/env python
from setuptools import setup

setup(name='django-oscar-approval',
      version='0.1',
      url='https://github.com/tangentlabs/django-oscar-approval',
      author="Tangentlabs",
      author_email="",
      description="Order approval module for django-oscar",
      keywords="order approval, order authorisation",
      license='BSD',
      packages=['oscar_approval'],
      include_package_data=True,
      classifiers=['Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: Unix',
                   'Programming Language :: Python'],
      install_requires=['django-oscar>=0.6,<0.7'],
      )
