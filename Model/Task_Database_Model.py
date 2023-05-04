import sqlite3 as sql
import pathlib as pl
import os

class taskManagerModel:
    def __init__(self):
        self._file_dir = str(pl.Path(os.path.dirname(__file__)).parents[0])+"\PPDatabase.db"
        self._connection = sql.connect(self._file_dir)
        self._cur = self._connection.cursor()
        self.Table = "Tasks"
        
    def AddTask(self, var):
        sql_command = """INSERT INTO """ + self.Table + """(Taskname, Progress, Description, Priority, DueDate) VALUES (?, ?, ?, ?, ?)"""
        self._cur.execute(sql_command, var)
        self._connection.commit()
        success = "Task has been added successfully!"
        return success  
    
    def DeleteTask(self, Name):
        sql_command = """DELETE FROM """ + self.Table + """ WHERE TaskName = ?"""
        sql_data = (self.run_comparison(Name),)
        self._cur.execute(sql_command, sql_data)
        self._connection.commit()
        print("Task has been successfully deleted")
        
    def run_comparison(self, Name):
        sql_command = """SELECT TaskName FROM """ + self.Table
        self._cur.execute(sql_command)
        TaskList = self._cur.fetchall()
        for task in TaskList:
            print(task[0])
            if(Name == task[0]):
                return self._cur.fetchone()[0]
            elif(Name != task[0]):
                continue
            else:
                print("Task not found.")
    
    
    