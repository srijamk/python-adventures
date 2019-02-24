def reststops(file_name):
    f = open(file_name, 'r')
    g = open('reststops.out', 'w')
    lines = f.read().splitlines()
    bp = list(map(int, lines[0].split(" ")))
    hikeLength = bp[0]
    numRestStops = bp[1]
    farmerSpeed = bp[2]
    bessieSpeed = bp[3]
    restStops = []
    isMax = []
    totalValue = 0
    for i in range(numRestStops):
        stop = list(map(int, lines[i + 1].split(" ")))
        restStops.append([stop[0], stop[1]])
        isMax.append(False)

    maxRestStop = 0
    for i in range(numRestStops - 1, -1, -1):
        if restStops[i][1] > maxRestStop:
            maxRestStop = restStops[i][1]
            isMax[i] = True

    lastStop = 0
    for i in range(0, numRestStops):
        if isMax[i]:
            if i == 0:
                totalValue += restStops[i][0] * (farmerSpeed - bessieSpeed) * restStops[i][1]
            else:
                totalValue += (restStops[i][0] - lastStop) * (farmerSpeed - bessieSpeed) * restStops[i][1]
            lastStop = restStops[i][0]
    
    g.write("%i\n" % totalValue)
    print(totalValue)
reststops('reststops.in')
