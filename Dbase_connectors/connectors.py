import sqlite3
import pyodbc
import mysql.connector
import psycopg2

class Connector():

    def __init__(self):
        
        #nothing to initialize ...
        pass

    def sqlite_connect(self, db_file):

        try:
            
            connection = sqlite3.connect(db_file)
            cursor = connection.cursor()
            
            return cursor 

        except Exception as e:

            return e

    def sqlserver_connect(self, driver, server, database, user, 
                                        password, trusted="no"):

        try:

            connection = pyodbc.connect("Driver={"+driver+"};\
                                            Server="+server+";\
                                            Database="+database+";\
                                            UID="+user+";\
                                            PWD="+password+";\
                                            Trusted_Connection="+trusted+";")

            cursor = connection.cursor()

            return cursor

        except Exception as e:

            return e


    def mysql_mariadb_connect(self, host, database, user, passwd, port=3306):

        try:

            connection = mysql.connector.connect(
                host = host,
                database = database,
                user = user,
                passwd = passwd,
                port = port
            )

            return connection
    
        except Exception as e:

            return e


    def postgresql_connect(self, host, database, user, password, port='5432'):

        try:
                connection = psycopg2.connect(
                    
                    host = host,
                    database = database,
                    user = user,
                    password = password,
                    port = port

                )

                cursor = connection.cursor()

                return cursor

        except Exception as e:

            return e