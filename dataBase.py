import pymysql
import sqlite3

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(host='162.256.19.89',
                      user='qanalze_dev24',
                      password='misbah@de55',
                      db='analyzeee_anyzer',
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)
        pass # end of DataBase

    def fetchFromDB(self, query):
        self.cursor = self.connection.cursor()
        self.cursor.execute(query)
        self.cursor.connection.commit()
        output = self.cursor.fetchall()
        self.cursor.close() #Closing the cursor
        return output # end of fetchFromDB function
    
    def insertToDB(self, query, values, tableName):
        self.cursor = self.connection.cursor()
        self.cursor.execute(query,values)
        self.cursor.connection.commit()
        self.cursor.execute(f""" SELECT * from {tableName}""")
        output = self.cursor.fetchall()
        lastRow = None
        for i in output:
            lastRow = i
        self.cursor.close() #Closing the cursor
        return lastRow # end of insertToDB function
    
    def deleteFromDB(self, query):
        self.cursor = self.connection.cursor()
        self.cursor.execute(query)
        self.cursor.connection.commit()
        return True
    pass # end of DataBase class

if __name__ == "__main__":
    dataBase = DataBase()
    tableName = "yolo_filters"
    query = """INSERT INTO yolo_filters (fid,cid,title,date_time) VALUES(%s,%s,%s,%s)"""
    values = (1,3,"Motorcycle","2023-07-18 12:49:22")