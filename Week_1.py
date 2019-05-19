'''
Python Basics 
  - is a high level language, which means it's optimized for reading by people instead of machines. 
  - is interpreted, meaning it doesn't compile to machine-level code for it to run. 
  - is dynamically-typed, meaning you do not need to declare the type of variable. 
  - because there is no compilation step, Python can be used interactively. 
  
Python Functions 
  - all of the optional parameters, the ones that you got default values for, need to come at the end of the function declaration. 
  - you can assign a variable to a function
'''
def add_numbers(x, y, z=None, flag=False):
    if (flag):
        print('Flag is true!')
    if (z==None):
        return x + y
    else:
        return x + y + z
    
print(add_numbers(1, 2, flag=True))
