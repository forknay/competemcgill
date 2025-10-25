import sys
from collections import deque
def solve(input):
    lines = input.strip().split('\n')
    #print(lines)
    n, m = lines[0].split()
    connections = dict()

    one, two = lines[-1].split()
    for i in range(1, int(m)+1):
        frm, to = lines[i].split()
        #print(frm, to, connections)
        if connections.get(frm):
            connections[frm].add(to)
        else:
            connections[frm] = set([to])
    #print(connections)
    q = deque()
    q.append(one)
    
    onereach = set()
    tworeach = set()
    onereach.add(one)
    tworeach.add(two)
    while q:
        #print(q)
        #print(onereach, tworeach)
        cur = q.pop()
        if not connections.get(cur):
            continue
        
        for val in connections.get(cur):
            if val not in onereach:
                q.append(val)
                onereach.add(val)
    
    q.append(two)
    while q:
        #print(q)
        #print(onereach, tworeach)
        cur = q.pop()
        if not connections.get(cur):
            continue
        
        for val in connections.get(cur):
            if val not in tworeach:
                q.append(val)
                tworeach.add(val)
    
    if onereach.intersection(tworeach):
        station = list(onereach.intersection(tworeach))[0]
        sys.stdout.write("yes\n")
        sys.stdout.write(station)
    else:  
        sys.stdout.write("no")

if __name__ == "__main__":
    solve(sys.stdin.read())
