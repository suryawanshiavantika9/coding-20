from collections import Counter

test_str = "aabbbbeeeefffggg"

# printing original string
print("The original string is : " + test_str)

# Consecutive characters frequency using Counter() and loop
res = []
count = 1

# using Counter() to count occurrence of each character
c = Counter(test_str)

# iterating through the string
for i in range(len(test_str)-1):
	# checking if the current character is equal to the next character
	if test_str[i] == test_str[i+1]:
		count += 1
	else:
		res.append(count)
		count = 1

res.append(count)

# printing result
print("The Consecutive characters frequency : " + str(res))



