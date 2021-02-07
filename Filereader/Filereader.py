'''
By: Haliima Ahmed
This program reads the datafile from the CSV file and displays them in the columns below.
'''

import csv
# this opens the datafile and gets rid of the encoding before the firstline of code
with open('13100262.csv') as datafile:

    CSVreader = csv.reader(datafile)
    #print Halima Ahmed
    print("Program written by Halima Ahmed")
    #loops through the columns to display the top values and the header
    for row in CSVreader:
        print(row[0]," ", row[1]," ",row[3]," ",row[4],"  ",row[ 5],"  ", row[6]," ", row[7]," ", row[8]," ",
              row[9]," ", row[10]," ", row[11]," ", row[12]," ", row[13]," ", row[14]," ", row[15]," ", row[16])

