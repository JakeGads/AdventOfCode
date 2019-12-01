
shift = 0
shift_array = []
File.open(__dir__ + "/day1.txt").each do |line|
  shift = shift + line.to_i
  shift_array.push(line.to_i)
puts shift



pulse = 0
pulse_array = [pulse]
tester = true

count = 0

while tester
  for i in shift_array
    count += 1
    pulse += i
    
    if pulse_array.include? pulse
      # puts pulse
      tester = false
      break

    else
      pulse_array.push(pulse.to_i)
      puts pulse.to_i
    end
  
  end

end

# puts pulse
# puts shift

