# -*- coding: utf-8 -*-


import sys
import sympy as sp
import os


# for debugging
# from IPython import embed as IPS

"""
This script demonstrates how to generate C-code from some sympy expression.

It also contains commands to compile that C-code. However they will probably
only work under some Unix-based OS.

Under debian / ubuntu it might be necessary to run

sudo apt install build-essential

before

"""




from sympy.abc import x,y,z

# expr = x*100+y**2 + 0.001 * z**3
expr = x*1000 + y*100 + z*10


func1 = sp.lambdify((x,y,z), expr)


def main():
    src = """
    #include <math.h>

    double func1_c(double x, double y, double z)
    {

        double res;
        res = %s;

        return res;
    }
    """ % sp.ccode(expr)

    print(src)

    cfilename = "funcs.c"
    ofilename = "funcs.o"
    sofilename = "funcs.so" # shared object
    with open(cfilename, "w") as myfile:
        myfile.write(src)
        print(cfilename, "written")

    print("\nCompiling:")

    cmd1 = "gcc -c -fPIC -lm %s -o %s" % (cfilename, ofilename)
    print(cmd1)
    os.system(cmd1)

    print("\nCreating shared library:")

    cmd2 = "gcc -shared %s -o %s" %(ofilename, sofilename)
    print(cmd2)
    os.system(cmd2)


if __name__ == "__main__":
    main()
