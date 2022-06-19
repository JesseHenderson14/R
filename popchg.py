#Jesse Henderson

import pyodbc

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};' # Driver

                      'Server=stairway.usu.edu;' # Server name

                      'Database=501_jessehenderson;' # Database Name

                      'UID=501_JesseHenderson;' # User ID

                      'PWD=GoAggies!;' # Password

                      'Trusted_Connection=no;')

cursor = conn.cursor() #connection for sql to run queries
    
on = True #on/off for first while

on2 = True #on/off for second while

on3 = True #on/off for third while

while on: #first while
    
    stateab = input("Please enter a state abbreviation (UT, WY, etc..): ") #ask the user to input a state abbreviation
    
    if len(stateab) == 2: #if the state abbreviation is equal to a 2 letter string shuts off the while loop and continues
        on = False #turns off while loop
    
    else:
        print("\n\t•Please enter a two letter state abbreviation, must be two letters.") #if the inputted string is anything but a 2 letter string, asks the user for a two letter abbreviation then goes back to top of while loop.
        

while on2: #second while
    
    popchange = input("Please enter the new population of the state selected above: ") #asks the user for the new population of above state
    
    try: #this try and except makes sure the value inputted is an integer so the program won't crash if accidental string is inputted
        popchange = int(popchange) #setting popchange equal to an integer of itself to check data type entry
        
        if popchange > 0: #if the popchange is an integer greater than 0, break out of the while loop and store the input
            on2 = False #ends the while loop
        elif popchange < 1: #if the pop change is an integer, but it is less than 1, sends the user back to the beginning of the loop
            print("Please enter a number larger than 0.")
        
    except: #if the user inputted population is not an integer sends the user back to the beginning of the loop 
        print("Please enter a valid integer above 0.") 
        
        
cursor.execute("SELECT Population, StateID FROM USState WHERE StateID like ('%s');" % stateab) #runs a select query in SQL using the state inputted from the user
while on3: #third while
    
    for x in cursor:
        print("\n\tCurrent population of %s: %d" % (x[1],x[0])) #prints the current population of that state to the user
    
    surechange = input("Are you sure you want to change the value of %s population to %d? y/n? " % (stateab,popchange)) #asks the user to input yes or no to be fully sure they want to change the population of their selected state using their input from above

    if surechange == "y": #if the user inputs yes, break from this while loop. 
        break
            
    elif surechange == "n": #if the user inputs no, print the database will not be updated thus ending the program
        print("\n\tThe database will not be updated.")
        on3 = False #shuts off while loop and ends program
    
cursor.execute("UPDATE USState SET Population = %d WHERE StateID = '%s';" % (popchange, stateab)) #changes the value of the inputted population for the inputted state in the SQL database

conn.commit() #forces those changes to the database
        
cursor.execute("SELECT Population, StateID, StateName FROM USState WHERE StateID like ('%s');" % stateab) #SQL query to select the new state population, id, and name to output

for y in cursor: #prints the new state population, the existing id and existing statename
    print("\nStatename: %s \nStateID: %s \nPopulation: %d" % (y[2],y[1],y[0]))
        
        
    