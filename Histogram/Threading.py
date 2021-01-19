import pandas
import threading

from Entity import _Entity

"""
By: Haliima Ahmed
Course:CST8333 Programming Language Research Project
Professor Name:Stanley Pieda
Assignment: 4
Due: March 25th,2020
thread class that will load the records inside the dataset.  

"""


# thread to execution to display the record
class Threading(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.mains = []
        self.data = pandas.read_csv('13100262.csv')

    # executes the code inside of the thread
    def run(self):
        print()

    # loads the data
    def reload(self):
        self.mains
        return self.mains


for line in range(5):
    # run multiple threads
    t = Threading()
    # invokes the run() above
    t.start()
