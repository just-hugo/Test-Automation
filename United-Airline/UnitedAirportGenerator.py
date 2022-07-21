import random

def airport_generator():
    airports = []

    #open() will open a file and return a corresponding file object . Refer here for information on arguments and parameters: https://www.programiz.com/python-programming/methods/built-in/open

    airportsfile = open(r'airports2.txt')
    for line in airportsfile:
        airports.append(line.split(','))
    #print(airports)

    randomAirport = random.choice(airports)

    return
