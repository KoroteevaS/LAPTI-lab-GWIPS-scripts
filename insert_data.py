#!/usr/local/bin/python3
from cgitb import enable
enable()

import pymysql as db
from sys import argv
import easygui
import os



def Creation (file0, path):
         print( 'haha %s' % (file0))
         try:        
                     connection = db.connect(host = 'localhost', user = 'gwips', password = '', database ='rn6')
                     cursor = connection.cursor(db.cursors.DictCursor)
                #cursor.execute("""SELECT COUNT(*) FROM information_schema.tables WHERE table_name = %s""" %(file0))
                # if cursor.rowcount > 0:
                 #    print("exists")
                  #   cursor.close()
                   #  connection.close()
                 #else:
                  #   print("Creating...")
                     cursor.execute('CREATE TABLE '+file0+' (filename varchar(255) not null) ')
                     print("Congratulations! Table is created")
                     cursor.close()
                     connection.close()
                     
         except db.Error as e :
             result  = "DB is in trouble at the moment. Call again later."   
             print ( e )
             return e

def Insertion ( file0, file3, path):
             try: 
                     fullname= path+file3
                     connection = db.connect(host = 'localhost', user = 'gwips', password = '', database ='rn6')
                     cursor = connection.cursor(db.cursors.DictCursor)
                #cursor.execute("""SELECT COUNT(*) FROM information_schema.tables WHERE table_name = %s""" %(file0))
                # if cursor.rowcount > 0:
                 #    print("exists")
                  #   cursor.close()
                   #  connection.close()
                 #else:
                  #   print("Creating...")
                     cursor.execute('INSERT into '+file0+' VALUES(%s);', (fullname))
                     print("Congratulations! Links are inserted")
                     cursor.close()
                     connection.commit()    
             except db.Error as e :
                      result  = "DB is in trouble at the moment. Call again later."   
                      print ( e )
                      return e 

def TrackDbinsertion ( insertionstatement ):
                 try:
                      connection = db.connect(host = 'localhost', user = 'gwips', password = '', database ='rn6')
                      cursor = connection.cursor(db.cursors.DictCursor)
                      cursor.execute('%s'% ( insertionstatement ));
                      print("Congratulations! Data is inserted")
                      cursor.close()
                      connection.commit() 

                 except db.Error as e :
                      result  = "DB is in trouble at the moment. Call again later."   
                      print ( e )
                      return e 


#def Myset( file0 ):
#
 #   myset = file1.split('_')
  #  if 'heart' in myset:
   #     setopt1 = 'heart'
    #if 'liver' in myset:
#        setopt1 = 'liver'
 #   if 'RP' in myset:
  #      setopt2 = 'RiboProElong'
   # if 'RiboCov' in myset:
    #    setopt2 = 'RiboCov'
#    if 'mRNACov' in myset:
 #       setopt2 = 'mRNACov'
  #  info2 = 'autoScale on\nalwaysZero on\nparent Schafer15_%s_%s off' % (setopt1, setopt2)
   # print info2
    


#def checkTableExists(dbcon, tablename):
 #   dbcur = dbcon.cursor()
  #  dbcur.execute("""
   #     SELECT COUNT(*)
    #    FROM information_schema.tables
     #   WHERE table_name = '{0}'
      #  """.format(tablename.replace('\'', '\'\'')))
   # if dbcur.fetchone()[0] == 1:
    #    dbcur.close()
     #   return True

   # dbcur.close()
    #return False
path1="/home/DATA/GWIPS_viz/gbdb/rn6/Schafer15/profiling/"
path2="/home/DATA/GWIPS_viz/gbdb/rn6/Schafer15/coverage/"
dirs1 = os.listdir(path1)
dirs2 = os.listdir(path2)
info1 = 'Ribo-seq coverage plots carried out in SHR/Ola and BN-Lx strains (Schafer et al. 2015)'

for file1 in dirs1:
    file0 = os.path.splitext(file1)
    file0 = file0[0]
    Creation (file0, path1)
    file3 = file1
    path = path1
    Insertion(file0, file3, path)
    myset = file0.split('_')
    if 'heart' in myset:
        setopt1 = 'heart'
    if 'liver' in myset:
        setopt1 = 'liver'
    if 'RP' in myset:
        setopt2 = 'RiboProElong'
    if 'RiboCov' in myset:
        setopt2 = 'RiboCov'
    if 'mRNACov' in myset:
        setopt2 = 'mRNACov'
    info2 = 'autoScale on\\nalwaysZero on\\nparent Schafer15_%s_%s off' % (setopt1, setopt2)
    #print info2
    insertionstatement = "INSERT INTO trackDb VALUES ('"+file0+"','all','bigWig','"+info1+"',0,1,0,200,0,0,200,0,0,0,0,'','','','RP-ElongatingRibos',1,'"+info2+"');"
   # print (insertionstatement)
    TrackDbinsertion ( insertionstatement )
 

for file2 in dirs2:
    file0 = os.path.splitext(file2)
    file0 = file0[0]
    Creation ( file0, path2)
    file3 = file2
    path = path2
    Insertion(file0, file3, path)
    myset = file0.split('_')
    if 'heart' in myset:
        setopt1 = 'heart'

    if 'liver' in myset:
        setopt1 = 'liver'

    if 'RP' in myset:
        setopt2 = 'RiboProElong'
    if 'RiboCov' in myset:
        setopt2 = 'RiboCov'
    if 'mRNACov' in myset:
        setopt2 = 'mRNACov'
    info2 = 'autoScale on\\nalwaysZero on\\nparent Schafer15_%s_%s off' % (setopt1, setopt2)
    #print info2
    insertionstatement = "INSERT INTO trackDb VALUES ('"+file0+"','all','bigWig','"+info1+"',0,1,0,200,0,0,200,0,0,0,0,'','','','RP-ElongatingRibos',1,'"+info2+"');"
    #print (insertionstatement)
    TrackDbinsertion ( insertionstatement )


      




#print(" Step 1. Entering path ")
#value = int(input("input 1 "))
#if  value ==  1:
 #   path = easygui.fileopenbox

#print (path )
#print("Step 2. Entering names")
#try: 
 #    dir_path(path + "/profiles/")
  #   frp = ftplib.FTP( dir_path 





