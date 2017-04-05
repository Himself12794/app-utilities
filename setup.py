"""
Holds the configuration information for this software
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='cda-utilities',
      version='0.0.1',
      author='Philip Whiting',
      author_email='phwhitin@cisco.com',
      packages=['cda_util'],
      install_requires=['pymongo', 'requests']
     )
