import sys

def maxcross(file_name):
    f = open(file_name, 'r')
    g = open('maxcross.out', 'w')
    lines = f.read().splitlines()
    boiler = list(map(int, lines[0].split()))
    N = boiler[0]
    K = boiler[1]
    B = boiler[2]
    lights = [1 for i in range(N)]

    for i in range(B):
        damagedLight = int(lines[i + 1])
        lights[damagedLight - 1] = 0
    
    currentSum = sum(lights[0:K])
    maxFixedLights = currentSum
    for i in range(1, N - K + 1): # 1, 2, 3, 4
        currentSum = currentSum - lights[i - 1] + lights[i + K - 1]
        maxFixedLights = max(currentSum, maxFixedLights)

    print(K - maxFixedLights)

    g.write("%i\n" % (K - maxFixedLights))

maxcross('maxcross.in')
