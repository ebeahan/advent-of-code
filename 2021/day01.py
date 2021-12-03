#!/usr/bin/env python

measurements = []

# read input
with open('./inputs/day01.txt') as filehandle:
	for item in filehandle:
		measurements.append(int(item.strip()))

# compare index to index-1 and track when index is larger
def compare_measurements(measurements):
	count = 0
	result = 0

	while count < len(measurements):
		if measurements[count - 1] < measurements[count]:
			result += 1
		count += 1	
	
	return result

# Part one
part_one_result = compare_measurements(measurements)

# Part two
three_measurement_windows = []
index = 0

while index < (len(measurements) - 2):
	three_measurement_windows.append(sum(measurements[index:index+3]))
	index += 1

part_two_result = compare_measurements(three_measurement_windows)

# Print results
print(f'Part one: {part_one_result}')
print(f'Part two: {part_two_result}')