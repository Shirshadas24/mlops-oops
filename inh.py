class Grandparent:
    def __init__(self, name):
        self.name = name

    def show1(self):
        print('Grandparent:', self.name)
class Parent(Grandparent):
    

    def show2(self):
        print('Parent:', self.name)
class Child(Parent):
  

    def show3(self):
        print('Child:', self.name)
obj = Child('Child')
obj.show1()
obj.show2()
obj.show3()