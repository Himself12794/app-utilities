"""
Holds the configuration information for this software
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='app-utilities',
      version='0.1.4',
      author='Philip Whiting',
      author_email='phwhitin@cisco.com',
      packages=['app_util'],
      install_requires=['pymongo', 'requests']
      )
