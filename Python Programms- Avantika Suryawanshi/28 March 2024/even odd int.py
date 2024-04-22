# Create a list 'array_nums' containing integers
array_nums = [1, 2, 3, 5, 7, 8, 9, 10]

# Display a message indicating that the following output will show the original array
print("Original arrays:")
print(array_nums)  # Print the contents of 'array_nums'

# Use the 'filter()' function with lambda functions to filter and count the number of odd and even numbers
# Use 'filter()' with a lambda function to filter and count the number of odd numbers in 'array_nums'
odd_ctr = len(list(filter(lambda x: (x % 2 != 0), array_nums)))

# Use 'filter()' with a lambda function to filter and count the number of even numbers in 'array_nums'
even_ctr = len(list(filter(lambda x: (x % 2 == 0), array_nums)))

# Display the number of even and odd numbers in the original array
print("\nNumber of even numbers in the above array: ", even_ctr)
print("\nNumber of odd numbers in the above array: ", odd_ctr)