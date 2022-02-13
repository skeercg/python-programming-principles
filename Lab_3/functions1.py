def toOunces(grams):
    return grams * 28.3495231

def toCelsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

def solve(heads, legs):
    for rabbits in range(heads):
        if (rabbits * 4 + (heads - rabbits) * 2 == legs):
            return (rabbits, heads - rabbits)
        
def filterPrimes(numbers):
    filteredNumbers = []
    for i in range(len(numbers)):
        isPrime = True
        if (numbers[i] == 1):
            isPrime = False
        for d in range(2, numbers[i]):
            if (numbers[i] % d == 0):
                isPrime = False
        if (isPrime):
            filteredNumbers.append(numbers[i])
    return filteredNumbers

def findAllPermutations(string):
    pass
