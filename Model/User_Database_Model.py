import sqlite3 as sql
import pathlib as pl
import os

class userManagerModel:
    
    _cur = None
    loginUser = ""
    
    #TABLES
    Table = "Users"
    
    def __init__(self):
        self._file_dir = str(pl.Path(os.path.dirname(__file__)).parents[0])+"\PPDatabase.db"
        self._connection = sql.connect(self._file_dir)
        self._cur = self._connection.cursor()
            
    def check(self):
        if(self._cur!=None):
            print("Connection Successful!")
        else:
            print("Connection Unsuccessful.")
    
    def searchEmail(self, Username=None, Email=None):
        if(Email != None):
            sql_command = """SELECT Email FROM """ + self.Table + """ WHERE Email = ?"""
            sql_data = (Email,)
            self._cur.execute(sql_command, sql_data)
            return self._cur.fetchone()[0] # Return Email
        elif(Username != None):
            sql_command = """SELECT Email FROM """ + self.Table + """ WHERE Username = ?"""
            sql_data = (Username,)
            self._cur.execute(sql_command, sql_data)
            return self._cur.fetchone()[0] # Return Username
        else:
            print("Invalid.")
    
    def getUser(self, Username):
        sql_command = """SELECT Username FROM """ + self.Table + """ WHERE Username = ?"""
        sql_data = (Username,)
        self._cur.execute(sql_command, sql_data)
        return self._cur.fetchone()[0] #Return Username
    
    def getName(self, Username):
        sql_command = """SELECT First_Name FROM """ + self.Table + """ WHERE Username = ?"""
        sql_data = (self.getUser(Username),)
        self._cur.execute(sql_command, sql_data)
        First_Name = self._cur.fetchone()[0]
        sql_command = """SELECT Last_Name FROM  """ + self.Table + """ WHERE Username = ?"""
        self._cur.execute(sql_command, sql_data)
        Last_Name = self._cur.fetchone()[0]
        return First_Name + " " + Last_Name
    
    def getPassword(self, Username):
        sql_command = """SELECT Password FROM """ + self.Table + """ WHERE Username = ?"""
        sql_data = (Username,)
        self._cur.execute(sql_command, sql_data)
        return self._cur.fetchone()[0] #Return Password 
    
    def run_comparison(self, User, Password):
        flag_username = False
        flag_password = False
        sql_command_username = """SELECT Username FROM """ + self.Table 
        self._cur.execute(sql_command_username)
        userList = self._cur.fetchall()
        for username in userList:
            print(username[0])
            if(User == username[0]):
                flag_username = True
                break
            elif(User != username[0]):
                continue
            else:
                print("User not found.")
                
        sql_command_password = """SELECT Password FROM """ + self.Table    
        self._cur.execute(sql_command_password)
        passList = self._cur.fetchall()
        for passcode in passList:
            if(Password == passcode[0]):
                flag_password = True
                break
            elif(Password != passcode[0]):
                continue
            else:
                print("Wrong Password.")   
        
        if(flag_username == True and flag_password == True):
            self.loginUser = User
            print(self.loginUser)
            return True
        
    def add_user(self, var):
        sql_command = """INSERT INTO """ + self.Table + """(Username, Password, Last_Name, First_Name, Sex, Email) VALUES (?, ?, ?, ?, ?, ?)"""
        self._cur.execute(sql_command, var)
        self._connection.commit()
        print("User has been successfully added into the Database.")
        
    def delete_user(self, Username):
        sql_command = """DELETE FROM """ + self.Users + """ WHERE UserID = ?"""
        sql_data = (self.returnID(Username),)
        self._cur.execute(sql_command, sql_data)
        self._connection.commit()
        print("User has been successfully deleted.")
    
        
if __name__ == '__main__':
    db = userManagerModel()
    db.check()
    if(db.run_comparison('a', 'b')):
        print("Login Succesful!")
    else:
        print("Login Unsuccessful.")
        
    db.getUser('a')
    db.getPassword('a')
    print(db.searchEmail(Email="joulesdearc@gmail.com"))
        
    
    
    
