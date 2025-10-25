import sys
import math

def curlingGame():
    pointsRed = pointsYellow = 0
    lines = [ln.strip() for ln in sys.stdin if ln.strip()]

    for i in range(0, len(lines), 2):
        # process data
        stonesR = list(map(int, lines[i].split()))
        stonesY = list(map(int, lines[i+1].split()))
        nrStonesR, nrStonesY = stonesR[0], stonesY[0]

        distR = []
        distY = []

        # build distance (using math.hypoth) lists from lines
        for j in range(1, 2*nrStonesR, 2):
            distR.append(math.hypot(stonesR[j] - 144, stonesR[j+1] - 84))

        for j in range(1, 2*nrStonesY, 2):
            distY.append(math.hypot(stonesY[j] - 144, stonesY[j+1] - 84))

        # sort the list from closest to farthest
        distR.sort()
        distY.sort()

        # check if the distance lists are not empty
        if not distR and not distY:
            continue

        if distR and (not distY or distR[0] < distY[0]):
            # red scores, check how many points they scored
            max = distY[0]
            for d in distR:
                if d < max:
                    pointsRed += 1
                else:
                    break

        elif distY and (not distR or distY[0] < distR[0]):
            # yellow scores, check how many points they scored
            max = distR[0]
            for d in distY:
                if d < max:
                    pointsYellow += 1
                else:
                    break

    return str(pointsRed)+" "+str(pointsYellow)

sys.stdout.write(curlingGame())


