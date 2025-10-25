import sys

def solve(input):
    lines = input.split('\n')
    minx, maxx = float('inf'), 0
    miny, maxy = float('inf'), 0
    for line in lines[1:]:
        x, y = map(int, line.split())
        minx = min(minx, x)
        maxx = max(maxx, x)
        miny = min(miny, y)
        maxy = max(maxy, y)
    sys.stdout.write("4\n")
    ans =[(maxx, maxy), (minx, maxy), (minx, miny), (maxx, miny)]
    for i in range(4):
        write = str(ans[i][0]) + " " + str(ans[i][1])
        sys.stdout.write(write)
        sys.stdout.write('\n')

if __name__ == "__main__":
    input = sys.stdin.read()
    solve(input)
