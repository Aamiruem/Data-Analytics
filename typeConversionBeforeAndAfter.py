# This code demonstrates type conversion before and after using the input() function in Python.


# before type conversion
x = input()
print(type(x))  # This will print <class 'str'> since input() returns a string


# after type conversion
x = int(x)
print(type(x))  # This will print <class 'int'> since we converted the string to an integer
