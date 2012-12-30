from setuptools import setup, find_packages

__name__ = "Mailgun-API"
__version__ = "0.1"
__doc__ = """Easy API access to mailgun!"""

setup(
 name = __name__,
 version = __version__,
 description = __doc__,
 py_modules = ['mailgun_api'],
  install_requires = [
  'requests',
 ],
 classifiers = [
  'Development Status :: 3 - Alpha',
  'Intended Audience :: Developers',
  'Programming Language :: Python',
  'Topic :: Software Development :: Libraries',
 ],
)
