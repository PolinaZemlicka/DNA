# DNA ID

Program that identifies a person based on their DNA.

1st command-line argument : name of a CSV file with STR counts for a list of individuals
2nd : name of a TXT file containing the DNA sequence to identify

STR: Short Tandem Repeats
CSV example:
name,AGAT,AATG,TATC
Alice,28,42,14
Bob,17,22,19
Charlie,36,18,25

program opens CSV file - reads it to memory
open the DNA sequence - reads it to memory

For each of the STRs (from the first line of the CSV file),
computes the longest run of consecutive repeats of the STR in the DNA sequence to identify.

If the STR counts match exactly with any of the individuals in the CSV file, 
prints out the name of the matching individual.
Else: print("No match")


