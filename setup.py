#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
pyCLE v0.1
Python-wrapped coronal line polarized package

For more information see:
::
    Main Changes in 0.0
    ---------------------
    * Working version
:copyright:
    T. Schad
:license:
    The MIT License (MIT)
"""

from setuptools import find_packages , setup
from setuptools.extension import Extension
from distutils.ccompiler import CCompiler
from distutils.errors import DistutilsExecError, CompileError
from distutils.unixccompiler import UnixCCompiler

import os
import platform
import sys
import numpy
import glob
import re

DOCSTRING = __doc__.strip().split("\n")

tmp = open('pywigner/__init__.py', 'r').read()
author = re.search('__author__ = "([^"]+)"', tmp).group(1)
version = re.search('__version__ = "([^"]+)"', tmp).group(1)

if(platform.system() == 'Darwin'):
    CC = 'clang'
    os.environ["CC"] = CC
    from distutils import sysconfig
    sysconfig.get_config_vars()['CC'] =  CC
    sysconfig.get_config_vars()['LDSHARED'] = CC
    link_opts=["-bundle","-undefined","dynamic_lookup"]
else:
    CC = 'gcc'
    link_opts = []

def _compile(self, obj, src, ext, cc_args, extra_postargs, pp_opts):
    compiler_so = self.compiler_so
    arch = platform.architecture()[0].lower()
    if (ext == ".f" or ext == ".f90"):
        if sys.platform == 'darwin' or sys.platform.startswith('linux'):
            compiler_so = ["gfortran"] # x86_64-conda_cos6-linux-gnu-gfortran"]
            if (ext == ".f90"):
                cc_args = ["-O3", "-march=native", "-fPIC", "-c", "-ffree-form","-ffree-line-length-none","-funroll-loops"]
            # Force architecture of shared library.
            if arch == "32bit":
                cc_args.append("-m32")
            elif arch == "64bit":
                cc_args.append("-m64")
            else:
                print("\nPlatform has architecture '%s' which is unknown to "
                      "the setup script. Proceed with caution\n" % arch)
    try:
        self.spawn(compiler_so + cc_args + [src, '-o', obj] +
                   extra_postargs)
    except DistutilsExecError as msg:
        raise CompileError(msg)

UnixCCompiler._compile = _compile

# Monkey patch the compilers to treat Fortran files like C files.
CCompiler.language_map['.f90'] = "c"
UnixCCompiler.src_extensions.append(".f90")

##CLE  --  these need to be in the right order
path = "src/"
list0 = ['wigner.f90','cywigner.pyx']
list_files = [path + s for s in list0]
lib_pycle = Extension('pywigner.codes.wigner_code',
                      extra_link_args=link_opts,
                      sources=list_files,
                      include_dirs=[numpy.get_include()])

setup_config = dict(
    name='pywigner',
    version=version,
    description=DOCSTRING[0],
    long_description="\n".join(DOCSTRING[2:]),
    author=author,
    author_email='tschad@nso.edu',
    license='GNU General Public License, version 3 (GPLv3)',
    platforms='OS Independent',
    install_requires=['numpy','cython'],
    ext_modules=[lib_pycle],
    keywords=['pycle'],
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
)

if __name__ == "__main__":
    setup(**setup_config)

    for filename in glob.glob("*.mod", recursive=True):
        try:
            os.remove(filename)
        except:
            pass
