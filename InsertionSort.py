#Purpose: perform insertion sort
#Inputs: User inserts a string of space separated integers.
#Outpus: A sorted string of space separated integers.

input = raw_input("Insert space separated string of integers for sorting: ")

print "Your input: " + input

input_split = input.split(" ")

print input_split

#Idea:
#Begin with second value.
#Compare to the first value.
#If smaller, move to next one
#If larger replace
#Continue as long as not at first position.

#Second value
j = 1
while (j < len(input_split)):
	current_value = input_split[j]
	i = j
	while (i > 0):
		if (int(input_split[i]) < int(input_split[i-1])):
			hold_value = input_split[i-1]
			input_split[i-1] = current_value
			input_split[i] = hold_value
		i -= 1
	j += 1

#print out sorted list.
print 'Sorted: ', input_split




