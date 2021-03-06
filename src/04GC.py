# Computing GC content

# Get array of data strings splitting by > and discarding empty first item
import sys
text = sys.stdin.read()
data = text.split('>')[1::]

# initialize answer comparisons
d = dict()
max = 0

# Perform calculations on each item
for item in data:

  # For each item, initialize variables to hold title until first newline reached 
	readTitle = True
	tempTitle = ''
	
	# For each item, initialize variables to calculate gcContent
	dataLen = 0
	gcCount = 0
	
	# Read the strings
	for char in item:
	  # If in title section of string
		if readTitle:
		  # Check for newline to indicate data starting, otherwise append character to title variable
			if char == '\n':
				readTitle = False
			else:
				tempTitle = tempTitle + char
	  # If in data section of string
		else:
		  # Don't count random newline characters towards data length 
			if char != '\n':
			  # Increment data length for any non-newline, increment gcCount for G or C
				dataLen = dataLen + 1
				if char == 'G' or char == 'C':
					gcCount = gcCount + 1
					
	# At the end of the item, perform GC content calculations
	d[tempTitle] = gcCount/float(dataLen)
	
	# Optional test commented out
  #	print "Set " + tempTitle + ": " + str(d[tempTitle])
	
	# Check if item is highest GC content, store in answer format
	if d[tempTitle] > max:
		max = d[tempTitle]
		ans = [tempTitle,str(100*max)]
		
# Print answer
print ans[0]
print ans[1]
			
