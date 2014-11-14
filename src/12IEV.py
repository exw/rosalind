# Calculating Expected Offspring

# get data

import sys
raw = sys.stdin.read().split(' ')
data = map(float,raw)

# calculate based on ev for couples

ev = data[0]*2 + data[1]*2 + data[2]*2 + data[3]*1.5 + data[4]*1 + data[5]*0

# display answer

print str(ev)
