import string
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

# Using map to encrypt strings
abc = string.ascii_lowercase


def encrypt(input_message, offset):
    return "".join(map(lambda x: abc[(abc.index(x)+offset) % 26] if x in abc else x, input_message))


def decrypt(input_message, offset):
    return "".join(map(lambda x: abc[(abc.index(x)-offset) % 26] if x in abc else x, input_message))


unencrypt_string = "abcd"
encrypt_string = encrypt(unencrypt_string, 1)
print(encrypt_string)
print(decrypt(encrypt_string, 1))





