class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

Alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

# 1. Copy the code and print the age of bob (using the dot notation)

print(bob.age)

# 2. Create an if-statement that prints the name of the oldest person of the two persons

if Alice.age > bob.age:
    print(Alice.name + " is the oldest!")
else:
    print(bob.name)

# 3. Create three other Persons. Make a list called 'people' with all 5 Person.

Pierre = Person("Pierre", 20)

Lorenzo = Person("Lorenzo", 19)

Popa = Person("Popa", 69)

person = [Alice, bob, Pierre, Lorenzo, Popa]

# 4. Make a loop that find and prints the youngest person's name.

youngest = person[0]
for p in person:
    if p.age < youngest.age:
        youngest = p
print(youngest.name + " is the youngest!")