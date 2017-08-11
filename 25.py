
class Person:
    name ="Person"

    def __init__(self,n="unknown"):  # default value
        self.name = n


print(Person.name)

ram = Person("Ram")

print(ram.name)

rock = Person()

print(rock.name)