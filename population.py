## This program calculates the projected population of a country
## based on current population, birth rate, death rate, and             


def count_population(year):
  current_population = 307357870
  birth_rate = 7
  death_rate = 13
  new_immigrant = 35
  year_to_seconds = year * 365 * 24 * 60 * 60
  births = (year_to_seconds/birth_rate) 
  death = (year_to_seconds/death_rate)
  new_immigrant_rate = (year_to_seconds/new_immigrant)
  total_population = current_population + births - death + new_immigrant_rate
  return total_population   

def main():
    year = int(input("Enter the number of years to project the population: "))
    total_population = count_population(year)
    print(f"The projected population after {year} years is: {total_population:.0f}")


if __name__ == "__main__":
    main()
 