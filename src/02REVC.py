# Complementing a strand of DNA

# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
# The reverse complement of a DNA string s  is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
# Given: A DNA string s  of length at most 1000 bp.
# Return: The reverse complement sc   of s .



import sys

# Get input string from stdin
s = sys.stdin.readline().strip('\n')

# Reverse input string
r = s[::-1]

# Replace with complements
sc = r.replace('G','X').replace('C','G').replace('X','C').replace('A','X').replace('T','A').replace('X','T')

print sc
