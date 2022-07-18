# FUNCIÓN 1. de creación de una población con alelos al azar

import scipy # for random numbers

def build_population(N, p):
    """Se va a construir una poblacion mediante el par ordenado (N, p), donde N representa l numero de individuos de la población y p es el numero ramdom asignado que será representado con la letra a.
    """
    population = []
    for i in range(N):
        allele1 = "A"
        if scipy.random.rand() > p:
            allele1 = "a"
        allele2 = "A"
        if scipy.random.rand() > p:
            allele2 = "a"
        population.append((allele1, allele2))
    return population


    
# FUNCIÓN 2. Conteo de pares de alelos
def compute_frequencies(population):
    """ Cuenta los genotipos de la población ya creada y Devuelve un diccionario de frecuencias genotípicas."""
    AA = population.count(("A", "A"))
    Aa = population.count(("A", "a"))
    aA = population.count(("a", "A"))
    aa = population.count(("a", "a"))
    return({"AA": AA, "aa": aa, "Aa": Aa, "aA": aA}) 



# FUNCIÓN 3. Creación de la población      
def reproduce_population(population):
    """ Crear una nueva generación mediante la reproducción. Para cada uno de los N nuevos descendientes:
    - elige a los padres al azar, 
    - la descendencia recibe un cromosoma de cada uno de los padres.
    """
    new_generation = []
    N = len(population)
    for i in range(N):
        # random integer between 0 and N-1
        dad = scipy.random.randint(N)
        mom = scipy.random.randint(N)
        # which chromosome comes from mom
        chr_mom = scipy.random.randint(2)
        offspring = (population[mom][chr_mom], population[dad][1 - chr_mom])
        #if offspring == ("a", "a"): 
          #next()
        new_generation.append(offspring)
    return new_generation
