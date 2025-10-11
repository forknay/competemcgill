import sys
from statistics import variance

def solve(input):
    lines = input.split("\n")
    n, k = map(int, lines[0].split())
    #print(lines)
    data = []
    for x in lines[1:]:
        x = x.strip()
        if x:
            data.append(int(x))
    data.sort()
    #print(data)
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
