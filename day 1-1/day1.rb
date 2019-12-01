def hand_off(num)
    # does the claculation step by step for debugging pruposes
    number = num.to_f / 3 # forces float (regardless of current type)
    number = number.floor # floors the number
    number -= 2 # subtracts 2
end

def calc_difference(weight)
    current_weight = hand_off(weight) # get the first weight
    weight = current_weight # set the max weight

    while true # loop runs until returns
        if hand_off(current_weight) > 0 # check if it is viable
            current_weight = hand_off(current_weight) # recalculte current weight
            weight += current_weight # recalculate weight
        else
            return weight # if there is no more calcualtions return weight
        end
        
    end
end

if __FILE__ == $0 # checks if this is the executing file
    sum = 0

    # opens file and splices it into an array
    file_data = File.open("day1.txt").readlines.map(&:chomp)


    file_data = file_data.map {|val| val.to_f} # forces values to be floats

    for i in file_data do # loops through all values calcuating difference
        sum += calc_difference(i)
    end

    puts sum