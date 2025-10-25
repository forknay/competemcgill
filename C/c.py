import sys

l = []

def ans():
    for a in l[:-1]:
        sys.stdout.write(str(a) + " ")
    sys.stdout.write(str(l[-1]))
    # sys.stdout.write("\n")
    exit()

def solve(file):
    n, t = map(int, file.readline().strip().split(" "))
    for a in file.readline().strip().split(" "):
        l.append(int(a))

    for g in range(t):
        hand = 1
        for i in range(n):
            if hand == 1:
                if not l[i]:
                    l[i] += 1
                    break
                hand += l[i]
                l[i] = 0
            else:
                hand -= 1
                l[i] += 1

    ans()

        

    



if __name__ == "__main__":
    solve(sys.stdin)