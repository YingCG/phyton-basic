import first_module

# result = first_module.enterNumber()

# print(f"The number you have enter: {result}")
print("Second Module's Name:{}".format(__name__))

first_module.main()
print("First Module's Name:{}".format(first_module.__name__))
