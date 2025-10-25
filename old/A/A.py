import time
import sys

def findLED():
    lines = sys.stdin.readlines()
    needs = lines[0]
    owns = lines[1]
    available = lines[2]
    
    # split to find r, g, b
    needsList = needs.split()
    needR= int(needsList[0])
    needG= int(needsList[1])
    needB= int(needsList[2])
    ownsList = owns.split()
    ownedR= int(ownsList[0])
    ownedG= int(ownsList[1])
    ownedB= int(ownsList[2])
    availableList = available.split()
    specRG= int(availableList[0])
    specGB= int(availableList[1])

    # how many to buy:
    buyR = needR - ownedR
    buyG = needG - ownedG
    buyB = needB - ownedB
    
    if buyR <= 0:
        buyR = 0
    if buyG <= 0:
        buyG = 0
    if buyB <= 0:
        buyB = 0

    if buyR > specRG or buyB > specGB:
        return - 1
    else:
        #buy the red and the blues
        boughtB = buyB
        boughtR = buyR
        #subtract from spec available
        specRG = specRG - buyR
        specGB = specGB - buyB
        # add the remainder to see if you have enough for G
        totG = specRG + specGB

        if buyG > totG:
            return -1
        else:
            # buy the green
            boughtG = buyG
            return boughtG + boughtB + boughtR



# start_time = time.perf_counter()
sys.stdout.write(str(findLED()))
print("hi")
# end_time = time.perf_counter()

# elapsed_time = end_time - start_time
# print(f"Execution time: {elapsed_time:.4f} seconds")





