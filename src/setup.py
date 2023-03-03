from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

c_ext = Extension("networkinglib", sources=["networkinglib.py"])

setup(
    name='networkinglib',
    version='0.1',
    description='Extension providing a basic networking protcol implementations as a Python module using C-Extenstions.',
    ext_modules=[c_ext]
)