# Consensus and Profile
# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
# Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

# Low level solution. Could look into it getting cleaned up with numpy representations of matrices

# Get data array
import sys
raw = sys.stdin.read().split('>')[1::]
data = []
for string in raw:
	data.append(''.join(string.split('\n')[1::]))

# Initialize profile matrix with 0s
profile = [[0 for j in xrange(len(data[0]))] for i in xrange(4)]

# Set row order to assign profile matrix rows to nucleotides in ACGT order
order = {'A' : 0, 'C' : 1, 'G' : 2, 'T' : 3, 0 : 'A', 1 : 'C', 2 : 'G', 3 : 'T'}


for strand in data:
	index = 0
	for nuc in strand:
		profile[order[nuc]][index] = profile[order[nuc]][index] + 1
		index = index + 1

max = [0 for x in xrange(len(data[0]))]
consensus = ['x' for x in xrange(len(data[0]))]

for column in xrange(len(data[0])):
	rowID = 0
	for row in profile:
		if row[column] > max[column]:
			max[column] = row[column]
			consensus[column] = order[rowID]
		rowID = rowID + 1
consensus = ''.join(consensus)

print consensus
#print str(len(consensus))

output = ''
rowID = 0
for row in profile:
	output = output + order[rowID] + ':'
	for num in row:
		output = output + ' ' + str(num)
	output = output + '\n'
	rowID = rowID + 1
print output
		

			
