"""
Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
"""

def calc_difference(mod_weight):
    current_weight = int(float(mod_weight) / 3) - 2 # weight of mass
    weight = current_weight # weight of the 
    while(True):
        if int(float(current_weight) / 3) - 2 > 0:
            current_weight = int(float(current_weight) / 3) - 2
            weight += current_weight
        else:
            return weight


if __name__ == "__main__":
    summation = 0
    with open('day1.txt', 'r') as file:
        for line in file:
            summation += calc_difference(line)
    
    print(summation)
