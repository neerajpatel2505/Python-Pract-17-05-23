def sum(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum
print(sum(10,20,30,40,50))
print(sum(tuple))

# def sum(*args,x):
#     sum=0
#     for i in args:
#         sum=sum+i
#     sum=sum*x
#     return sum
# print(sum(10,20,30,40,x=50))

# def sum(x,*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     sum=sum*x
#     return sum
# print(sum(10,20,30,40,50))