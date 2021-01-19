import csv
import mysql.connector


#Database connectivy:Inserting into the "database" table 
data = mysql.connector.connect(user='root', passwd='halima', host='localhost', database='database')
cursor = data.cursor()

    # print programmer name 
    print("Program written by Halima Ahmed")
# this opens the datafile and reads
with open('13100262.csv', 'r') as datafile:
    CSVreader = csv.reader(datafile)
    # loops through the columns to display the top values and the header
    for row in CSVreader:
        cursor.execute(
            # Mysql database
            'INSERT INTO database(ref_date,geo,dguid,sex,age_group,student_response,uom,uom_id,scalar_factor,'
            'scalar_id,vector,coordinate,_value,_status,symbol,_terminated,decimals)'
            # File:13100262
            'VALUES ("%(REF_DATE)s", "%(GEO)s", "%(DGUID)s", "%(Sex)s", "%(Age group)s","%(Student response)s",''"%(UOM)s",' 
            '"%(UOM_ID)s", "%(SCALAR_FACTOR)s", "%(SCALAR_ID)s"," %(VECTOR)s","%(COORDINATE)s", "%(VALUE)s", '
            '"%(STATUS)s"," %(SYMBOL)s", "%(TERMINATED)s", "%(DECIMALS)s")', row)

   
    data.commit();
    data.close();
