import os
import sys
 
pycDist = os.path.dirname(os.path.abspath(__file__)) + "\\pycdist\\"

if os.path.isfile(pycDist + "__init__.pyc"):
    try:
        os.remove(pycDist + "__init__.pyc")
    except: 
        pass

if os.path.isfile(pycDist + "pycapp.c"):
    try:
        os.remove(pycDist + "pycapp.c")
    except: 
        pass

if os.path.isfile(pycDist + "pycapp.cpp"):
    try:
        os.remove(pycDist + "pycapp.cpp")
    except: 
        pass

if os.path.isfile(pycDist + "pycapp.pyd"):
    try:
        os.remove(pycDist + "pycapp.pyd")
    except: 
        pass

try: 
    os.system("python setup.py develop")
except: 
    pass

