class Animal:
    def __init__(self):
        self.name = "julia"
        # self.__name = name
    def speak(self):
        print(f"{self.name} says something")

class Dog(Animal):
    # def __init__(self):
    #     self.behaviour = "good dog"
    def __init__(self, breed):
        super().__init__()
        self.breed = breed

    def speak(self):
        super().speak()
        print(f"{self.name} barks.{self.breed} is a good dog")
# animal=Animal("Animal")
# animal.speak()
dog=Dog("alsatian")
dog.speak()
