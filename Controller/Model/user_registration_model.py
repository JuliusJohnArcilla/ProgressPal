import sqlite3
import os
import pathlib as pl

class registerModel:
    
    _connection = None
    _cur = None
    
    #TABLES
    Users = "Users"

    def __init__(self, dir):
        self._file_dir = str(pl.Path(os.path.dirname(__file__)).parents[1]) + dir
        self._connection = sqlite3.connect(self._file_dir)
        self._cur = self._connection.cursor()

    def check(self):
        if(self._cur!=None):
            print("Connection Successful!")
        else:
            print("Connection Unsuccessful.")
    
    def insertUser(self, var):
        sql_command = """INSERT INTO """ + self.Users + """(Username, Password, Last_Name, Middle_Name, First_Name, Sex, Email, Phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
        self._cur.execute(sql_command, var)
        self._connection.commit()
        print("User has been successfully added into the Database.")
        
    def deleteUser(self, Username):
        sql_command = """DELETE FROM """ + self.Users + """ WHERE UserID = ?"""
        sql_data = (self.returnID(Username),)
        self._cur.execute(sql_command, sql_data)
        self._connection.commit()
        print("User has been successfully deleted.")
    
    def searchUser(self, Username):
        sql_command = """SELECT * FROM """ + self.Users + """ WHERE UserID = ?"""
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
    
    database = registerModel("\PPDatabase.db")
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