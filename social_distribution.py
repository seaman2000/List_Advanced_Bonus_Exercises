population = list(map(int, input().split(", ")))
min_wealth = int(input())


if sum(population) < min_wealth * len(population):
    print("No equal distribution possible")
else:
    for i in range(len(population)):
        if population[i] < min_wealth:
            need = min_wealth - population[i]

            while need > 0:
                richest_idx = population.index(max(population))
                available = population[richest_idx] - min_wealth

                if available <= 0:
                    break

                give = min(need, available)
                population[richest_idx] -= give
                population[i] += give
                need -= give

    print(population)

