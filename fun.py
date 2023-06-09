def add(x,y):
    sum=x+y
    return sum

def sub(x,y):
    sub=x-y
    return sub

def multi(x,y):
    multi=x*y
    return multi

x=int(input("Enter first no:"))
y=int(input("Enter second no:"))

Sum=add(x,y)
print("Sum:",Sum)

Sub=sub(x,y)
print("Sub:",Sub)

Multi=multi(x,y)
print("Multi:",Multi)