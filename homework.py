f = open("homework.in", "r")
g = open("homework.out", "w")
lines = f.readlines()
num_scores = int(lines[0])
scores = list(map(int, lines[1].split(" ")))

currentSum = 0
currentMin = 10000000000000000
bestSum = 0
bestLength = 1
result = []
for i in range(num_scores - 1, 0, -1):
    # Continually add on another score from the end of the list, thus reducing the number of scores eaten by the cow
    currentSum += scores[i]
    currentMin = min(currentMin, scores[i])
    print("%i %i" % (i, currentMin))
    if i <= num_scores - 2 and (currentSum - currentMin) * bestLength > (bestSum) * (
        num_scores - i - 1
    ):

        bestSum = currentSum - currentMin
        bestLength = num_scores - i - 1
        result = []
        result.append(i)
    elif i <= num_scores - 2 and (currentSum - currentMin) * bestLength == (bestSum) * (
        num_scores - i - 1
    ):
        result.insert(0, i)

for i in result:
    g.write("%i\n" % i)
g.close()
