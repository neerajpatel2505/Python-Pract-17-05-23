# def display(dict):
#     for k,v in dict.keys(),dict.values():
#         print(k,"=",v)
# input = eval(input("Enter your dict"))
# dict = dict(input)
# print(dict)
# print(type(dict))
# display(dict)


# def display(dict):
#     sum=0
#     for v in dict.values():
#         sum=sum+v
#     print("Sum=",sum)
# input = eval(input("Enter your dict"))
# dict = dict(input)
# print(dict)
# print(type(dict))
# display(dict)

# dict={'name':'Neeraj','age':35,'city':'Bhopal'}
# dict['name'] = 'neeraj'
# print(dict['name'])
# print(dict['age'])
# print(dict['city'])
# dict.update({'name':'Neeraj'})
# print(dict)


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for k,v in myfamily.items():
    print(v['name'])

