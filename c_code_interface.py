
"""
module for easy access to self written c functions, which are stored in a
shared lib


For further information see:

https://docs.python.org/2.7/library/ctypes.html

or

https://docs.python.org/3.5/library/ctypes.html

(depending on your python version)
"""

import ctypes as ct

import inspect
import os.path as pp


# get the path
path2thismodule = pp.realpath(pp.dirname(inspect.getfile(lambda :1)))
LIBDIR = path2thismodule


def getFunc(libName, fncName, numRetVals):
    """
    This is a helper function which which wraps some often used functionality
    of the ctypes library.

    It supposes that the function which will be imported only takes arguments
    of type double


    libName:    name of the shared library (.so or .dll)
    fncName:    name of the function to be imported

    numRetVals: length of the array with the return values
    """

    lib = ct.cdll.LoadLibrary(LIBDIR+"/"+libName)

    the_c_func = getattr(lib, fncName)

    # this converts the result in a python float obj:
    the_c_func.restype = ct.c_double

    def thefunc(*args):

        c_args=map(ct.c_double, args)

        res = the_c_func(*c_args)

        # res == 0?

        return res

    return thefunc
