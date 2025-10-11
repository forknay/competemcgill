# I1 : r, c, n
# I2-n+1 : i, j
import sys

def solve(input):
    # edit input
    lines = input.split('\n')
    r, c, n = map(int, lines[0].split())
    # Initialize grid
    grid = [[[0,0] for _ in range(c)] for _ in range(r)]
    # Read tower positions
    cur = 1
    towers = []
    for line in lines[1:n+1]:
        #print(line)
        i, j = map(int, line.split())
        #print(i,j)
        towers.append((i-1,j-1, cur))
        grid[i-1][j-1][0] = cur
        cur += 1
    #for l in grid:
    #    print(l)
    #OK ABOVE
    dir = [(0,1),(1,0),(0,-1),(-1,0)]
    # Rough just iterate
    no_change = True
    start = 0
 
    while start < len(towers):
        t = towers[start]
        start += 1
        i, j, id = t
        for d in dir:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < r and 0 <= nj < c:
                if grid[ni][nj][0] == 0:
                    grid[ni][nj][0] = id
                    towers.append((ni,nj,id))
                elif grid[ni][nj][1] == 0 and grid[ni][nj][0] != id:
                    grid[ni][nj][1] = id
                    towers.append((ni,nj,id))
    for l in grid:
        sys.stdout.write(' '.join([str(x[0]) for x in l]) + '\n')
    
    for l in grid:
        sys.stdout.write(' '.join([str(x[1]) for x in l]) + '\n')
           
                    
if __name__ == "__main__":
    input = sys.stdin.read()
    solve(input)

    """input = "500,500,3\n1,1 \n4,1 \n2,6"
    start = time.perf_counter()
    solve(input)
    time.sleep(2)
    end = time.perf_counter()
    print(end - start)"""