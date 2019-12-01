def part1():
    freq = 0 # start with an empty freq
    with open('day1.txt', 'r') as file:
        for line in file:
            freq += int(line) # for every line add it back to the orginal value

    return freq 

def part2_2():
    freq = 0 # start my freq at 0
    freq_list = [freq] # append it to the master list
    while True: # allows for the recursive nature of the problem
        for line in [1, -1]: # the line in the list (nomicalture is just to match as the below part2 functions)
            freq += int(line) # casts to int and adds it
            if freq in freq_list: # checks if it exists in the list
                return freq
            else:
                freq_list.append(freq) # returns if needed

def part2():
    freq = 0 # starts my freq at 0
    freq_list = [freq] # append it to the master list
    while True: # allows for the recursive nature
        with open('day1.txt', 'r') as file: # opens up my files (reopens when needed)
            for line in file: # reads each line
                freq += int(line) # adds to freq
                if freq in freq_list: # checks if its present
                    return freq
                else:
                    freq_list.append(freq) # appends if if doesn't reloops (the entire file if needed)

def part2_r():
    shifts = []
    with open('day1.txt', 'r') as file:
        for line in file:
            shifts.append(int(line))
    
    current_freq = 0
    all_freqs = []

    while True:
        for i in shifts:
            current_freq += i
            if current_freq in all_freqs:
                return current_freq
            else:
                all_freqs.append(current_freq)

if __name__ == "__main__":
    print(f"Part 1: {part1()}") # print statments
    print(f"Part 2: {part2_r()}")