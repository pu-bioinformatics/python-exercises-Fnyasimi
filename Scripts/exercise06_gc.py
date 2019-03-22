#! /home/user/anaconda2/envs/bioinf/bin/python

def gcfunction(dna):
    """This function is used to calculate the GC and AT percentage content of a DNA sequence"""
    dna = dna.upper()
    GC_p = ((dna.count('C') + dna.count('G'))/len(dna) * 100)
    AT_p = ((dna.count('A') + dna.count('T'))/len(dna) * 100)
    return print("The DNA has a GC percentage of %.3f and AT percentage of %.3f, the length of DNA is %i." \
                    %(GC_p, AT_p, len(dna)))

#CK: This function and the one in exercise06_dna should be combined. 
# gcfunction should call the dnafunction to check for validity before calculating GC content -2 
# Also, you need to call the function -1