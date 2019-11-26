''' Setup script to gather metrics for various CCI services
'''

# Bootstrap setuptools if necessary
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(name='cci-metrics',
      version='0.1',
      packages=find_packages()
)
