def checkConn(db):
    try:
        cur = db.cursor()
        print("Connection Successful")
    except:
        print("Connection Unsuccessful")
        
def insertData(db):
    cur = db.cursor()
    while(True):
        choice = input("[1]User\n[2]Employee\n")
        match int(choice):
            case 1:
                Username = input("Enter the username: ")
                Password = input("Enter the Password: ")    
                LastName = input("Enter your Last Name: ")
                FirstName = input("Enter the First Name: ")
                Email = input("Enter your Email Address: ")
                Phone = int(input("Enter your Phone Number: "))
                sql_command = """INSERT INTO Users(Username, Password, Last_Name, First_Name, Email, Phone) VALUES (?, ?, ?, ?, ?, ?)"""
                sql_data = (Username, Password, LastName, FirstName, Email, Phone)
                cur.execute(sql_command, sql_data)
                print("data inserted successfully!")
                
            case 2:
                Username = input("Enter the username: ")
                Password = input("Enter the Password: ")    
                LastName = input("Enter your Last Name: ")
                FirstName = input("Enter the First Name: ")
                Address = input("Enter your Address: ")
                Email = input("Enter your Email Address: ")
                Phone = int(input("Enter your Phone Number: "))
                sql_command = """INSERT INTO Employees(Username, Password, Last_Name, First_Name, Address, Email, Phone) VALUES (?, ?, ?, ?, ?, ?, ?)"""
                sql_data = (Username, Password, LastName, FirstName, Address, Email, Phone)
                cur.execute(sql_command, sql_data)
                print("data inserted successfully!")
            
            case 0:
                break
            
    db.commit()
    db.close()
            

def commandList():
    print("?inserData\n?close\n")
    