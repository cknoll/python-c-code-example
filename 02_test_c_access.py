# -*- coding: utf-8 -*-


"""
testing the c_code_interface
"""

from IPython import embed as IPS
import ctypes as ct

import c_code_interface as ci

from generate_code import func1 # lambda


f1 = ci.getFunc('funcs.so', 'func1_c', 1)





IPS()