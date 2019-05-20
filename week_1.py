'''
Python Basics 
  - is a high level language, which means it's optimized for reading by people instead of machines. 
  - is interpreted, meaning it doesn't compile to machine-level code for it to run. 
  - is dynamically-typed, meaning you do not need to declare the type of variable. 
  - because there is no compilation step, Python can be used interactively. 
  
Python Functions 
  - all of the optional parameters, the ones that you got default values for, need to come at the end of the function declaration. 
  - you can assign a variable to a function
  
Python Strings 
  - Python strings are unicode-based in Python 3 (suppots over a million diff characters). 
    In Python 2, string are ASCII-based (1-256 different latin chars + 0-9 numericals). 
    The transition to unicode was due to a need to support non-latin chars + mathematical operators as well. 
  - String manipulation is important for data cleaning...relevant functions are format and string. 
  
Python Dates and Times
  - The date time object has handy attributes to get the representative hour, day, seconds, etc.
  - You might want to look for any five day span of time where sales were highest, and flag that for follow up --> where datetime's time deltas come into use.

Python Objects + map()
  - classes are generally named using camel case, which means the first character of each word is capitalized.
  - objects in Python do not have private or protected members. If you instantiate an object, you have full access to any of the methods or attributes of that object.
  - Functional programming is a programming paradigm in which you explicitly declare all parameters which could change through execution of a given function. 
    Thus functional programming is referred to as being side-effect free, because there is a software contract that describes what can actually change by calling a function.
    With the functional approach, we use expressions (such as map) to transform the data. 
    We are expressing what we want done, not how to do it. 
    
Python Lambdas and List comprehension
  - python lambdas are anonymous functions. In other words, they are functions with no name, are single expressions, and are meant to be very simple.
  - list comprehension: list comprehension by pulling the iteration on one line
'''
#####Python Functions#######
def add_numbers(x, y, z=None, flag=False):
    if (flag):
        print('Flag is true!')
    if (z==None):
        return x + y
    else:
        return x + y + z
    
print(add_numbers(1, 2, flag=True))

#####Python Strings#######

print('Chris' + str(2))


sales_record = {
'price': 3.24,
'num_items': 4,
'person': 'Chris'}

sales_statement = '{} bought {} item(s) at a price of {} each for a total of {}'

print(sales_statement.format(sales_record['person'],
                             sales_record['num_items'],
                             sales_record['price'],
                             sales_record['num_items']*sales_record['price']))

#####Python Dates and Times#######
import datetime as dt
import time as tm

#time returns the current time in seconds since the Epoch. (January 1st, 1970)
tm.time()
#1558311511.450097


#Convert the timestamp to datetime.
dtnow = dt.datetime.fromtimestamp(tm.time()) #dt.datetime is a class that combines both a date and a time 
dtnow
#datetime.datetime(2019, 5, 20, 0, 32, 4, 74276)


dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second # get year, month, day, etc.from a datetime
#(2019, 5, 20, 0, 32, 4)

delta = dt.timedelta(days = 100) # create a timedelta of 100 days
delta
#datetime.timedelta(100)

today = dt.date.today() #datetime.date class gives a naive representation of date in year, month, day form 
today - delta # the date 100 days ago
#datetime.date(2019, 2, 9)

today > today-delta # compare dates
#True 


######Examples of map()###########
#idea of map: map(some function, iterable1, iterable2,...) 

#list comprehension 
#create all possible ids where it's of the form 'charchardigitdigit'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

correct_answer = [a+b+c+d for a in lowercase for b in lowercase for c in digits for d in digits]

correct_answer[:50] # Display first 50 ids
