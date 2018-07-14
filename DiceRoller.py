import random

# How many times to run the experiement
numRolls = 1000000
# buckets to keep track of how many times a particular sum shows up
buckets = [0] * (108)

# begin rolling
for x in range(numRolls):

    # 6 different stats, for str, dex, con, etx
    stats = [0,0,0,0,0,0]
    for y in range(6):
        # roll 4 times for each stat
        numD6 = 4
        rolls = [0] * numD6
        for z in range(numD6):
            rolls[z] = random.randint(1,6)
        # Drop the lowest
        rolls.remove(min(rolls))
        #sum the remaining values to get the stat value
        stats[y] = sum(rolls)
    # Sum all the stats and put it in the appropriate bucket counter
    buckets[sum(stats)] += 1

for x in range(108):
    print("Percent chance for {}: {:.6f}".format(x + 1, buckets[x] / numRolls))