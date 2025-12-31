#You can use this if you want to upgrade the CPU bound of a your code
from Cython.Build import cythonize
from setuptools import setup
def set_C(file:str):
    setup(
        ext_modules=cythonize(file, compiler_directives={'language_level':'3'}),
        zip_safe=False,
    )
#ext_modules:lista moduli da compilare in C
#cythonize:converte .py in .c .so
#language_level:'3': usa python3 oer faegli capire come è composta la sintassi
#zip_safe=False:non comprime i binari

