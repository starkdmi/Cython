from setuptools import setup, Extension
from Cython.Distutils import build_ext

INCLUDES = [] # C includes, for example ["X11/Xlib.h"]
SRC_DIR = "pycdist"
SOURCES = [SRC_DIR + "/pycapp.pyx", SRC_DIR + "/lib/cfunc.c", SRC_DIR + "/lib/cplusfunc.cpp"] # C/C++ files
REQUIRES = ['cython'] # Python requires for .pyx file

ext_1 = Extension(SRC_DIR + ".pycapp",
                    sources=SOURCES,
                    libraries=INCLUDES,
                    #language="c++"
                )

if __name__ == "__main__":
    setup(install_requires=REQUIRES,
          script_args=['build'], 
          options={'build':{'build_lib':'.'}},
          packages=[SRC_DIR],
          zip_safe=False,
          name="pycapp",
          version="0.1",
          cmdclass={"build_ext": build_ext},
          ext_modules=[ext_1]
          )