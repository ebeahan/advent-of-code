#!/usr/bin/env python

measurements = []

# read input
with open('./inputs/day02.txt') as filehandle:
	for item in filehandle:
		measurements.append(item.strip())

position = {
	'horizontal': 0,
	'depth': 0
}

# part one
for item in measurements:
	direction, value = item.split()
	value = int(value)
	match direction:
		case 'forward':
			position['horizontal'] += value
		case 'up':
			position['depth'] -= value
		case 'down':
			position['depth'] += value	

print(f"Part one solution: {position['horizontal'] * position['depth']}")

# part two
position = {
	'horizontal': 0,
	'aim': 0,
	'depth': 0
}

for item in measurements:
	direction, value = item.split()
	value = int(value)
	match direction:
		case 'forward':
			position['horizontal'] += value
			if position['aim'] != 0:
				position['depth'] += value * position['aim']
		case 'up':
			position['aim'] -= value
		case 'down':
			position['aim'] += value

print(f"Part two solution: {position['horizontal'] * position['depth']}")
