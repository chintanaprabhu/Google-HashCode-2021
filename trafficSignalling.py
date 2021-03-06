file = 'Input/c.txt'
outputfile = 'Output/c.txt'
with open(file, 'r') as f:
    # Reading simulation, intersections, streets, cars and points
    line = f.readline()
    temp = list(map(int, line.split()))
    simulation = temp[0]
    intersections = temp[1]
    streets = temp[2]
    cars = temp[3]
    points = temp[4]

    # Initialize Variables
    inDegrees = {}
    streetCount = 0
    carCount = 0
    paths = []
    pathSet = set()
    route = [[0 for i in range(intersections)] for j in range(intersections)]
    streetToIndex = {}
    streetToEnd = {}
    map = {}
    visited = set()
    inDegreeStreets = {}
    # Initializing route matrix
    for line in f.readlines():
        if streetCount != streets:
            temp = line.split()
            source = int(temp[0])
            dest = int(temp[1])
            street = temp[2]
            time = int(temp[3])
            route[source][dest] = 1
            streetCount += 1
            map[street] = [source, dest,time]
            streetToEnd[dest] = street
            streetToIndex[source] = street
        else:
            # Initializing paths travelled
            temp = line.split()
            # print(temp)
            path = []
            for i in range(int(temp[0])):
                pathSet.add(temp[i + 1])
                path.append(temp[i + 1])
            paths.append(path)
            carCount += 1
    print(route)
    print(paths)
    print(streetToIndex)
    print(map)
    matrixTranspose = [list(i) for i in zip(*route)]
    n = len(matrixTranspose)
    for i in range(n):
        row = matrixTranspose[i]
        inDegreeStreets[i] = []
        if row.count(1)>1:
           if i in inDegrees:
               inDegrees[i] += 1
           else:
               inDegrees[i] = 2
           length = len(row)
           for j in range(length):
               r = row[j]
               #print('here', r)
               if r==1:
                   inDegreeStreets[i].append(streetToIndex[j])
                   #print('here',j)

    print(inDegrees)
    print(streetToEnd)
    lightsCount = len(inDegrees)
    text = ""
    with open(outputfile, 'w') as f:
        for path in paths:
            for p in path[1:]:
                if map[p][0] not in inDegrees and map[p][0] not in visited:
                    text += str(map[p][0])+"\n"+"1"+"\n"+streetToEnd[map[p][0]]+" "+"1"+"\n"
                    visited.add(map[p][0])
                    #print(p, map[p][0])
                    lightsCount += 1
        for key,value in inDegrees.items():
            text+=str(key)+"\n"+str(value)+"\n"
            roads = inDegreeStreets[key]
            val = 1
            flag = 0
            for r in roads:
                if not flag:
                    val = 1
                else:
                    val = 2
                text+= r+" "+str(val)+"\n"
                flag = not flag
                #print(roads)

        print(lightsCount)
        print(text)
        f.write(str(lightsCount)+"\n")
        f.write(text)



