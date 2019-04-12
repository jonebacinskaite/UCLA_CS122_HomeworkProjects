# Python program to print all permutations with repetition of characters
def to_string(List):
	return ''.join(List)

# The main function that recursively prints all repeated permutations of the given string.
# data[] stores all permutations one by one
def all_lexicographic_recur (string, data, last, index):
	length = len(string)
	# One by one fix all characters at the given index and recur for the subsequent indexes
	for i in range(length):
		# Fix the ith character at index and if this is not the last index then recursively call for higher indexes
		data[index] = string[i]
		# If this is the last index then print the string stored in data[]
		if index==last:
			print(to_string(data))
		else:
			all_lexicographic_recur(string, data, last, index+1)

# This function sorts input string, allocate memory for data and calls allLexicographicRecur() for printing all permutations
def all_lexicographic(string):
	length = len(string)
	# Create a temp array that will be used by allLexicographicRecur()
	data = [""] * (length+1)
	# Sort the input string so that we get all output strings in lexicographically sorted order
	string = sorted(string)
	# Now print all permutations
	all_lexicographic_recur(string, data, length-1, 0)

# Driver program to test the above functions
string = "ABC"
print("All permutations with repetition of " + string + " are:")
all_lexicographic(string)

# This code is contributed to Bhavya Jain

