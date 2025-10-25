import sys
import math
max = 0
def distance(p1, p2):
    x = (p1[0] - p2[0]) ** 2
    y = (p1[1] - p2[1]) ** 2

    return math.sqrt(x+y)

def check(p1, p2, p3):
    global max
    d1 = distance(p1,p2)
    d2 = distance(p2,p3)
    d3 = distance(p1,p3)
    d_new = math.sqrt((d3**2)/2)
    
    gain = 2*d_new - d1 - d2
    if gain > max:
        max = gain

def solve(file):
    n = int(file.readline().strip())
    p1 = list(map(int, file.readline().strip().split(" ")))
    p2 = list(map(int, file.readline().strip().split(" ")))
    p1_init, p2_init = p1, p2
    for i in range(n-2):
        p3 = list(map(int, file.readline().strip().split(" ")))
        check(p1,p2,p3)
        p1, p2 = p2, p3

    p3 = p1_init
    check(p1,p2,p3)

    p1,p2,p3 = p2,p3,p2_init
    check(p1,p2,p3)

    sys.stdout.write(str(max))







if __name__ == "__main__":
    solve(sys.stdin)