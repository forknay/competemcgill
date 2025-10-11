import time
import sys

def solution(stdin):
    #limits
    limits = stdin.readline().strip().split()
    height, width = int(limits[0]), int(limits[1])
    
    #position & direction
    pos = stdin.readline().strip().split()
    y_init, x_init = int(pos[0])-1, int(pos[1])-1
    direction = 1 #0 up, 1 right, 2 down, 3 left

    #final position
    pos = stdin.readline().strip().split()
    y_final, x_final = int(pos[0])-1, int(pos[1])-1
    
    

    #conditions
    def cond1():
        nonlocal direction
        nonlocal x, y
        if direction == 0: #up
            if x <= 0:
                return False
            elif maze[y][x-1] == '1':
                return False
        elif direction == 1: #right
            if y <= 0:
                return False
            elif maze[y-1][x] == '1':
                return False
        elif direction == 2: #down
            if x >= (width - 1):
                return False
            elif maze[y][x+1] == '1':
                return False
        elif direction == 3: #left
            if y >= (height - 1):
                return False
            elif maze[y+1][x] == '1':
                return False
        return True
    def cond2():
        nonlocal direction
        nonlocal x, y
        if direction == 3: #left
            if x <= 0:
                return False
            elif maze[y][x-1] == '1':
                return False
        elif direction == 0: #up
            if y <= 0:
                return False
            elif maze[y-1][x] == '1':
                return False
        elif direction == 1: #right
            if x >= (width - 1):
                return False
            elif maze[y][x+1] == '1':
                return False
        elif direction == 2: #down
            if y >= (height - 1):
                return False
            elif maze[y+1][x] == '1':
                return False
        return True


    def turn_left():
        nonlocal direction
        direction = (direction - 1) % 4
    def turn_right():
        nonlocal direction
        direction = (direction + 1) % 4
    def move_forward():
        nonlocal x, y
        if direction == 0:
            y -= 1
        elif direction == 1:
            x += 1
        elif direction == 2:
            y += 1
        else: #direction == 3
            x -= 1

    maze = stdin.readlines()
    x, y = x_init, y_init
    while True:
        #print(x, y, direction)
        if (x, y) == (x_final, y_final):
            sys.stdout.write(str(1))
            return
        elif cond1():
            turn_left()
            move_forward()
        elif cond2():
            move_forward()
        else:
            turn_right()

        if (x, y, direction) == (x_init, y_init, 1):
            sys.stdout.write(str(0))
            return

if __name__ == '__main__':
    #start_time = time.perf_counter()
    solution(sys.stdin)
    # end_time = time.perf_counter()
    # print("\n" + f"Execution time: {end_time - start_time:.4f} seconds")