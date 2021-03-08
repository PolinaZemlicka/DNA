from sys import argv, exit
import csv
import re


def main():

    if len(argv) != 3:
        print("Expecting 2 command-line arguments here")
        exit(1)

    filename_txt = argv[2]                       # txt file - open - read
    with open(filename_txt, 'r') as f2:
        dna = f2.read()                          # long ribbon of dna

    if argv[1] == 'databases/small.csv':         # small and else: large csv files
        ls = ['AGATC', 'AATG', 'TATC']           # list of STRs
    else:
        ls = ['AGATC', 'TTTTTTCT', 'AATG', 'TCTAG', 'GATA', 'TATC', 'GAAA', 'TCTG']

    dls = ['Name']                               # list STR counts in dna sample

    for STR in ls:
        g = re.findall(fr'(?:{STR})+', dna)      # list of strings of ALL consecutive repeats of the STR
        if len(g) == 0:
            dls.append('0')
        else:
            l = max(g, key=len)                  # the longest string from the list
            dls.append(str(len(l) // len(STR)))  # making a list of len(STRs) just like the csv file

    filename_csv = argv[1]                       # csv file - open - read
    with open(filename_csv) as f1:
        for row in csv.reader(f1):               # iterate
            if row[1:] == dls[1:]:               # compare to my list or len(STRs)
                print(row[0])                    # print name of match
                break
        else:
            print('No match')


if __name__ == "__main__":
    main()

