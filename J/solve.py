import sys
import time

def solve(input):
    # 1, 10, 11, ..., 19, 21, 31, 41, 51, 61, 71, 81, 91, 100
    
    sys.stdout.write(input.split()[-1][-1])
    #print(input.split()[-1][-1])

if __name__ == "__main__":
     #start = time.perf_counter()
     solve(sys.stdin.read())
     #end = time.perf_counter()
     #print(end - start)