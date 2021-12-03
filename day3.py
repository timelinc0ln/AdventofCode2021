from collections import Counter

data = open('data.txt', 'r').read().split("\n")

gamma = ''
for j in range(0,12):
	count = 0
	for i in range(0,len(data)):
		count += int(data[i][j])
	if count > len(data)/2:
		gamma += '1'
	else:
		gamma += '0'

epsilon = ''
for character in gamma:
	if character == '1':
		epsilon += '0'
	else:
		epsilon += '1'

print("Gamma:", gamma)
print("Epsilon:", epsilon)

print("Gamma * Eplison", int(epsilon,2)*int(gamma,2))

ogen = data[:]
scrub = data[:]

for i in range(len(data[0])):
	ogencount = Counter([n[i] for n in ogen])
	scrubcount = Counter([n[i] for n in scrub])

	if len(ogen) > 1:
		if ogencount['0'] > ogencount['1']:
			ogen = [n for n in ogen if n[i] == '0']
		else:
			ogen = [n for n in ogen if n[i] == '1']

	if len(scrub) > 1:
		if scrubcount['0'] > scrubcount['1']:
			scrub = [n for n in scrub if n[i] == '1']
		else:
			scrub = [n for n in scrub if n[i] == '0']

print(int(ogen[0],2))
print(int(scrub[0],2))
print(int(ogen[0],2)*int(scrub[0],2))
