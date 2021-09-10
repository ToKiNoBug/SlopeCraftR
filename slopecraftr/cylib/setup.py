from setuptools import Extension, setup
from Cython.Build import cythonize

file_name = 'cy_api'
full_file_name = f'{file_name}.pyx'
ext = [Extension(file_name, [full_file_name])]

if __name__ == '__main__':
    setup(
        name=file_name,
        ext_modules=cythonize(ext)
    )
