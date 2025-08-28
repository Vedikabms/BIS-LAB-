import random

POP_SIZE = 20
GENE_LENGTH = 10  # Number of bits per individual
MAX_GENERATIONS = 5
MUTATION_RATE = 0.05
CROSSOVER_RATE = 0.7

def fitness_function(x):
    return x**2

def initialize_population():
    population = []
    for _ in range(POP_SIZE):
        individual = [random.choice(['0', '1']) for _ in range(GENE_LENGTH)]
        population.append(individual)
    return population

def gene_expression(individual):
    bitstring = ''.join(individual)
    return int(bitstring, 2)

def evaluate_population(population):
    fitnesses = []
    for individual in population:
        x = gene_expression(individual)
        fitnesses.append(fitness_function(x))
    return fitnesses

def select(population, fitnesses):
    total_fit = sum(fitnesses)
    if total_fit == 0:
        return random.choice(population)
    pick = random.uniform(0, total_fit)
    current = 0
    for individual, fit in zip(population, fitnesses):
        current += fit
        if current >= pick:
            return individual
    return population[-1]

def crossover(parent1, parent2):
    if random.random() > CROSSOVER_RATE:
        return parent1[:]
    point = random.randint(1, GENE_LENGTH - 1)
    child = parent1[:point] + parent2[point:]
    return child

def mutate(individual):
    mutated = individual[:]
    for i in range(GENE_LENGTH):
        if random.random() < MUTATION_RATE:
            mutated[i] = '1' if mutated[i] == '0' else '0'
    return mutated

def gene_expression_algorithm():
    population = initialize_population()
    best_solution = None
    best_fitness = float('-inf')

    for generation in range(1, MAX_GENERATIONS + 1):
        fitnesses = evaluate_population(population)

        for individual, fit in zip(population, fitnesses):
            if fit > best_fitness:
                best_fitness = fit
                best_solution = individual[:]

        new_population = []
        while len(new_population) < POP_SIZE:
            parent1 = select(population, fitnesses)
            parent2 = select(population, fitnesses)
            offspring = crossover(parent1, parent2)
            offspring = mutate(offspring)
            new_population.append(offspring)

        population = new_population
        expressed = gene_expression(best_solution)
        print(f"Generation {generation}: Best x = {expressed}, Fitness = {best_fitness}")

    print("\nFinal Best Solution:")
    print(f"Genotype (binary): {''.join(best_solution)}")
    print(f"Expressed Solution (x): {gene_expression(best_solution)}")
    print(f"Best Fitness (x^2): {best_fitness}")

if __name__ == "__main__":
    gene_expression_algorithm()
