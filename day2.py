data = open('data.txt', 'r').read().split("\n")

depth = 0
horizontal = 0

for command in data:
	if command[0] == 'u':
		depth -= int(command[-1])
	if command[0] == 'd':
		depth += int(command[-1])
	if command[0] == 'f':
		horizontal += int(command[-1])

print('Part 1:', depth*horizontal)

depth = 0
horizontal = 0
aim = 0

for command in data:
	if command[0] == 'u':
		aim -= int(command[-1])
	if command[0] == 'd':
		aim += int(command[-1])
	if command[0] == 'f':
		horizontal += int(command[-1])
		depth += aim * int(command[-1])

print('Part 2:', depth*horizontal)