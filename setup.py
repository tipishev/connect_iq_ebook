from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='garmin-connect-iq-ebook',
      version='0.2',
      description='Tools for creating Garmin Connect IQ eBooks',
      url='https://fascin.us/ebook',
      author='Fascinus',
      author_email='fascinus.team@gmail.com',
      license='GPL3',
      packages=['ebook'],
      include_package_data=True,
      zip_safe=False)
