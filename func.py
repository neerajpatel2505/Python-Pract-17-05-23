# a=10 # Global variable
# def display():
#     a=50 # Local variable
#     print(a)
#     print(globals()['a']) # to access global variables with having same name as local variables.
# def display1():
#     print(a)   
# display()
# display1()

# ---------------------------------------------------------------------------------------------

x=30
def display():
    global a
    a=50 # Local variable
    print(a)
    print(globals()['x']) # to access global variables with having same name as local variables.
def display1():
    print(a)   
display()
display1()

# ---------------------------------------------------------------------------------------------

