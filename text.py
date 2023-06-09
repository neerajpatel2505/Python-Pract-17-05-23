class A:
    def _xyz(self):
        print("Hiiii")
        
class B():
    def xyz(self):
        print("Access in another class")
        obj1=A()
        obj1._xyz()
        
obj2=B()
obj2.xyz