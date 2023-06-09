def sum(input1):
    Sum=0
    for i in input1:
        Sum=Sum+i
    print("Sum=",Sum)
input1 = eval(input("Enter your all numbers:"))
input1 = tuple(input1)
sum(input1)