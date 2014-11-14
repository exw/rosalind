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
		elif source.endswith(target[0:3]):
			answer.append([titles[sourceIndex],titles[targetIndex]])
		targetIndex = targetIndex + 1
	sourceIndex = sourceIndex + 1

# Check for duplicates
for pair in answer:
	for checked in answer:
		if pair[0] == checked[1] and pair[1] == checked[0]:
			answer.remove(pair)
			
formatted = []
# Format answer
for found in answer:
	formatted.append(found[0] + ' ' + found[1])
for ans in formatted:
	print ans
