file = 'Input/a.txt'
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
    map = {}

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
            streetToIndex[source] = street
            map[street] = [source, dest,time]
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
    print(pathSet)
    print(streetToIndex)
    print(map)
    # Initializing inDegrees
    # for i in pathSet:
    #     for j in paths:
    #         if i in j:
    #             if i in inDegrees:
    #                 inDegrees[i] += 1
    #             else:
    #                 inDegrees[i] = 1
    # print(inDegrees)

