# Used codepad for this one, ideone having uptime issues. 

# initialize data
raw = '93 16'
raw = raw.split(' ')
months = int(raw[0])
lifeSpan = int(raw[1])
babies = [1]
mature = [0]

# calculate recurrence relation
for month in xrange(1,months):
  babies.append(mature[month-1])
  mature.append(babies[month-1] + mature[month-1])
  if month >= lifeSpan:
    mature[month] = mature[month] - babies[month-lifeSpan]

# print total rabbits
print str(babies[months-1] + mature[months-1])
