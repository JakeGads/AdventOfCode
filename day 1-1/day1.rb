def hand_off(num)
    number = num.to_f / 3
    number = number.floor
    number -= 2
end

def calc_difference(weight)
    current_weight = hand_off(weight)
    weight = current_weight

    is_not_zero = true

    while is_not_zero
        if hand_off(current_weight) > 0
            current_weight = hand_off(current_weight)
            weight += current_weight       
        else
            return weight
        end
        
    end
end

sum = 0

file_data = File.open("day1.txt").readlines.map(&:chomp)

file_data = file_data.map {|val| val.to_f}

for i in file_data do
    sum += calc_difference(i)
end

puts sum