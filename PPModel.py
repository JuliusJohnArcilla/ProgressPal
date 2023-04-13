import sqlite3
import SQLTools as SQL


conn = sqlite3.connect("PPDatabase.db")
SQL.checkConn(conn)

while(True):
    choice = input("Enter a command: (?help for list of commands)")
    try: 
        match choice:
            case "?help":
                SQL.commandList()
            case "?insertData":
                SQL.insertData(conn)
            case "?close":
                break
            case _:
                print("Invalid command.")
                continue
    except:
        continue
            



conn.close()