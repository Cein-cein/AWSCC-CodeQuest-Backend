import areaCircle

print("|===================================|",
      "\n|=== Day 9: Modules and Packages ===|",
      "\n|====== Programmed by: Vince =======|",
      "\n|===================================|")

print("\nCalculate the area of a circle\n")

num = int(input("Enter the radius: "))

area = areaCircle.area(num)

print(f"\nThe area of the circle is {round(area, 2)}")
