# Really should just use a built-in reader from the python Bio library
# In the meantime, this convoluted code gets the data from raw input

import sys
raw = sys.stdin.read().split('>')[1::]
titles = []
data = []

for string in raw:
	readTitle = True
	tempTitle = ''
	tempData = ''
	for char in string:
		if readTitle:
			if char == '\n':
				readTitle = False
				titles.append(tempTitle)
			else:
				tempTitle = tempTitle + char
		else:
			if char == '\n':
				pass
			else: 
				tempData = tempData + char
	data.append(tempData)

answer = []
test = []

# Compare reverse of target string with other strings for length k=3 as indicated
sourceIndex = 0
for source in data:
	targetIndex = 0
	for target in data:
		if data[targetIndex] == data[sourceIndex]:
			pass
		elif source[-1:-4:-1] == target[0:3]:
			answer.append(titles[sourceIndex] + ' ' + titles[targetIndex])
			test.append("next pair: " + data[sourceIndex] + '\n' + data[targetIndex])
		targetIndex = targetIndex + 1
	sourceIndex = sourceIndex + 1


# Format answer
for found in answer:
	print found
