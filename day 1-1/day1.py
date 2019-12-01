"""
Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
"""

def calc_difference(mod_weight):
    current_weight = int(float(mod_weight) / 3) - 2 # weight of mass
    weight = current_weight # weight of current mod
    while(True): # runs until return
        if int(float(current_weight) / 3) - 2 > 0: # checks to see if it can move down another rung
            current_weight = int(float(current_weight) / 3) - 2 # moves down that rung
            weight += current_weight # adds that back to weight
        else: 
            return weight # if there is no more calc to do return the value


if __name__ == "__main__":
    summation = 0 # the sum 
    with open('day1.txt', 'r') as file: # opens the file
        for line in file: # reads all lines
            summation += calc_difference(line) # calcs 
    
    print(summation) # outputs
