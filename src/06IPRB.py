# Mendel's First Law

# Get data
import sys
text = sys.stdin.read()
data = text.split(' ')
print data

k = float(data[0])
m = float(data[1])
n = float(data[2])

# choice 1 count
t = k + m + n
# choice 2 count
u = t-1

dominantPhenotype = k/t + (m/t)*(k/u) + .75*(m/t)*((m-1)/u) + .5*(m/t)*(n/u) + (n/t)*(k/u) + .5*(m/t)*(n/u)

print dominantPhenotype
