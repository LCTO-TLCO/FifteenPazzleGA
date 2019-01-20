class Gene:
    def __init__(self):
        self.max_length = 16
        self.gene = []
        self.action = []

    def setGene(self, board_status):
        self.gene = board_status
        self.calcAction()

    def actGene(self, destination):
        self.gene[destination], self.gene[self.gene.index(16)] = \
            self.gene[self.gene.index(16)], self.gene[destination]
        self.calcAction()
        return self

    def calcAction(self):
        self.action = []
        # search 16
        blank = self.gene.index(16)
        # up
        if not blank < 4:
            self.action.append(blank - 4)
        # down
        if not blank > 11:
            self.action.append(blank + 4)
        # left
        if not blank % 4 == 0:
            self.action.append(blank - 1)
        # right
        if not blank % 4 == 3:
            self.action.append(blank + 1)

    # for cross over
    def getConnectionPoint(self, other_gene):
        pass
