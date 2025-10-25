import time
import sys

def solve(input):
    # Try all subsets
    lines = input.split('\n')
    n, b, r, w = lines[0].split()
    nums = []
    ans = []
    nb = len(nums)
    def backtrack(cur, i):
        ans.append(cur[:])
        for j in range(i, nb):
            cur.append(nums[j])
            backtrack(cur[:], j+1)
            cur.pop()
    backtrack([], 0)
    



if __name__ == "__main__":

    start_time = time.perf_counter()
    input = sys.stdin.read()
    solve(input)
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    print(f"Execution time: {elapsed_time:.4f} seconds")