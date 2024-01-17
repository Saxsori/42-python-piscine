def ft_filter(function, iterable):
    """
    Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None,
    return the items that are true.
    """
    if function is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function(item)]

# List comprehension in python is provide a concise way to create lists.
# Allow you to create a list by applying an expression to each item in an iterable.
# [expression for item in iterable if condition]
# it is a syntactic sugar for the following code:
# for item in iterable:
#     if condition:
#         expression
# The expression is optional and can be omitted.
# The condition is also optional and can be omitted.
# The iterable can be any iterable object, like a list, tuple, set etc.
# The condition can be any expression that returns a boolean value.
# The expression can be anything, meaning you can put in all kinds of objects in lists.
# The expression and condition can also be omitted, passing only the iterable.
# Example:
# >>> [i for i in range(10) if i % 2 == 0]
# [0, 2, 4, 6, 8]
# >>> [i if i % 2 == 0 else 10 for i in range(10)]
# [0, 10, 2, 10, 4, 10, 6, 10, 8, 10]
# >>> [i for i in range(10)]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> [i for i in range(10) if i % 2 == 0 if i % 3 == 0]
# [0, 6]
# >>> [i for i in range(10) if i % 2 == 0 and i % 3 == 0]
# [0, 6]
# >>> [i for i in range(10) if i % 2 == 0 or i % 3 == 0]
# [0, 2, 3, 4, 6, 8, 9]
# >>> [i for i in range(10) if i % 2 == 0 or i % 3 == 0 if i % 4 == 0]
# [0, 4, 8]
# >>> [i for i in range(10) if i % 2 == 0 if i % 3 == 0 if i % 4 == 0]
# [0]
# 