# Lesson 01 : Python Variables 

# 1. String 
name = 'Hello World!'
print(name)
print(type(name))

# 2. Int
age = 33
print(age)
print(type(age))

# 3. Float 
salary = 20000.22
print(salary)
print(type(salary))

# 4. Boolean 
isActive = True
print(isActive)
print(type(isActive))


# Declaring multiple variables in one line

firstname, lastname, age, country, is_married = 'Abhi', 'Rai', 34, 'India', True

print(firstname, lastname, age, country, is_married)

print('firstname :', firstname)
print('Length of firstname', len(firstname))

a, b, c = 1, 2, 3
print('a, b, c: ', a, b, c)

# Swap two variables without temp variable
a, b = b, c
print('a, b, c: ', a, b, c)


# What happend here
x = y = 10
print('Value of x', x)
print('Value of y', y)

# Casting: Converting one data type to another data type. 
# We use int(), float(), str(), list, set When we do arithmetic operations string 
# numbers should be first converted to int or float otherwise it will return an error. 
# If we concatenate a number with a string, the number should be first converted to a string. 
# We will talk about concatenation in String section.

# int to float 
num_int = 10   #10
print('num_int', num_int)
num_float = float(num_int)
print('num_float',num_float)

# flot to int 
num_float = 1.12
print('num_float', num_float)
num_int = int(num_float)
print('num_int',num_int)

# int to str
num_int = 18
print('num_int', num_int)
num_str = str(num_int)
print('num_str', num_str)


# str to int or float
num_str = '110.6'

num_float = float(num_str)  # Convert the string to a float first
print('num_float', float(num_str))  # 10.6

num_int = int(num_float)    # Then convert the float to an integer
print('num_int', int(num_float)) 



# str to list
first_name = 'Abhi'
print(first_name)               # 'Abhi'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 'b', 'h', 'i']s