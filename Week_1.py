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
