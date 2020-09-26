square = float(input("Input a number squared: "))

def isNegative(number):
    combinedVal = number + abs(number)
    return combinedVal == 0

def root(square):
    rootGuess = square / 2
    prevGuess = rootGuess - 1
    size = str(square).index(".") - 1
    if size > 2:
        precision = (size - 1) * -1
    else:
        precision = 0
    while rootGuess**2 != square:
       if isNegative(rootGuess**2 - square):
           prevGuess = rootGuess
           if rootGuess - 1 == prevGuess:
               rootGuess = rootGuess - (9 * 1 / (10**(precision - 1)))
               precision = precision + 1
           else:
               rootGuess = rootGuess - 1 / (10**precision)
           continue
       elif not isNegative(rootGuess**2 - square):
           prevGuess = rootGuess
           rootGuess = rootGuess + 1
           continue
print(root(square))
