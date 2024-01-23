import math,random,sys

MUTATION_BARRIER = 30
MAX_GENERATIONS = 1000

def solve(points):
    n = len(points)
    #I will create n arrays of solutions
    initial_population = [randSol(points,n) for i in range(n)]
    #initial_population = [randSol(points,n) for i in range(min(math.log(n,2),2))]
    return evolution(initial_population)

def evolution(population):
    n = len(population)
    for gen_iter in range(0,MAX_GENERATIONS):
        #sort the population by fitness
        graded_population = sorted(population,key=fitness)
        #will take only the top 66% candidates for mating 
        viable_candidates = graded_population[0:2*n//3]
        next_generation = []
        for i in range(1,n//2,2):
            cross_point = random.randint(0,n-1)
            parent1 = viable_candidates[i-1]
            child = parent1[0:cross_point]
            parent2 = viable_candidates[i]
            remaining_parent2 = [p for p in parent2 if p not in child]
            child += remaining_parent2
            #check if mutated
            dice_roll = random.randint(1,100)
            if dice_roll <= MUTATION_BARRIER:
                #If a mutation occured, pick a random index,
                #and replace it with n-1-index
                mutatedIndex = random.randint(0,n-1)
                #cooler way to perform swap
                child[mutatedIndex],child[n-1-mutatedIndex] = child[n-1-mutatedIndex],child[mutatedIndex]
            next_generation.append(child)
        #since the crossings produces 0.33n children, I take the top 67% of the original generation
        #to the next one, discarding only the 33% worst original candidates
        population = viable_candidates + next_generation
    return sorted(population,key = fitness)[0]

def dist(p1,p2):
    return float(math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2))

def fitness(points):
    sum=0
    for i in range(1,len(points)):
        sum+=dist(points[i-1],points[i])
    return sum


def randSol(points,size):
    mn=sys.maxsize
    for i in range(size):
        ps = points.copy()
        random.shuffle(ps)
        f = fitness(ps)
        if f<mn:
            mn=f
            best=ps
    return best