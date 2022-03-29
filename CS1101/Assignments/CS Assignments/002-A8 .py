#!/usr/bin/env python
# coding: utf-8

# # CS1101 Assignment - 08

# ## Question 1:

# An RNA sequence is formed by the nucleotides ’A’, ’C’, ’G’, and ’U’. A triplet of nucleotides in such a sequence is called a codon and a protein coding gene is characterized by a start codon and a stop codon. Write a program that takes an RNA string as input and prints the codons present in the sequence. For example, for the sequence given below
# 
# Input: AUGGGAACUUCACUACGUAAAUAG
# 
# Output: Codons are: AUG, GGA, ACU, UCA, CUA, CGU, AAA, UAG
# 
# Determine the frequency $\frac{No.\ of\ times\ a\ codon\ appears}{Total\ no.\ of\ codons\ in\ the\ sequence}$ of each of the 64 codons in the input sequence.

# In[19]:


rna = input('Enter an RNA sequence: ')
rna_list = []
while (len(rna) % 3 != 0):
    rna = rna[:len(rna) - 1]
for i in range(0, len(rna), 3):
    rna_list.append(rna[i:i + 3])
print('Codons are: ', rna_list)
rna_freq = [rna_list.count(codon) for codon in rna_list]
rna_freq = [str(rna_freq[i]) + '/' + str(len(rna_list)) for i in range (0, len(rna_freq))]
x = dict(zip(rna_list, rna_freq))
print('Frequency of each Codon: ',x)


# ## Question 2:

# Given a genetic code (see image below), i.e., a mapping between codons and amino acids, a coding sequence like the RNA sequence given above can be translated into an amino acid sequence. Using a dictionary like the one specified in slide 76 of the updated lecture slides, convert a protein coding mRNA sequence input by the user into an amino acid sequence.
# 
# <img src='Stop Codon.png' width="700" height="700">
# 
# Note that the last codon in an mRNA sequence is either UAA or UAG or UGA which are stop codons that are not translated into an amino acid. As in the above example, when such a codon is encountered, translation should be terminated. 
# 
# You can use the following 1-letter code for amino acids to specify the values associated with the keys (which are codons) in your dictionary.
# 
# <img src='Code.png' width="200" height="300">
# 
# Input mRNA sequence: AUGGGAACUUCACUACGUAAAUAG
# 
# Output: MGTSLRK 
# 
# (where M,G,…..,K are amino acids associated with codons AUG, GGA,…,AAA)

# In[47]:


def amino_acids (mRNA):
    protein = ''
    RNA_codon_table = {
    # U
    'UUU': 'Phe', 'UCU': 'Ser', 'UAU': 'Tyr', 'UGU': 'Cys', # UxU
    'UUC': 'Phe', 'UCC': 'Ser', 'UAC': 'Tyr', 'UGC': 'Cys', # UxC
    'UUA': 'Leu', 'UCA': 'Ser', 'UAA': '---', 'UGA': '---', # UxA
    'UUG': 'Leu', 'UCG': 'Ser', 'UAG': '---', 'UGG': 'Trp', # UxG

    # C
    'CUU': 'Leu', 'CCU': 'Pro', 'CAU': 'His', 'CGU': 'Arg', # CxU
    'CUC': 'Leu', 'CCC': 'Pro', 'CAC': 'His', 'CGC': 'Arg', # CxC
    'CUA': 'Leu', 'CCA': 'Pro', 'CAA': 'Gln', 'CGA': 'Arg', # CxA
    'CUG': 'Leu', 'CCG': 'Pro', 'CAG': 'Gln', 'CGG': 'Arg', # CxG

    # A
    'AUU': 'Ile', 'ACU': 'Thr', 'AAU': 'Asn', 'AGU': 'Ser', # AxU
    'AUC': 'Ile', 'ACC': 'Thr', 'AAC': 'Asn', 'AGC': 'Ser', # AxC
    'AUA': 'Ile', 'ACA': 'Thr', 'AAA': 'Lys', 'AGA': 'Arg', # AxA
    'AUG': 'Met', 'ACG': 'Thr', 'AAG': 'Lys', 'AGG': 'Arg', # AxG

    # G
    'GUU': 'Val', 'GCU': 'Ala', 'GAU': 'Asp', 'GGU': 'Gly', # GxU
    'GUC': 'Val', 'GCC': 'Ala', 'GAC': 'Asp', 'GGC': 'Gly', # GxC
    'GUA': 'Val', 'GCA': 'Ala', 'GAA': 'Glu', 'GGA': 'Gly', # GxA
    'GUG': 'Val', 'GCG': 'Ala', 'GAG': 'Glu', 'GGG': 'Gly'  # GxG
    }


    singleletter = {'Cys': 'C', 'Asp': 'D', 'Ser': 'S', 'Gln': 'Q', 'Lys': 'K',
    'Trp': 'W', 'Asn': 'N', 'Pro': 'P', 'Thr': 'T', 'Phe': 'F', 'Ala': 'A',
    'Gly': 'G', 'Ile': 'I', 'Leu': 'L', 'His': 'H', 'Arg': 'R', 'Met': 'M',
    'Val': 'V', 'Glu': 'E', 'Tyr': 'Y', '---': '*'}

    stop_codons = {"UGA","UAG","UAA"}
    
    while mRNA:
        codon = mRNA[:3]  
        mRNA = mRNA[3:]  
        if codon in stop_codons:
            continue
        amino_acid = singleletter[RNA_codon_table[codon]]
        protein = protein + amino_acid
    return protein
mrna = input('Enter mRNA sequence: ')
print('Amino Acid Sequence: ',amino_acids(mrna))


# ## Question 3:
# 
# Write a program in python to input the radius of a sphere, and print the volume using 
# formatted output corrected to 1, 2, 3 and 4 decimal places.

# In[38]:


r = float(input('Enter radius: '))  
   
volume = (4 * 22 * (r ** 3))/(3 * 7) 

print("The volume is:", format(volume,".1f"), ",", format(volume, ".2f"), ",", format(volume, ".3f"), ",", format(volume, ".4f"))   


# ## Question 4:
# 
# Use try, except to check if an inputted number is non-negative or not and for the former 
# print the sqrt in a format with 3 places after decimal; for the negative case print an 
# appropriate message in the except block.

# In[1]:


import math
x = int(input("Enter a number: "))
try:
    print(format(math.sqrt(x), ".3f"))
except:
    print("Negative Number encountered")


# In[ ]:




