class User:
    def __init__(self, first_name, last_name, age, gender, address):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.address = address

    def describe_user(self):
        print(f"First name: {self.first_name}\nLast name: {self.last_name}\nAge: {self.age}\nGender: {self.gender}\nAddress: {self.address}.")

    def greet_user1(self):
        print(f"Hello {self.first_name} {self.last_name}!")

    def greet_user2(self):
        print(f"Bella {self.first_name} {self.last_name}!")

    def greet_user3(self):
        print(f"No vabbè, bella {self.first_name} {self.last_name}!")

user1 = User("Luca", "Marchetti", 20, "Male", "Via Maurizio Quadrio 30")
user2 = User("Pierre", "Damien", 21, "Asexual", "Via Efrem Reat")
user3 = User("Lorenzo", "Rossi", 19, "Unknown", "Aranova")


user1.describe_user()
print("-------------------")
user1.greet_user1()
print("\n-------------------")
user2.describe_user()
print("-------------------")
user2.greet_user2()
print("\n-------------------")
user3.describe_user()
print("-------------------")
user3.greet_user3()