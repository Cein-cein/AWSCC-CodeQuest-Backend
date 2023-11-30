print("|===================================|",
      "\n|====== Day 11: File Handling ======|",
      "\n|====== Programmed by : Vince ======|",
      "\n|===================================|")

#Variable for file directory
directory = 'submissions\challenges\day-11\studentNames.txt'

print("\n***Unsorted Names of the Students***")
#Reads and prints studentNames.txt
with open(directory, 'r') as file:
    names = file.readlines()
    for newLine in names:
        print(newLine.strip())

#Overwrites the contents of studentNames.txt and sorts out the names alphabetically
with open(directory, 'w') as file:
    sortedNames = sorted(names)
    file.writelines(sortedNames)

print("\n***Sorted Names of the Students***")
#Reads and prints the updated studentNames.txt
with open(directory, 'r') as file:
    outputSortedNames = file.readlines()
    for newLine in outputSortedNames:
        print(newLine.strip())
    