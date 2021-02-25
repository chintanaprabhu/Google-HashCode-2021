import codecs

class DeliverPizzas:
    def __init__(self):
        self.numPizzas = 0
        self.twoMemTeams = 0
        self.threeMemTeams = 0
        self.fourMemTeams = 0

    def DeliverPizzas(self, inputData):
        lines = inputData.split('\n')
        metaData = lines[0]
        self.numPizzas = metaData[0]
        self.twoMemTeams = metaData[1]
        self.threeMemTeams = metaData[2]
        self.fourMemTeams = metaData[3]
        return "ok"
