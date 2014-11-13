import sys

# Get input parameters
text = sys.stdin.readlines()
s = text[0].strip('\n')
t = text[1]

# Initialize output string
output = ''

# Scan for substring by checking each slice of length of substring 
i = 0
while i < len(s) - len(t):
	if s[i:i+len(t)] == t:
		output = output + str(i+1) + ' '
	i = i + 1

output = output[0:len(s)-1]
print output
