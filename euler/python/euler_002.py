# ProjectEueler Problem 2: even fibs
# Ari Larson 04/14/2018

import sys

def main():
    if len(sys.argv) > 1: TARGET = int(sys.argv[1])
    else: TARGET = 4000000
    print _even_fib(TARGET)

def _even_fib(target, l0=0, l1=1):
    ''' i vaguely remember that there are more efficient ways to do this but meh
        @l1: two fibs ago
        @l0: last fib
    '''
    ret = l0 + l1
    if ret < target:
        # ignore odd:
        if ret%2: return   _even_fib(target, l0=ret, l1=l0)
        else: return ret + _even_fib(target, l0=ret, l1=l0)
    else:
        return 0

if __name__ == '__main__':
    main()
