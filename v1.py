print "This is Pizza Pi R Squared.  What's it do?  It lets you determine whether buying a small pizza or a large pizza is a better value in terms of cost per bite of pizza."
 
diameter_one = int(raw_input("What's the first pizza's diameter (in inches)?"))
cost_one = int(raw_input("How much does the first pizza cost? (in dollars and cents)"))
area_one = (diameter_one / 2) **2 * 3.14
total_one = cost_one / area_one

print "With this pizza, you're paying %s cents per square inch." % (total_one)

diameter_two = int(raw_input("What's the second pizza's diameter (in inches)?"))
cost_two = int(raw_input("How much does the second pizza cost? (in dollars and cents)"))
area_two = (diameter_two / 2) **2 * 3.14
total_two = cost_two / area_two

print "With this pizza, you're paying %s cents per square inch." % (total_two)

if total_one < total_two:
	print "The first pizza is a better value. Buy that one!"
elif total_two < total_one:
	print "The second pizza is the better deal - more pizza for the buck. Get that one!"
else:
	print "Same deal - get whichever you'd like!"
	

#I'm a noob python programmer and this is my first script, other than those from "Learn Python the Hard Way."  
#Suggestions/improvements/ideas appreciated!
#Feel free to drop me a note at gteninbaum@suffolk.edu.
