# the reduce function is taking an iterable, such as a list, and reduces it down to a single cumulative value.
# The reduce function can take in three arguments, two of which are required.
# The two required arguments are: a function (that itself takes in two arguments),
# and an iterable (such as a list). The third argument, which is an initializer, is optional.
# reduce(function, iterable[, initializer])

from functools import reduce

num_list = [1, 2, 3, 4, 5, 6]

# In other words, the x argument gets updated with the accumulated value,
# and the y argument gets updated from the iterable.
# Mathematically, you can think of reduce as doing the following:
# f(f(f(f(f(x,y),y),y),y),y)
sum_list = reduce(lambda x, y: x + y, num_list)
print(sum_list)

sum_odd_list = reduce(lambda x, y: x + y, filter(lambda num: num % 2 != 0, num_list))
print(sum_odd_list)