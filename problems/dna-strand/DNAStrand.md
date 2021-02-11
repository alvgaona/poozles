# DNA Strand

DNA molecules are made of two twisting, paired strands. Each strand is made of four chemical units, called nucleotide bases. The bases are adenine (A), thymine (T), guanine (G) and cytosine (C). The human genome contains approximatel 3 billion of these base pairs, which reside in the 23 pairs of chromosomes within the nucleus of all our cells.
There are many parts of the genome with contiguous repetitions of the same nucleotide, so they are good candidates for compression.

## Task

Write a program in Java that takes the DNA Strand from the read of the sequencer and encodes it replacing repeated nucleotides with the number of repetitions followed by the repeated nucleotide.

**Input**

```text
ACTTTTTAGCCCCCCCGGGGTTTTTA
```
**Output**

```text
AC5TAG7C4G5TA
```
