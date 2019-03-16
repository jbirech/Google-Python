"""
Simple python algorithm to convert temperatures from celsius into farenheight.
"""
import sys

def Covert(C):
    F = C * 1.8 + 32
    print(F)
    return F

def backCov(f):
    c = (f - 32)/1.8
    print(c)
    return c


if __name__ == '__main__':
    #Covert(sys.argv[1])
    Covert(8)
    backCov(46.4)
