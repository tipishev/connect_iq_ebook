from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='connect-iq-ebook',
      version='0.1',
      description='Tools for creating Connect IQ eBooks',
      url='https://fascin.us/ebook',
      author='Fascinus',
      author_email='fascinus.team@gmail.com',
      license='GPL3',
      packages=['connect_iq_ebook'],
      include_package_data=True,
      zip_safe=False)
