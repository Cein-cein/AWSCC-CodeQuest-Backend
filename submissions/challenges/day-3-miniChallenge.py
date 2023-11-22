print("|====================================|",
      "\n|=== Day 3: POSITIVE or NEGATIVE? ===|",
      "\n|======= Programmed by: Vince =======|"
      "\n|====================================|")

num = float(input("Enter a number: "))

if num > 0:
    print(f"{num} is a POSITIVE number!")
elif num < 0:
    print(f"{num} is a NEGATIVE number!")
else:
    print("That number is Zero!")