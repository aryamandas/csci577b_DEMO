
import sys

def main():
	selection = input("Which function would you like to call? (enter number) \n 1. sum \n 2. fruit \n")

	if selection == "1" or selection == "sum":
		sum()
	elif selection == "2" or selection == "fruit":
		fruit()
	else:
		print("Invalid function choice. Exiting the program ...")
		sys.exit(1)


'''
Takes two numbers from the input and returns the sum
'''	
def sum():
	# Retrieve the input
	num1 = input("Enter the first number: ")
	num2 = input("Enter the second number: ")

	# Calculate the sum
	sum = float(num1) + float(num2)

	# Display the sum
	print("The sum of {} and {} is {}.".format(num1, num2, sum))


'''
Create a fruit basket
'''
def fruit():
	# Define an empty fruit basket
	fruit_basket = []
	more_fruit = True

	while more_fruit:
		choice = input("Please name a fruit: ")
		if choice not in fruit_basket:
			print("Adding {} to basket!".format(choice))
			fruit_basket.append(choice)
		else:
			print("Sorry, this fruit is already in the basket.")

		repeat = input("Would you like to enter more fruit? (Enter 'y' for yes and 'n' for no) ")

		if repeat == 'y' or repeat == 'yes':
			more_fruit = True
		else:
			more_fruit = False

	print("Contents of the fruit basket: {}".format(fruit_basket))


if __name__ == "__main__":
	main()