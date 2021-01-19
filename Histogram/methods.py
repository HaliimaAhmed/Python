import csv
from csv import writer
from Entity import _Entity

"""
By: Haliima Ahmed
Course:CST8333 Programming Language Research Project
Professor Name:Stanley Pieda
Assignment: 4
Due: March 25th,2020
This class edits, deletes, writes the datafile from the CSV file  
"""


class methods:

    def __init__(self):

        self.mains = []
        self.data = '13100262.csv'
        self.header = ["REF_DATE", "GEO", "DGUID", "Sex", "Age_group", "Student_response", "UOM", "UOM_ID",
                       "SCALAR_FACTOR", "SCALAR_ID", "VECTOR", "COORDINATE", "VALUE", "STATUS", "SYMBOL", "TERMINATED",
                       "DECIMALS"]

#write from file
    def write(self):

        with open(self.data, 'w') as write:
            csvWriter = csv.writer(write)
            csvWriter.writerow(self.header)
            for line in self.mains:
                csvWriter.writerow((
                    line.REF_DATE, line.GEO, line.DGUID, line.Sex, line.Age_group, line.Student_response,
                    line.UOM, line.UOM_ID, line.SCALAR_FACTOR, line.SCALAR_ID, line.VECTOR,
                    line.COORDINATE, line.VALUE, line.STATUS, line.SYMBOL, line.TERMINATED,
                    line.DECIMALS))
#create from file
    def create(self, _Entity):
        self.display()
        with open(self.data, 'a') as write:
            csvWriter = writer(write)
            csvWriter.writerow((_Entity.REF_DATE, _Entity.GEO, _Entity.DGUID, _Entity.Sex, _Entity.Age_group,
                                _Entity.Student_response, _Entity.UOM, _Entity.UOM_ID, _Entity.SCALAR_FACTOR,
                                _Entity.SCALAR_ID, _Entity.VECTOR, _Entity.COORDINATE, _Entity.VALUE, _Entity.STATUS,
                                _Entity.SYMBOL, _Entity.TERMINATED, _Entity.DECIMALS))

    # delete from file
    def delete(self, deleteRow):
        self.display()
        if self.saved(deleteRow):
            del self.mains[deleteRow - 1]
            self.write()

    # save from file
    def saved(self):
        array = len(self.mains)
        if 0 < id < array + 1:
            return True
        else:
            print("there is no record saved")
            return False

    # edit from file
    def edit(self, editor):
        self.display()
        edits = int(editor.id)
        del self.mains[edits - 1]
        self.mains.insert(edits - 1, editor)
        self.write()
