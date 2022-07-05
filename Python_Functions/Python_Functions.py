# Notes from Corey Schafer's Python Course
# https://www.youtube.com/c/Coreyms
# Functions

def hello_func():
    pass  # allows you to leave the function blank until a later date

hello_func()
# Output
# Nothing provided 

def hello_func2():
    print("Hello Function 2")

hello_func2()

# Output
# Hello Function 2

def hello_func3():
    return ("Hello function 3")

print(hello_func3())
# output
# Hello function 3

def hello_func4():
    return ("Hello function 4")

print(hello_func4().upper())
# output
# HELLO FUNCTION 4

def hello_func5(greeting):
    return '{} Function.'.format(greeting) # limited to scope to function
        
print(hello_func5('Hi'))
# output
# Hi Function.

def hello_func6(greeting, name='You'): # default value of you, if a name is not passed
    return '{}, {}'.format(greeting, name)

print(hello_func6('Hi', 'Joe'))

# output
# Hi, Joe

def student_info(*args, **kwargs): # accept any number of arguments, names dont have to be args and kwargs
    print(args) #tuple
    print(kwargs) # dic

student_info('Math', 'Art', name='John', age = 22)

# output
#('Math', 'Art')
# {'name': 'John', 'age': 22}

def student_info2(*args, **kwargs): 
    print(args)
    print(kwargs)

courses = ['Math', 'Art'] # list
info = {'name': 'John', 'age': 22}

student_info2(*courses, **info) #* unpacks values coming from list and dict
# output
# ('Math', 'Art')
# {'name': 'John', 'age': 22

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

#year 2017
# month 2
def days_in_month(year, month):
    if not 1 <= month <=12: # 2 is between 1 and 12, so this does not return
        return 'Invalid Month'
    if month == 2 and is_leap(year): # month = 2 true, but is_leap(year) returns false, so does not return
        return 29
    return month_days[month] # the month is 2, which goes to index 2 on month_days index

print(is_leap(2017))
# output
# false
print(is_leap(2020))
# output
# true
print(days_in_month(2017, 2))
# output
# 28

