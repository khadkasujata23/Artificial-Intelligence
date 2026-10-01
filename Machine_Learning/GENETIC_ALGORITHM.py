# Genetic Algorithm

import random


# Fitness function
# We want to maximize x^2
def fitness(chromosome):
    x = int(chromosome, 2)
    return x * x


# Initial population
population = [
    '00101',
    '01010',
    '01111',
    '10001',
    '10100',
    '11000'
]


# Number of generations
generations = 10


for generation in range(generations):

    # Sort population according to fitness
    population.sort(key=fitness, reverse=True)

    # Select the best two chromosomes
    parent1 = population[0]
    parent2 = population[1]

    # Crossover
    point = 3

    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]

    # Mutation
    child1 = list(child1)
    child2 = list(child2)

    mutation_point = random.randint(0, 4)

    child1[mutation_point] = str(
        1 - int(child1[mutation_point])
    )

    child2[mutation_point] = str(
        1 - int(child2[mutation_point])
    )

    child1 = ''.join(child1)
    child2 = ''.join(child2)

    # Create new population
    population = [
        parent1,
        parent2,
        child1,
        child2,
        '11110',
        '11111'
    ]


# Find best chromosome
best = max(population, key=fitness)

print("Best Chromosome:", best)
print("Value of x:", int(best, 2))
print("Fitness:", fitness(best))