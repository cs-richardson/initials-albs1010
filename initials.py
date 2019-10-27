#Albert
'''
This is a program that, given a person’s name, prints the person’s initials
'''

get_string = input("")
#splits the names and put it into a list
name = get_string.split()
initials = ""

#Grabs the first letter of each name and store it
for i in name:
    initials = initials + i[0].upper()
    
initials = initials + "\n"

print(initials)
        
