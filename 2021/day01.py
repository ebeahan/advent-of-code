#!/usr/bin/env python

measurements = []

with open('./inputs/day01.txt') as filehandle:
	for item in filehandle:
		measurements.append(int(item.strip()))

count = 0
result = 0

while count < len(measurements):
	if measurements[count - 1] < measurements[count]:
		result += 1
	count += 1

print(result)