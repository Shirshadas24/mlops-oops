class employee:
    def __init__(self):  #constructor - dunder /magic /specil method
        print("started executing attributes/data")
        self.id = 123
        self.salary = 10000
        self.designation = "Software Engineer"
        print("attributes/data have been initiated")
    def travel(self,destination):
        print("travel function called amnually")
        print(f"Employee is travelling to {destination}")

sam=employee()
# print(sam.id)
# print(sam.salary)
# print(sam.designation)
sam.travel("Bangalore")