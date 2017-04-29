#!/usr/local/bin/python3
from cgitb import enable
enable()

import pymysql as db
import os


def Deletion (file0):
         try:        
                     connection = db.connect(host = 'localhost', user = 'gwips', password = '', database ='rn6')
                     cursor = connection.cursor(db.cursors.DictCursor)
                     cursor.execute('DROP TABLE ' +file0)
                     print("Congratulations! Table is deleted")
                     cursor.close()
                     connection.close()
                     
         except db.Error as e :
             result  = "DB is in trouble at the moment. Call again later."   
             print ( e )
             return e

path1="/home/DATA/GWIPS_viz/gbdb/rn6/Schafer15/profiling/"
path2="/home/DATA/GWIPS_viz/gbdb/rn6/Schafer15/coverage/"
dirs1 = os.listdir(path1)
dirs2 = os.listdir(path2)
dirs = dirs1+dirs2
for file in dirs:
    file0 = os.path.splitext(file)
    file0 = file0[0]
    Deletion ( file0 )
 






