# ProjectEueler Problem 1: "do you know what mod is"
# Ari Larson 04/14/2018

import sys

def main():
    if len(sys.argv) > 1: TARGET = int(sys.argv[1])
    else: TARGET = 1000

    sum = 0
    for i in range(TARGET):
         if not (i%3 and i%5):
    	sum+=i
    print sum

if __name__ == '__main__':
    main()
