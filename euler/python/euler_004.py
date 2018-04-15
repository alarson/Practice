# ProjectEueler Problem 3: largest prime factor
# Ari Larson 04/14/2018
import math
import sys

def main():
    if len(sys.argv) > 1: TARGET = int(sys.argv[1])
    else: TARGET = 3
    print _lpn(TARGET)

def _lpn(m):
    ''' @m: magnitude
    '''

    a = b = 10**m - 1
    m = a*b
    best = a
    # print m, a, b
    for i in range(a,0,-1):
        for j in range(b,0,-1):
            if _pally(i*j):
                # print "{}x{}={}".format(i,j,i*j)
                best = max(best,i*j)
    return best
    # while m>a:
    #     if _pally(m) and
    #         return m
    #     else: m-=1
def _pally(n):
    ''' is palindrome?
    '''
    s = str(n)
    return all([s[i] == s[len(s)-i-1] for i in range(0,len(s)/2)])
if __name__ == '__main__':
    main()
