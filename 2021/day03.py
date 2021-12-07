#!/usr/bin/env python

import collections

bits = []

# read input
with open('./inputs/day03.txt') as filehandle:
	for item in filehandle:
		bits.append(list(item.strip()))

# Part one
target_count = len(bits[0])
count = 0
gamma_bin_str = ""

while count < target_count:
	current_position_values = []
	for item in bits:
		current_position_values.append(item[count])
	gamma_bin_str += max(current_position_values, key=current_position_values.count)
	count += 1

epsilon_bin_str = ''.join('1' if x == '0' else '0' for x in gamma_bin_str)
result = int(gamma_bin_str, 2) * int(epsilon_bin_str, 2)

print(f"Part one solution: {result}")

# Part two
def count_bits(candidates, mode):
	position = 0

	while len(candidates) > 1:
		current_position_values = []

		for item in candidates:
			current_position_values.append(item[position])

		current_counter = collections.Counter(current_position_values).most_common()
	
		match mode:
			case 'oxygen':
				if current_counter[0][1] == current_counter[-1][1]:
					current_bit = '1'
				else:
					current_bit = current_counter[0][0]
			case 'co2':
				if current_counter[0][1] == current_counter[-1][1]:
					current_bit = '0'
				else:
					current_bit = current_counter[-1][0]

		temp_candidates = []
		for item in candidates:
			if item[position] == current_bit:
				temp_candidates.append(item)

		candidates = temp_candidates
		position += 1

	return int(''.join(candidates[-1]), 2) 


oxygen_generator_rating = count_bits(bits, 'oxygen')
co2_scrubber_rating = count_bits(bits, 'co2')

print(f"Part two solution: {oxygen_generator_rating * co2_scrubber_rating}")