import time
import sys

def solution(file):
    k = int(file.readline().strip().split()[1])

    diff = set()
    
    for d in file.readlines():
        diff.add(int(d.strip()))
        if len(diff) == k:
            sys.stdout.write(str(k))

    sys.stdout.write(str(len(diff)))



if __name__ == '__main__':
    start_time = time.perf_counter()
    solution(sys.stdin)
    end_time = time.perf_counter()
    print("\n" + f"Execution time: {end_time - start_time:.4f} seconds")