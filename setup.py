from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        "cudasift.cudasift",
        ["cudasift/_cudasift.pyx"],
        include_dirs=['/usr/local/cuda/include','/usr/local/'], # not needed for fftw unless it is installed in an unusual place
        libraries=['cudasift.so'],
        library_dirs=['/usr/local/lib'], # not needed for fftw unless it is installed in an unusual place
    ),
]

setup(
    name = "cudasift",
    packages = find_packages(),
    ext_modules = cythonize(extensions)
)
