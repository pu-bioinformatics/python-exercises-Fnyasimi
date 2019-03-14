#! /home/user/anaconda2/envs/bioinf/bin/python


def dnafunction(seq):
    """This fuction determines if a sequence is made up of valid DNA bases"""
    seq = seq.upper()
    qc = True
    bases = 'ATGC'

    for b in seq:
        if b in bases:
            pass
        else:
            qc = False
            print("%s is an invalid base" %b)
    return print("The quality check is complete and your sequence is a %s DNA." %qc)


