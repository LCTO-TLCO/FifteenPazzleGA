from indivisual import Indivisual
import random
import numpy as np


class FifteenPazzle:
    def __init__(self):
        # defines
        self.indivisuals_num = 100
        self.max_epock = 300
        self.prob_cross = 0.5

        self.init_status = list(range(1, 16, 1))
        self.correct_status = self.init_status
        random.shuffle(self.init_status)
        self.best_fitness = 0
        self.selected = []
        # init indivisuals
        self.indivisuals = []
        for i in range(self.indivisuals_num):
            self.indivisuals.append(Indivisual(self.init_status))

    def run(self):
        for i in range(self.max_epock):
            self.evaluation()
            self.selection()
            self.crossover()
            print("best[{}] : {}".format(i, self.best_fitness)) if i % 250 == 0 else None

    def evaluation(self):
        for i in self.indivisuals:
            fitness = i.eval(self.correct_status)
            if self.best_fitness < fitness:
                self.best_fitness = fitness

    def selection(self):
        self.selected = []
        # make roulette
        weight = ()
        for i in self.indivisuals:
            weight += tuple(i.fitness)
        w = np.array(weight) / sum(weight)
        # select
        for selection in range(self.indivisuals_num):
            self.selected.append(np.random.choice(self.indivisuals, p=w))

    def crossover(self):
        pass


if __name__ == "__main__":
    main = FifteenPazzle()
    main.run()
