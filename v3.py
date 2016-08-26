print "\n\nWELCOME TO PIZZA PI R SQUARED. \n\nWhat's it do?  \n\nIt lets you determine whether buying a small pizza or a large pizza is a better value."
 
diameter_one = float(raw_input("\nWhat's the first pizza's diameter (in inches)?"))
cost_one = float(raw_input("\nHow much does the first pizza cost? (in dollars and cents)"))
area_one = (diameter_one / 2) **2 * 3.14
total_one = cost_one / area_one

print "\nWith this pizza, you're paying $%s per square inch." % (total_one)

diameter_two = float(raw_input("\nWhat's the second pizza's diameter (in inches)?"))
cost_two = float(raw_input("\nHow much does the second pizza cost? (in dollars and cents)"))
area_two = (diameter_two / 2) **2 * 3.14
total_two = cost_two / area_two

print "\nWith this pizza, you're paying $%s per square inch." % (total_two)

if total_one < total_two:
	print "\nThe first pizza is a better value. Buy that one!"
elif total_two < total_one:
	print "\nThe second pizza is the better deal - more pizza for the buck. Get that one!"
else:
	print "\nSame deal per square inch of pizza - they represent the same value."
	

#Suggestions/improvements/ideas appreciated!
Gabe Teninbaum / gteninbaum@suffolk.edu
