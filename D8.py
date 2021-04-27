print("\nThis is the first excesice about functions")

name = input("yout name please: ")
location = input("Where do you live?  ")

def greet(name, location):
    print(f'Hello {name}')
    print(f"Some friend told me that you are from {location} , rigth?")
    # print("xd")

greet(location = location, name = name  ) # <------  KEYWORD Argumens
