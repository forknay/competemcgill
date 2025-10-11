import sys
from statistics import mean, variance

def solve(input):
    lines = input.split("\n")
    n, k = map(int, lines[0].split())
    data = sorted(list(map(int, lines[1:])))
    # First off find our collection
    i, j = 0, k # Exclusive
    curminbad = float('inf')
    while j <= n:
        #print(data[i:j])
        var = variance(data[i:j])
        #print(var)
        curminbad = min(var, curminbad)

        i += 1
        j += 1
    sys.stdout.write(str(curminbad))

if __name__ == "__main__":
    input = sys.stdin.read()
    solve(input)
