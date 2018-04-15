# ProjectEueler Problem 3: largest prime factor
# Ari Larson 04/14/2018
import math
import sys

def main():
    if len(sys.argv) > 1: TARGET = int(sys.argv[1])
    else: TARGET = 600851475143
    # print _rec_lpf(TARGET) or TARGET #print TARGET if prime
    print _iter_lpf(TARGET) or TARGET

def _rec_lpf(n, d=2, b=1):
    ''' recursive find largest prime. appears to work well for
        small numbers, but I don't have enough recursion depth
        for really big ones oops.

        @n: number to factor
        @d: current divisor to check
        @b: biggest divisor found so far
    '''
    #base
    if d >= math.sqrt(n):
        if b == 1: return None #target was prime..
        elif not n%d: return d #perfect square
        else: return max(b,n)
    # if divisor:
    if not n%d:
        print "{} divides by {} for {}".format(n, d, n/d)
        return _rec_lpf(n/d, d, b=d)
    # keep looking, even though d+1 may be multiple of checked #..
    else: return _rec_lpf(n, d+1, b=b)

def _iter_lpf(n):
    ''' iterively find largest prime factor
    '''
    sn = int(math.sqrt(n))
    print sn
    d = 2
    b = None
    while n >= sn:
        if not n%d: #divisor
            print "{} divides by {} for {}".format(n, d, n/d)
            n/=d
            b = d
        else: d += 1
    return max(b,n)

if __name__ == '__main__':
    main()
