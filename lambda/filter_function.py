# the filter function will “filter out” an iterable object based on a specified condition.
# This condition will be decided by the function that we pass in.
# filter(function, iterable)

# list comprehensions can have the same functionality as the built-in map and filter functions.
# The operation applied to each element is similar to the map function,
# and if we add a condition to which elements are added to the list in the list comprehension,
# that’s similar to the filter function.
# Also, the expression that is added in the beginning of a list comprehension is similar to the lambda expression
# that can be used inside the map and filter functions.
# [x**2 for x in range(10) if x%2==0]

num_list = [1, 2, 3, 4, 5, 6]

even_list = filter(lambda element: element % 2 == 0, num_list)
# list comprehension to display each element of the list
[print(x) for x in even_list]

even_list = list(filter(lambda element: element % 2 == 0, num_list))
print(even_list)

