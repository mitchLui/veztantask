# Completed 27 May 2020 - Job Application Withdrawn


"""
Write a Python function to count the occurrences of each character in a given string. 
For example, given the string "ab", your function should return [['a', 1], ['b', 1]].
"""

# Counts the occurrences of each charcter in the given string
def countString():
	# Asks user to enter a string
	statement = input("Enter String: ")
	# Create a dictionary 
	occurrences = {}
	# for every character in the dictionary, use it as a key and count how many times it appears in the string. If it exists more than once, the value of the key is incremented by 1. Otherwise, the key's value is 1.
	for word in statement:
		if word in occurrences:
			occurrences[word] += 1
		else:
			occurrences[word] = 1
	# Converting the answer to the desired format
	# Initialises array that will contain the final answer
	answerArray = []
	for key, value in occurrences.items():
		# Creates a temporary array that stores the character and its number of occurrences in it
		temp = [key, value]
		answerArray.append(temp)
	print("Answer: {0}".format(answerArray))

if __name__ == "__main__":
	countString()