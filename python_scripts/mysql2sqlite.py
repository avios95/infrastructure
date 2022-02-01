import sqlite3, mysql.connector,re
from sqlite3 import Error
from mysql.connector import MySQLConnection, Error



def run_read_query(host, db, user, passwdord, SQLquery):
    try:
        conn = mysql.connector.connect(host=host, database=db, user=user, password=passwdord)
        if conn.is_connected():
            print('Connected to MySQL  database, run query: ' + SQLquery)
            cursor = conn.cursor()
            cursor.execute(SQLquery)
            result = cursor.fetchall()
            return result
    except Error as e:
        print(e)
    finally:
        conn.close()


def sqlite_conn(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print("Connection to SQLite DB successful")
        return conn
    except Error as e:
        print(e)

def sqlite_create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        print('Connected to SQLite database, run query: ' + create_table_sql)
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def sqlite_insert(conn, run_sql):
    try:
        c = conn.cursor()
        print('Connected to SQLite database, run query: ' + run_sql)
        c.execute(run_sql)
        conn.commit()
    except Error as e:
        print(e)

###############################
h='123.123.123.123'
u='userfordb'
d='namedb'
p='password'

sqlite_connection = sqlite_conn("./db_from_mysql.sqlite")
if sqlite_connection is not None:
    for tables_row in run_read_query(h, u, d, p, "SHOW TABLES;"):
        for tables in tables_row:
            #print(tables)

            query = "SHOW COLUMNS FROM " + tables + ";"
            collumns =""
            allcollumns=""
            for columns_row in run_read_query(h, u, d, p, query):
                #print(columns_row[0], " -----  ", columns_row[1:])
                type = " TEXT "
                if "int" in str(columns_row):  type = " INTEGER "
                pri = " NOT NULL "
                #if "PRI" in columns_row:  pri = " PRIMARY KEY "
                collumns = columns_row[0] + " " + type + pri
                allcollumns = allcollumns + ", " + collumns
            c = re.sub(',', '', allcollumns, 1)
            sql_create_table = "CREATE TABLE " + tables +" ( " + c +" );"
            sqlite_create_table(sqlite_connection, sql_create_table)

            allrow=""
            row=""
            query = "SELECT * FROM " + tables + ";"
            for content_row in run_read_query(h, u, d, p, query):
                if "datetime" in str(content_row): print("NEED FIX >> datetime <<  --->> " + str(content_row)); continue
                #print(content_row)
                # allrow = allrow + ", " + str(content_row)
                # c = re.sub(',', '', allrow, 1)
                sql_insert = "INSERT INTO " + tables +" VALUES "+ str(content_row) +" ;"
                #print(sql_insert)
                sqlite_insert(sqlite_connection, sql_insert)


else:
    print("Error! cannot create the database connection.")
