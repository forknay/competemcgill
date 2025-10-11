import sys
import time

def solve():
    moves = 0
    def found(moves, i, j):
        if moves <= 2:
            print("?", i, j-1, flush=True)
            if (sys.stdin.read() == "1"):
                i -= 1
                j -= 1
                print("?", i, j, flush=True)
            else:
                i -= 1
                j += 1
                print("?", i, j, flush=True)

            if (sys.stdin.read() == "1"):
                print("!", i, j, flush=True)
            else:
                print("!", i+1, j, flush=True)
            
        
    
    def found_loop(input, moves):

    def loop(input, moves):
        if moves == 0:
            print("? 4 2 ", flush=True)
            moves += 1
        elif moves == 1:
            if input == 0:
                print("? 4 4 ", flush=True)
            else:
                print("? ")
        elif 
print("? 1 4 ", flush=True)
time.sleep(1)
print(sys.stdin.read(), flush=True)
