#!/usr/bin/env python

from __future__ import annotations
import collections

# read input
with open('./inputs/day05.txt') as filehandle:
	INPUT_S = filehandle.read()

points: collections.Counter[tuple[int, int]] = collections.Counter()

for line in INPUT_S.splitlines():
	start, end = line.split(' -> ')
	x1_s, y1_s = start.split(',')
	x2_s, y2_s = end.split(',')
	x1, y1, x2, y2 = int(x1_s), int(y1_s), int(x2_s), int(y2_s)

	if x1 == x2:
		for y in range(min(y1, y2), max(y1, y2) + 1):
			points[(x1, y)] += 1

	elif y1 == y2:
		for x in range(min(x1, x2,), max(x1, x2) + 1):
			points[(x, y1)] += 1

	else:

		if x1 < x2:
			x_d = 1
		else:
			x_d = -1

		if y1 < y2:
			y_d = 1
		else:
			y_d = -1

		x, y = x1, y1
		while (x, y) != (x2 + x_d, y2 + y_d):
			points[(x, y)] += 1
			x, y = x + x_d, y + y_d


count = 0
for k, v in points.most_common():
	if v > 1:
		count += 1
	else:
		break

print(count)