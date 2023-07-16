class Animal:
    def __init__(self):
        print("NEW MEMBER JOINING THE TEAM")

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print("EATING TIME")


rabbit = Animal()
rabbit.whoAmI()
rabbit.eat()


class Horse(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Welcome HORSE to the team")

    def talk(self):
        print("~ neigh...")

    def eat(self):
        print("~~ I enjoying some fresh grass from this new field... ")


Jenny = Horse()
Jenny.whoAmI()
Jenny.eat()
Jenny.talk()


class Book:
    def __init__(self, title, subject, chapter):
        self.title = title
        self.subject = subject
        self.chapter = chapter

    # ToString method --> otherwise it would only return the object a class
    def __str__(self):
        return "Today we are reading: {}, Capter {}".format(self.title, self.chapter)

    # Len --> without the special method will return an error
    def __len__(self):
        return self.chapter

    def __delattr__(self):
        print("Complete this book!")


nightTimeStory = Book("Little princess", "entertainment", 1)
print(nightTimeStory)
print(len(nightTimeStory))
del nightTimeStory
