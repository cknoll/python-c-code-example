"""
testing the c_code_interface
"""

# pip install ipydex (useful for interactive exploring)
from ipydex import IPS
import ctypes as ct

import c_code_interface as ci

# from generate_code import func1 # lambda


f1 = ci.getFunc('funcs.so', 'func1_c', 1)


# start interactive shell
# type e.g. f1(1, 2, 3)
IPS()
