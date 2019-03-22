#! /home/user/anaconda2/envs/bioinf/bin/python
print("Input your DNA sequence: ")

dna = input()
dna = dna.upper()
GC_percent=((dna.count('C') + dna.count('G'))/len(dna) * 100)
AT_percent=((dna.count('A') + dna.count('T'))/len(dna) * 100)
print("The DNA has a GC percentage of %.3f and AT percentage of %.3f, the length of DNA is %i." \
	%(GC_percent, AT_percent, len(dna)))

## CK: Good, but you need to add comments to your code -1 