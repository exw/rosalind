# Computing GC content

# Get data
import sys
text = sys.stdin.read()
data = text.split('\n')[:2:]
first = data[0]
second = data[1]
index = 0
hamming = 0

# Compare strings

for char in first:
	if first[index] != second[index]:
		hamming = hamming + 1
	index = index + 1

# Print answer
print hamming
