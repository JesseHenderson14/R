#Jesse Henderson

#creating a blank list to store names
name_list = []

#this is the string placeholder for inputing names
name_input = ''

#keeping the while loop active as long as this is true, basically just changing it to false once a blank value has been entered.
active_naming = True

#the above variable is always true so this would be active forever until a condition is met changing active_naming to false
while active_naming:
     name = input("•Add first name to list or press enter to end list > ") #asking for an input of a name
    
     if len(name) == 0: #this is checking to see if there is a blank enter, if the length of the input is 0
        print("\n\tYou added", len(name_list),"names to this list.") #displays the total names added to the list by checking the length of the list after inputs
        active_naming = False #turns off the while loop by changing active_naming to false
        
     elif len(name) > 0: #if the length of the name entered is greater than 0, so they entered any string, this condition is met
        print("\n\tYou added %s to the list." %name) #displays the name added to the list
        name_list.append(name) #this adds the name to the list on line 4, adding items to a list each time a name is entered
        
for x in name_list: #for each value in the list name_list is what this is saying. So if place 0 in the list is "Jesse", then do something with that item. This iterates over the whole list until there are no more items to consider in the list. 
    print("\n\t","•",x) #new line for each name, x is each name in the list. 
    


