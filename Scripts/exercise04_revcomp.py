#! /home/user/anaconda2/envs/bioinf/bin/python

#create s string of DNA
print("""Input the DNA sequence which you want to 
find the reverse compliment: """)
a = str(input())
a = a.upper()
print("""This is the DNA of interest 
%s""" %a)
#create a dictionary 
comp = dict({'A':'T','T':'A', 'C':'G', 'G':'C'})
#convert the sequence into a list
b = list(a)
#invert the strand in reverse order
b.reverse()
#join the sequence
rev = "".join(b)
#create a list of the reverse strand
revl = list(rev)
#creating a reverse complement
rev_comp = [comp[b] for b in revl]
#join the list to a str
rev_comp2 = "".join(rev_comp)
print("""This is the reverse compliment of the above DNA sequence 
%s""" %rev_comp2)
