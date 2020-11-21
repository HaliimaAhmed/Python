import threading

from Entity import _Entity
from Threading import Threading


"""
By: Haliima Ahmed
Course:CST8333 Programming Language Research Project
Professor Name:Stanley Pieda
Assignment: 4
Due: March 25th,2020
This class lets the user perform the functions defined inside methods.py and display it in the main menu.
"""

crud = Threading()
Record = crud.reload()


# displays the records saved in the reload() in methods.py. this will display the values inside the csv file.
def displayRecord():
    try:
        Record = crud.reload()
        for column in Record:
            print("Display Record = ", column.REF_DATE, column.GEO, column.DGUID, column.Sex,
                  column.Age_group, column.Student_response, column.UOM,
                  column.UOM_ID, column.SCALAR_FACTOR, column.SCALAR_ID,
                  column.VECTOR, column.COORDINATE, column.VALUE, column.STATUS,
                  column.SYMBOL, column.TERMINATED, column.DECIMALS)
    except:
        print("try again")


# lets the user input the information they want to edit
def editRecord():
    try:
        edit = input("edit: ")
        if crud.saved(int(edit)):
            REF_DATE = input("enter ref date:")
            GEO = input("enter geo:")
            DGUID = input("enter diguid:")
            Sex = input("enter sex:")
            Age_group = input("enter age group: ")
            Student_response = input("enter student responses:")
            UOM = input("enter uom:")
            UOM_ID = input("enter uom id:")
            SCALAR_FACTOR = input("enter scalar factor:")
            SCALAR_ID = input("enter scalar id:")
            VECTOR = input("enter vector:")
            COORDINATE = input("enter coordinates:")
            STATUS = input("enter status:")
            VALUE = input("enter value:")
            SYMBOL = input("enter symbol:")
            TERMINATED = input("enter terminated:")
            DECIMALS = input("enter decimals:")

            DataSet_new = _Entity(edit, REF_DATE, GEO, DGUID, Sex, Age_group, Student_response, UOM, UOM_ID,
                                  SCALAR_FACTOR, SCALAR_ID, VECTOR, COORDINATE, VALUE, STATUS, SYMBOL, TERMINATED,
                                  DECIMALS)
            crud.edit(DataSet_new)
    except:
        print("try again")


# allows the user to create values.
def createRecord():
    try:
        REF_DATE = input("enter ref date:")
        GEO = input("enter geo:")
        DGUID = input("enter diguid:")
        Sex = input("enter sex:")
        Age_group = input("enter age group: ")
        Student_response = input("enter student responses:")
        UOM = input("enter uom:")
        UOM_ID = input("enter uom id:")
        SCALAR_FACTOR = input("enter scalar factor:")
        SCALAR_ID = input("enter scalar id:")
        VECTOR = input("enter vector:")
        COORDINATE = input("enter coordinates:")
        STATUS = input("enter status:")
        VALUE = input("enter value:")
        SYMBOL = input("enter symbol:")
        TERMINATED = input("enter terminated:")
        DECIMALS = input("enter decimals:")

        DataSet_new = _Entity(REF_DATE, GEO, DGUID, Sex, Age_group, Student_response, UOM, UOM_ID,
                              SCALAR_FACTOR, SCALAR_ID, VECTOR, COORDINATE, VALUE, STATUS, SYMBOL, TERMINATED,
                              DECIMALS)
        crud.create(DataSet_new)

    except:
        print("try again")


# user cna delete a record. it will go through an exception
def deleteRecord():
    try:
        delete = input("Enter record to delete: ")
        crud.deleted(int(delete))

    except Exception:
        print("error! please try again")


# users menu: allows the user to display, create, edit and delete through all options
def sortRecord():
    pass


def menu():
    def project_menu():
        try:
            print("   Welcome to Haliima Ahmed's program \n ")
            print("1. Display all the records ")
            print("2. Create a new record ")
            print("3. Display and edit a record ")
            print("4. Delete a record ")
            print("5. sort a record ")
            print("6. Histogram ")

        except Exception as e:
            print(e)

    # loop set to boolean
    loop = True
    # while loop to go through the values and process the functions
    while loop:
        project_menu()
        choice = input("Enter your value here: ")

        if choice == '1':
            displayRecord()
            print("Halima Ahmed:all records have been displayed\n")

        elif choice == '2':
            createRecord()
            print("Halima Ahmed:successfully created new record\n")

        elif choice == '3':
            editRecord()
            print("Halima Ahmed:selected, displayed and edited records\n")

        elif choice == '4':
            deleteRecord()
            print("Halima Ahmed:deleted a record\n")

        elif choice == '5':
            deleteRecord()
            print("Halima Ahmed:sorted a record\n")

        elif choice == '6':
            from Final import finalMenu
            finalMenu()
            print("Halima Ahmed:age/gender of user\n")
            loop = True
        # user must enter a value from 1-4
        else:
            input("ERROR please try again..\n")

    return [choice]


menu()
