import sys
import time
def solution(stdin):
    n = int(stdin.readline().strip())
    
    dist = stdin.readline().strip().split()
    a = int(dist[0]/3)
    b = int(dist[-1]/3)

    

    
    

    return




if __name__ == '__main__':
    start_time = time.perf_counter()
    solution(sys.stdin)
    end_time = time.perf_counter()
    print("\n" + f"Execution time: {end_time - start_time:.4f} seconds")