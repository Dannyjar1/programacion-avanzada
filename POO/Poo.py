class Dog:

    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def __str__(self):
        return "This is a class example dog"

    def spkeak(self, say):
        return f" {self.name}say {say}"


print(Dog)

Chikis = Dog ("Chikis", 3) 
print(Chikis.name)
print(Chikis.age)
print(Chikis.__str__())
print(Chikis.spkeak("Wolf"))



Toby = Dog ("Toby", 3) 
print(Toby.name)
print(Toby.age)
print(Toby.__str__())
print(Chikis.spkeak("Walf"))


