import sys
import time

def subsets(nums):
        ans = []
        n = len(nums)
        def backtrack(cur, i):
            ans.append(cur[:])
            for j in range(i, n):
                cur.append(nums[j])
                backtrack(cur[:], j+1)
                cur.pop()
        backtrack([], 0)
        return ans

def solve(input):
    lines = input.split("\n")
    n = int(lines[0])
    team_cont = {0:0}
    for i, t in enumerate(lines[1].split()):
        team_cont[int(i)+1] = int(t)
    sub = subsets(list(map(int, lines[2].split())))
    # print(team_cont)
    # print(sub)
    # now check for answers
    tot = 0
    teamnum = 0
    for comp in sub:
        n = len(comp)
        curtot = sum(comp) + team_cont[n]
        if curtot > tot:
            tot = curtot
            teamnum = n
    ans = tot/teamnum
    print(str(ans), end="")


if __name__ == "__main__":
     #start = time.perf_counter()
     solve(sys.stdin.read())
     #end = time.perf_counter()
     #print(end - start)