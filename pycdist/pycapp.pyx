cimport cython

# Using C function example
cdef extern from "lib/cfunc.h":
    void hello()

def c_hello():
    hello()

# Using C++ function example
'''cdef extern from "lib/cplusfunc.cpp":                                      
    void hello() 
    
def cplus_hello():
    hello()'''

def myfunc():
    print "Hello World!"
    