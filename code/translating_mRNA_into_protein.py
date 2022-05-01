#!/usr/bin/python3
"""
Rosalind solve problem: The Genetic Code
url: https://rosalind.info/problems/prot/
"""
import sys

def translate_mRNA_seq(seq):
    codon_dict = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
           "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
           "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
           "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
           "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
           "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
           "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
           "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
           "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
           "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
           "UAA": "stop", "CAA": "Q", "AAA": "K", "GAA": "E",
           "UAG": "stop", "CAG": "Q", "AAG": "K", "GAG": "E",
           "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
           "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
           "UGA": "stop", "CGA": "R", "AGA": "R", "GGA": "G",
           "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"}
    aa=[]
    for i in range(0,len(seq),3):
        aa.append(codon_dict[seq[i:i+3]])
    return ''.join(aa)



if __name__ == "__main__":
    path=sys.argv[1]
    with open(path, 'r') as f:
        mRNA_seq_sample = f.readline().strip()
    print(translate_mRNA_seq(mRNA_seq_sample))


