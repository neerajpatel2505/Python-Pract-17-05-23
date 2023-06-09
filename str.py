class A:
   def _xyz(self):
      print("Hello...")
      
class B:
   def abc(self):
      print("Hi....")
      obj1=A()
      obj1._xyz()

# obj=A()
# obj._xyz()

obj2=B()
obj2.abc()