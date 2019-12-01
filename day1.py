def part1():
    freq = 0
    with open('day1.txt', 'r') as file:
        for line in file:
            freq += int(line)

    print(freq)

def part2_2():
    round = 1
    freq = 0
    freq_list = [freq]
    while True:
        print(round)
        round += 1

        for line in [1, -1]:
            freq += int(line)
            if freq in freq_list:
                return freq
            else:
                freq_list.append(freq)

def part2():
    round = 1
    freq = 0
    freq_list = [freq]
    while True:
        with open('day1.txt', 'r') as file:
            for line in file:
                print(len(freq_list))
                freq += int(line)
                if freq in freq_list:
                    return freq
                else:
                    freq_list.append(freq)

    
if __name__ == "__main__":
    print(part2())
    