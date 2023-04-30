import sqlite3 as sql
import pathlib as pl
import os

class taskManagerModel:
    
    _cur = None
    
    #TABLES
    Table = "Tasks"
    
    def __init__(self):
        self._file_dir = str(pl.Path(os.path.dirname(__file__)).parents[0])+"\PPDatabase.db"
        self._connection = sql.connect(self._file_dir)
        self._cur = self._connection.cursor()
    
    
    
    