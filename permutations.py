from itertools import permutations
import math

# Permutation Function #

def allPerms(inputSet):

	global permList
	permList = permutations(inputSet)

	global num
	num = math.factorial(len(inputList))

	return permList

# Inputs #

inputSet = input("Enter your elements separated by spaces:\n")
inputList = []

for x in inputSet.split():
	inputList.append(x)

allPerms(inputList)

# Choice: Print to terminal or txt file #

while True:
	choice = input("There are {} permutations. Print to text file? (y/n)\n".format(num))
	if choice != "y" and choice != "n":
		print("Invalid input.")
	else:
		break

# Print to terminal #

if choice == "n":
	while True:
		choice2 = input("Spaces between elements? (y/n)\n")
		if choice2 != "y" and choice2 != "n":
			print("Invalid input.")
		else:
			break
	print("=======\nAll {} permutations:\n=======\n".format(num))
	if choice2 == "n":
		for perm in permList:
			print(''.join(perm))
	else:
		for perm in permList:
			print(' '.join(perm))

# Print to txt file #

else:
	while True:
		choice2 = input("Spaces between elements? (y/n)\n")
		if choice2 != "y" and choice2 != "n":
			print("Invalid input.")
		else:
			break
	with open("permutationList.txt","w+") as File_object:
		File_object.write("{} permutations:\n=======\n".format(num))
		if choice2 == "y":
			for perm in permList:
				File_object.writelines("%s\n" % str(' '.join(perm))) 
		else:
			for perm in permList:
				File_object.writelines("%s\n" % str(''.join(perm))) 
	print("Permutations written to permutationList.txt")
	File_object.close()
