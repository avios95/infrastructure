#!/usr/bin/python

import sqlite3, re, sys
from sqlite3 import Error

##################################################### def #############################################################

def sqlite_conn(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print("Connection to SQLite DB successful")
        return conn
    except Error as e:
        print(e)


def sqlite_exec(query):
    try:
        cursor.executescript(query)
        print("RUN Sqlite query --==> " + query + "; <==--")
    except Error as e:
        if "no such table" in str(e) : return 0
        else:
            print("!!!!! ERROR in query !!!!! " + query + " ----> " + str(e))


def get_args():
    inputfile = ''
    outputfile = ''
    try:

        if len (sys.argv) == 1:
            print("""
            Please run from console(you can use -i and -o ):
            /usr/bin/python3 /path/to/sql2sqlite.py -i /path/to/inputfile.sql -o /path/to/outputfile.sqlite
            """)
        else:
            if len (sys.argv) < 5:
                print ("Error: Too few parameters.")
                sys.exit (1)

            if len (sys.argv) > 5:
                print ("Error. Too many options.")
                sys.exit (1)

            param_name = sys.argv[1]
            param_value = sys.argv[2]
            param_name2 = sys.argv[3]
            param_value2 = sys.argv[4]
            if (param_name == "-i"):
                #print ("-i = " + param_value )
                inputfile = param_value
            elif(param_name == "-o"):
                #print("-o = " + param_value)
                out_dir = param_value
            else:
                err = "Error. Unknow parrametr '{}'".format (param_name)

            if (param_name2 == "-i"):
                #print ("-i = " + param_value2 )
                inputfile = param_value2
            elif(param_name2 == "-o"):
                #print("-o = " + param_value2)
                outputfile = param_value2
            else:
                err = "Error. Unknow parrametr '{}'".format (param_name2)
    except:
        print(err)
        sys.exit(1)
    return inputfile, outputfile

######################################################## main #########################################################

# SQLdbPath = "./petclinic.sql"
# SQLitedbPath = "./petclinic.sqlite"


SQLdbPath, SQLitedbPath = get_args()
print("File in: "+SQLdbPath)
print("File out: "+SQLitedbPath)

sqlite_connection = sqlite_conn(SQLitedbPath)
cursor = sqlite_connection.cursor()
sql_file = open(SQLdbPath, encoding="utf8").read().split(';')

for command in sql_file:
    command = re.sub('(?m)^UNLOCK.*\n?', '', command)                   # remove UNLOCK command
    command = re.sub('(?m)^LOCK.*\n?', '', command)                     # remove LOCK command
    command = re.sub('(?m)^REM.*.\n^SET.*', '', command)                # remove REM command
    command = re.sub('AUTO_INCREMENT=\S+', '', command)                 # remove AUTO_INCREMENT int parametrs
    command = re.sub('ENGINE=\S+', '', command)                         # remove ENGINE type
    command = re.sub('DEFAULT CHARSET=\S+', '', command)                # remove DEFAULT CHARSET
    command = re.sub('AUTO_INCREMENT', '', command)                     # remove AUTO_INCREMENT in autoincrement colums
    command = re.sub('ALTER TABLE.*.DISABLE CONSTRAINT', 'ALTER TABLE DROP COLUMN', command)
    command = re.sub('ENABLE CONSTRAINT', 'ADD COLUMN', command)
    command = re.sub('unsigned', '', command)                           # remove unsigned
    command = re.sub('\'', '\"', command)                               # replace ' to "
    command = re.sub('(?m)^-.*', '', command)                           # remove string with first symbol -
    command = re.sub('(?m)^\/.*\n?', '', command)                       # remove string with first symbol /
    command = re.sub('(?m)^\n', '', command)                            # remove all null string
    command = re.sub('\,.*\n.*.KEY \`.*.\` \(\`.*.\`\)', '', command)   # remove KEY parametrs

    if command != "":
        sqlite_exec(command)
    else:
        continue
