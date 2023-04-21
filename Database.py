import tkinter as tk
import sqlite3
import os

class db:
    
    _connection = None
    _file_dir = ""
    _cur = None

    def __init__(self, dir):
        self._file_dir = os.path.dirname(__file__) + dir
        self._connection = sqlite3.connect(self._file_dir)
        self._cur = self._connection.cursor()
        
    def check(self):
        if(self._cur!=None):
            print("Connection Successful!")
        else:
            print("Connection Unsuccessful.")
    
    def insertUser(self, Username:str, Password: str, LastName: str, FirstName: str, Email: str, Phone: int):
        sql_command = """INSERT INTO Users(Username, Password, Last_Name, First_Name, Email, Phone) VALUES (?, ?, ?, ?, ?, ?)"""
        sql_data = (Username, Password, LastName, FirstName, Email, Phone)
        self._cur.execute(sql_command, sql_data)
        self._connection.commit()
        print("User has been successfully added into the Database.")
    
    def returnID(self, Username):
        sql_command = """SELECT * FROM Users WHERE Username = ?"""
        sql_data = (Username,)
        self._cur.execute(sql_command, sql_data)
        ID = self._cur.fetchone()
        return ID[0]
        
    def deleteUser(self, Username):
        sql_command = """DELETE FROM Users WHERE UserID = ?"""
        sql_data = (self.returnID(Username),)
        self._cur.execute(sql_command, sql_data)
        self._connection.commit()
        print("User has been successfully deleted.")
    
    def searchUser(self, Username):
        sql_command = """SELECT * FROM Users WHERE UserID = ?"""
        sql_data = (self.returnID(Username),)
        self._cur.execute(sql_command, sql_data)
        print(self._cur.fetchone())
                
    def printTable(self, Table):
        sql_command = """SELECT * FROM """ + Table
        self._cur.execute(sql_command)
        data = self._cur.fetchall()
        if(len(data)==0):
            print("No Data found.")
        else:
            for row in data:
                print(row,'\n')
            
    def close(self):
        self._cur.close()
        self._connection.close()
        

        
def main():
    
    database = db("\Database\PPDatabase.db")
    database.check()
    database.printTable("Users")
    database.insertUser('ildpa', '12345', 'Palaruan', 'Ildreen,', 'Ildpa@gmail.com', 123456789)
    database.insertUser('juli', '150134', 'Arci', 'Juli', 'ArciJuli@gmail.com',123567802)
    database.printTable("Users")
    database.searchUser('juli')
    database.deleteUser('ildpa')
    database.printTable("Users")
    database.close()    
        
if __name__ == '__main__':
    main()