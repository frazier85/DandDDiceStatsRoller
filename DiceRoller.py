import random

buckets = [0] * (108)
for x in range(1000000):
    stats = [0,0,0,0,0,0]
    for y in range(6):
        rolls = [0,0,0,0]
        for z in range(4):
            rolls[z] = random.randint(1,6)
        rolls.remove(min(rolls))
        stats[y] = sum(rolls)
    buckets[sum(stats)] += 1

for x in range(108):
    print("Percent chance for {}: {:.6f}".format(x + 1, buckets[x] / 1000000))