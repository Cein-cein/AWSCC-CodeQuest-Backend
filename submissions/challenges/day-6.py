print("|====================================|",
      "\n|=== Day 6: Loops (FizzBuzz Game) ===|",
      "\n|======= Programmed by: Vince =======|",
      "\n|====================================|")

print("\nWelcome to the FizzBuzz Game!")

#Asks user to enter a limit for range
limitNum = int(input("Enter a number limit: "))

#Loops according to user input
#Add 1 to user input to include the inputted number as the last number
for x in range(limitNum+1):
    #Exclude 0 in output
    if x == 0:
        print("")
    elif (x%3 == 0) and (x%5 == 0):
        print("FizzBuzz!")
    elif x%3 == 0:
        print("Fizz")
    elif x%5 == 0:
        print("Buzz")
    else:
        print(x)
