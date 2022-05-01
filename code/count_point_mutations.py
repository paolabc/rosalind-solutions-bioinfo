#!/usr/bin/python3
"""
Rosalind solve problem: Counting Point Mutations
url: https://rosalind.info/problems/hamm/

"""

import sys


#"The Hamming distance between two strings having the same length is the minimum number of symbol substitutions required to transform one string into the other. If the strings are given by s1 and s2, then we write the Hamming distance between them as dH(s1,s2)."


#arg input
s = sys.argv[1]
t = sys.argv[2]
dna_check={"A","C","G","T"}
def hamming_distance(s,t):

  if len(s)!= len(t):
      print('The sequences have no equal size.')
      
  elif set(s.upper()).issubset("ACGT") and set(t.upper()).issubset("ACGT"):
      Hdistance=0
      for i in range(0,len(s)):
          if s[i] != t[i]:
            Hdistance+=1
      return Hdistance
  else:
       print('Try again, there are characters that do not correpond to DNA sequence.')
if hamming_distance(s,t) != None:
   print('Hamming distance is:',hamming_distance(s,t))


