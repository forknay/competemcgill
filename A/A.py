import math
import sys


def a(input):
    lines = input.split()
    l = int(lines[0])
    r = int(lines[1])


    if (l <= r):
        result = math.comb(l+r, l)
    else:
        if (r == 1):
            if (l % 2 == 0):
                result = (l + r)*2
            elif (l % 2 == 1):
                result = (l + r)* 2 - 1
        else:
            result = math.comb(l+r, l) - l - r
    
    return result

if __name__ == "__main__":
    input = sys.stdin.read()
    sys.stdout.write(str(a(input)))
