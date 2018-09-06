import math

radius = 4000 # Radius of the earth in km considerd to be 4000 here as per problem statement 

def degreeToRadian(degree):
    return degree * (math.pi / 180)

def getDistanceBetweenTwoPints(la1, lo1, la2, lo2):
    dLo1 = degreeToRadian(lo1)
    dLo2 = degreeToRadian(lo2)
    dLa1 = degreeToRadian(la1)
    dLa2 = degreeToRadian(la2)
    z = math.sin(dLa1) * math.sin(dLa2) + math.cos(dLa1) * math.cos(dLa2) * math.cos(dLo1 - dLo2)
    return radius * math.acos(z)


def extractMin(coveredVertices, uncoveredVertices):
    minDist = math.inf
    vert = -1
    print("coveredVertices",coveredVertices)
    print("uncoveredVertices",uncoveredVertices)
    for i in coveredVertices:
        if(i[1] < minDist and i[0] in uncoveredVertices):
            minDist = i[1]
            vert = i[0]

    if(vert == -1):
        return uncoveredVertices[len(uncoveredVertices)-1]
    else:
        return vert


inputTupLat = (0,20,55)
inputTupLon = (-20,85,42)
canTravel =([1],[0],[0])
start = 0
end = 1

coveredVertices  = [[n,math.inf,''] for n in range(0,len(canTravel))] #all vertices which are not covered
uncoveredVertices = [n for n in range(0,len(canTravel))] #all vertices which are not covered
coveredVertices[0] = [0,0,0]

while len(uncoveredVertices) != 0:

    vert = extractMin(coveredVertices,uncoveredVertices)
    if(vert >= 0):
        for i in canTravel[vert]:
            dist = getDistanceBetweenTwoPints(inputTupLat[vert],inputTupLon[vert],inputTupLat[i], inputTupLon[i])
            if(dist + coveredVertices[vert][1] < coveredVertices[i][1]): #update the min dist if lesser than the value we alredy have
                coveredVertices[i][1] = dist + coveredVertices[vert][1] 
                coveredVertices[i][2] = vert

    uncoveredVertices.remove(vert)  #as the current vertice has been covered, let's remove it from list of uncovered vertices

print(coveredVertices)