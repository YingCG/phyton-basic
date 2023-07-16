# everythin is object.
print(type([1, 2, 3]))
print(type(200))
print(type(2.0))


# above all is a class, we can also made our own
class Sample:
    pass


x = Sample()
print(type(x))


# to add attribute and method to the class
class Dog:
    # CLASS OBJECT ATTRIBUTE
    species = "mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


mydog = Dog("Lab", "Sunny")
print((mydog.breed + " - " + mydog.name))

otherdog = Dog(breed="Husky", name="Jimmy")
print((otherdog.breed + " - " + otherdog.name))

print(mydog.species)


class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self, new_r):
        self.radius = new_r


pinkCircle = Circle(3)
print(pinkCircle.radius)

print(pinkCircle.area())

# pinkCircle.radius = 100
# print(pinkCircle.area())
pinkCircle.set_radius(999)
print(pinkCircle.area())
