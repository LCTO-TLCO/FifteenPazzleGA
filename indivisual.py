from gene import Gene


class Indivisual:
    def __init__(self, init_status):
        self.max_genes = 100
        self.status = []
        self.genes = []
        self.min_fitness = self.max_genes + 64
        self.fitness = 0
        gene = Gene()
        gene.setGene(init_status)
        self.genes.append(gene)
        # run

    def eval(self, correct_status):
        # if correct
        for i in self.genes:
            if i == correct_status:
                self.fitness = self.min_fitness - self.genes.index(i)
                return self.fitness
        # if not correct
        self.fitness = self.min_fitness - (self.max_genes + self.distance())
        return self.fitness

    def distance(self):
        gene = self.genes[-1]
        distance = 0
        for i in range(16):
            distance += abs(int(i / 4) - self.genes.index(i)) + abs((i % 4) - self.genes.index(i) % 4)
            return distance

    def cross_over(self):
        pass
