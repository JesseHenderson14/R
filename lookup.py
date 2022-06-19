#Jesse Henderson


import pyodbc

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};' # Driver

                      'Server=stairway.usu.edu;' # Server name

                      'Database=501_jessehenderson;' # Database Name

                      'UID=501_JesseHenderson;' # User ID

                      'PWD=GoAggies!;' # Password

                      'Trusted_Connection=no;')

cursor = conn.cursor() #connection for SQL queries to run

active = True #on/off for while loops

counter = 0 #counter to check if there are actual records of selected people in database

while active:
    id_or_name = input("Would you like to lookup customer by ID or name? ") #asking user to input a name or ID
    try: #this first try checks whether or not the user inputted 'name' or 'id', if they did not enter either the corresponding except runs and reruns the loop. 
        id_or_name == "ID" 
        id_or_name == "name"
        if id_or_name == "ID": #this checks if the user inputted 'ID'
            id_input = input("Please enter your Customer ID: ") #once the user inputs 'ID' this asks for the user ID
            try: #this try checks if the user inputted an integer, if not the corresponding except will run and start this loop over again
                id_input = int(id_input)
                cursor.execute("SELECT Fname, Lname, Gender, CustState, CustID, Population FROM Customer C, USState U WHERE CustID = '%d' and C.CustState = U.StateID;" % id_input) #using an SQL query with the user inputted ID to select that ID from the database.
                for x in cursor: #this prints the selected items from the query above
                    counter += 1 #checking if there are existing records
                    print("Firstname: %s Lastname: %s Gender: %s State: %s CustomerID: %d State Population: %d" % (x[0],x[1],x[2],x[3],x[4],x[5]))    
                if counter == 0: #if the counter is 0 the records don't exist, tells the user there are no records
                    print("\n\t•Customer ID does not exist.")
                    continue
                ask_again = input("Enter another name or ID y/n? ") #asks the user if they would like to continue checking more names or ID's
                if ask_again == "y": #if they type yes reruns the loop
                    continue
                elif ask_again == "n": #if they type no ends the program
                    active = False
                    print("\n\t•Thank you, have a nice day.")
                else: 
                    print("Please enter y or n") #checks the user input for yes or no and loops back if not either
            except: 
                print("Please enter a valid customer ID")
                    
                
                
        elif id_or_name == "name": #checks if the user entered name for first entry
            fname_input = input("Please enter your first name: ") #checks first name input
            lname_input = input("Please enter your last name: ") #checks last name input
            
            if fname_input == '' and len(lname_input) > 0: #if the user doesn't enter a first name but enters a last name
                percent = '%' #this is a placeholder for wildcards in SQL, python gets funny about placeholders and parentheses
                cursor.execute("SELECT Fname, Lname, Gender, CustState, CustID, Population FROM Customer C, USState U WHERE Lname like ('%s') and Fname like ('%s') and C.CustState = U.StateID;" %   (lname_input, percent)) #this is taking the user first name and last name user inputs and running them in an SQL query
                for x in cursor: #lines 58-69 are the same purpose as lines 34-45 above
                    counter += 1
                    print("Firstname: %s Lastname: %s Gender: %s State: %s CustomerID: %d State Population: %d" % (x[0],x[1],x[2],x[3],x[4],x[5]))
                if counter == 0:
                    print("\n\t•Customer does not exist.")
                    continue
                ask_again3 = input("Enter another name or ID y/n? ")
                if ask_again3 == "y":
                    continue
                elif ask_again3 == "n":
                    active = False
                    print("\n\t•Thank you, have a nice day.")
                else:
                    print("Please enter y or n") #checks the user input for yes or no and loops back if not either
            elif len(fname_input) > 0 and len(lname_input) > 0: #if both last name and first name are inputted run this
                cursor.execute("SELECT Fname, Lname, Gender, CustState, CustID, Population FROM Customer C, USState U WHERE Lname = '%s' and Fname = '%s' and C.CustState = U.StateID;" %  (lname_input, fname_input))
                for x in cursor: #lines 76-87 are the same purpose as lines 58-69 above
                    counter += 1
                    print("Firstname: %s Lastname: %s Gender: %s State: %s CustomerID: %d State Population: %d" % (x[0],x[1],x[2],x[3],x[4],x[5]))
                if counter == 0:
                    print("\n\t•Customer does not exist.")
                    continue
                ask_again2 = input("Enter another name or ID y/n? ")
                if ask_again2 == "y":
                    continue
                elif ask_again2 == "n":
                    active = False
                    print("\n\t•Thank you, have a nice day.")
                else:
                    print("Please enter y or n")
                    
        elif id_or_name != "name" or id_or_name != "ID": #this is the first part of the if in line 29. If the user inputs something other that 'name' or 'ID', notifies the user to enter either ID or name.
            print("Enter either ID or name") 
        
    except: #this try and except is only trying for 2 variable names, I could have used this to run if it was not an ID but a name or vice versa. Made more sense to me to do it this way and not split the code in two huge parts. 
        print()
        













        