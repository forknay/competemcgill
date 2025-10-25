import math
import sys

def l(input):
    """lines = input.split()
    t = int(lines[0])
    if (t > 0) and (t <= 360):
        lunch = 0
    elif (t > 360) and (t <= 540):
        lunch = 30
    elif (t > 540) and (t <= 720):
        lunch = 45
    elif (t > 720) and (t <= 900):
        lunch = 60
    elif (t > 900) and (t <= 1080):
        lunch = 75
    elif (t > 1080) and (t <= 1260):
        lunch = 90
    elif (t > 1260) and (t <= 1440):
        lunch = 105
    return lunch"""
    t = int(input)
    time = 30
    if t <= 390:
        print(0, end="")
        return
    elif t > 645:
        """print(0, end="")
        return"""
        extra = t - 645
        time += extra
        t -= extra
    
    t -= 390
    while t > 195:
        t -= 195
        time += 15

    print(time, end="")


if __name__ == "__main__":
    input = sys.stdin.read()
    l(input)
