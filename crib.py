import numpy as np

class Node:

    def __init__(self):
        self.infoset = ""
        self.regretSum = []
        self.strategy = []
        self.strategySum = []
        self.NUM_ACTIONS = 6


    def getStrategy(self, realizationWeight):

        normalizingSum = 0

        for a in range(self.NUM_ACTIONS):
            
            if regretSum[a] > 0:
                self.strategy[a] = self.regretSum[a]
            else:
                self.strategy[a] = 0
            
            normalizingSum += self.strategy[a]

        for a in range(self.NUM_ACTIONS):
            if normalizingSum > 0:
                self.strategy[a] /= normalizingSum

            else:
                self.strategy[a] = 1.0 / self.NUM_ACTIONS

            self.strategySum[a] += realizationWeight * self.strategy[a]

        return self.strategy

    def getAverageStrategy(self):
        
        avgStrategy = []
        normalizingSum = 0

        for a in range(self.NUM_ACTIONS):
            normalizingSum += self.strategySum[a]

        for a in range(self.NUM_ACTIONS):

            if normalizingSum > 0:
                avgStrategy[a] = self.strategySum[a] / normalizingSum
            else:
                avgStrategy[a] = 1.0 / NUM_ACTIONS

        return avgStrategy

        def str_rep(self):
            return self.infoset + " " + str(*self.getAverageStrategy())

def train(iterations):
     
    cards = list(range(52))
    util = 0
    
    for _ in range(iterations):
        np.random.shuffle(cards)

        util = += cfr(cards, "", 1, 1)
    
    print("Average: " + str(util / iterations))
    for node in NodeMap:
        print(node)
        

def cfr(cards, history, p0, p1):

    plays = len(history)

    if plays > 1:
        return

    