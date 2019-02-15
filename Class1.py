import sys

#def ClassOne:


class Myclass:
     x = "joe"
     y = "Kipchumba"
     z = "Birech"

p1 = Myclass()
print(p1.z)



class Studentinfo:
    def __init__(self, name, age, height, race, gender):
        self.name = name
        self.age= age
        self.height = height
        self.race = race
        self.gender = gender

    def myf(self):
        print ("Student's name is: " + self.name)


p1 = Studentinfo("Prince Joe", 21, 5.8, "black", "male")
#print(p1.age)
#print(p1.race)
p1.myf()

mytuple = ("banana", "republic", "kame", "wewe")

for x in mytuple:
    print (x)

class Nmbers:
    def __iter__(self):
        self.a = 1
        return (self)
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = Nmbers()
myiter = iter(myclass)

print(next(myiter))
