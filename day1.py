import csv

with open('input.csv', mode='r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	print(csv_reader)

	temp = []
	# part 1
	for row in csv_reader:
		temp.append(int(row[0]))
	count = 0
	for i in range(0,len(temp)-1):
		if(temp[i+1]-temp[i]>0):
			count +=1
	print("Part 1:", count)


	# part 2
	temp2 = []
	for i in range(0,len(temp)-2):
		trisum = 0
		for j in range(0,3):
			trisum += temp[i+j]
		temp2.append(trisum)
	count2 = 0
	for i in range(0,len(temp2)-1):
		if(temp2[i+1]-temp2[i]>0):
			count2 +=1
	print("Part 2:", count2)