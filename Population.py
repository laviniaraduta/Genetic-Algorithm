from random import random, randint

def reMap(value, minInput, maxInput, minOutput, maxOutput):
    value = maxInput if value > maxInput else value
    value = minInput if value < minInput else value

    inputSpan = maxInput - minInput
    outputSpan = maxOutput - minOutput

    scaledThrust = float(value - minInput) / float(inputSpan)

    return minOutput + (scaledThrust * outputSpan)  

class DNA:
    def __init__(self, num):
        self.alphabet = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM "
        self.genes = []
        self.fitness = 0
        for i in range(num):
            self.genes.append(self.alphabet[randint(0, 10000) % 53])
        
    def getPhrase(self):
        phrase = ""
        return phrase.join(self.genes)
    
    def setFitness(self, target):
        score = 0.0
        for i in range(len(self.genes)):
            if self.genes[i] == target[i]:
                score += 1
        self.fitness = 1.0 * score / len(target)
    
    def crossover(self, other):
        child = DNA(len(self.genes))
        midpoint = randint(0, len(self.genes) - 1)
        for i in range (0, len(self.genes)):
            if i > midpoint:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = other.genes[i]
                
        return child
    
    def mutate(self, mutationRate):
        for i in range(len(self.genes)):
            rand = random()
            if rand < mutationRate:
                self.genes[i] = self.alphabet[randint(0, 10000) % 53]

class Population():
    def __init__(self, target, mutationRate, num):
        self.target = target
        self.mutationRate = mutationRate
        self.generations = 0
        self.perfectScore = 1
        self.isFinished = False
        self.populationLen = num
        self.population = []
        for i in range(self.populationLen):
            self.population.append(DNA(len(self.target)))
        self.calcFitness()
        self.matingPool = []

    def calcFitness(self):
        for i in range(self.populationLen):
            self.population[i].setFitness(self.target)
    
    def naturalSelection(self):
        self.matingPool.clear()
        maxFitness = 0.0
        for i in range(self.populationLen):
            if self.population[i].fitness > maxFitness:
                maxFitness =  self.population[i].fitness

        for i in range(self.populationLen):
            fitness = reMap(self.population[i].fitness, 0, maxFitness, 0, 1)
            n = int(fitness * 100)
            for j in range(n):
                self.matingPool.append(self.population[i])
    
    def generate(self):
        for i in range(self.populationLen):
            a = randint(0, len(self.matingPool) - 1)
            b = randint(0, len(self.matingPool) - 1)
            partnerA = self.matingPool[a]
            partnerB = self.matingPool[b]
            child = partnerA.crossover(partnerB)
            child.mutate(self.mutationRate)
            self.population[i] = child
        self.generations += 1
    
    def getBest(self):
        worldRecord = 0
        index = 0
        for i in range(self.populationLen):
            if self.population[i].fitness > worldRecord:
                index = i
                worldRecord = self.population[i].fitness
        if worldRecord == self.perfectScore:
            self.isFinished = True
        print(self.population[index].fitness)
        return self.population[index].getPhrase()
    
    def finished(self):
        return self.isFinished

    def getGenerations(self):
        return self.generations

    def getAverageFitness(self):
        total = 0
        for i in range(self.populationLen):
            total += self.population[i].fitness
        return total / self.populationLen

    def getAllPhrases(self):
        everything = ""
        displayLimit = min(self.populationLen, 50)
        for i in range(displayLimit):
            everything += self.population[i].getPhrase() + "\n"
        return everything

def main():
    target = "Vlad e cel mai bun profesor de Python"
    popmax = 500

    mutationrate = 0.01
    population = Population(target, mutationrate, popmax)
    ok = True
    contor = 1
    while ok == True:
        population.naturalSelection()
        population.generate()
        population.calcFitness()
        answer = population.getBest()
        print(answer)
        print(population.generations)
        if population.isFinished == True:
            ok = False
if __name__ == '__main__': 
    main()
    
