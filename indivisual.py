from gene import Gene
import numpy as np


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
        # init run
        for i in range(self.max_genes):
            self.genes.append(self.genes[-1].actGene(np.random.choice(self.genes[-1].action)))

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
        for i in range(1,16+1):
            distance += abs(int(i / 4) - gene.gene.index(i)) + abs((i % 4) - gene.gene.index(i) % 4)
            return distance

    def cross_over(self):
        pass
