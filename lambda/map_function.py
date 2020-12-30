# the map function provides us a way to apply a function to each element in an iterable object,
# such as lists, strings, tuples, etc…
# Thus, the map function takes in two arguments: the function we want to apply,
# and the iterable object we want to apply it to.
# map(function, iterable)

num_list = [1, 2, 3, 4, 5]
# The map function will return a map object, which is an iterator.
# If we want to create a list from this map object,
# we would need to pass in our map object to the built-in list function.
squared_list = list(map(lambda x: x**2, num_list))
print(squared_list)
