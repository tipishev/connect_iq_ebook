#!/usr/bin/env python

from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    author='Fascinus',
    author_email='fascinus.team@gmail.com',
    description='Tools for creating Garmin Connect IQ eBooks',
    include_package_data=True,
    license='GPL3',
    long_description=readme(),
    name='connect-iq-ebook',
    packages=['connect_iq_ebook'],
    scripts=['bin/make-connect-iq-ebook'],
    test_suite='nose.collector',
    tests_require=['nose'],
    url='https://fascin.us/ebook',
    version='0.2',
    zip_safe=False,
)
