import sys
from collections import deque

def solve(input):
    lines = input.split('\n')
    #print(lines)
    n, m = lines[0].split()
    connections = dict()
    one, two = lines[-1].split()
    for i in range(1, int(m)+1):
        frm, to = lines[i].split()
        #print(frm, to, connections)
        if connections.get(frm):
            connections[frm].append(to)
        else:
            connections[frm] = [to]
    #print(connections)
    q = deque()
    q.append((one, one))
    q.append((two, two))
    onereach = set()
    tworeach = set()
    while q:
        #print(q)
        #print(onereach, tworeach)
        cur, group = q.popleft()
        if group == one:
            curset = onereach
        else:
            curset = tworeach
        if not connections.get(cur):
            continue
        for val in connections.get(cur):
            if val not in curset:
                q.append((val, group))
                curset.add(val)
        if onereach.intersection(tworeach):
            station = list(onereach.intersection(tworeach))[0]
            sys.stdout.write("yes\n")
            sys.stdout.write(station)
            return
    sys.stdout.write("no")

if __name__ == "__main__":
    solve(sys.stdin.read())
