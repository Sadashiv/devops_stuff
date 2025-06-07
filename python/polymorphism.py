class Animal():
    def __init__(self, name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstracted class")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Bow bow!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} say meow meow"

mudhol = Dog('Mudol Huland')
bubli = Cat('Bubli cat')
print(mudhol.speak())
print(bubli.speak())
myanimal = Animal('Mudhol Huland')
print(myanimal.speak())

