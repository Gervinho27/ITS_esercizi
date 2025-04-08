# 1. Write a class called Student with the attributes name(str) and studyProgram(str)

class Student:
    def __init__(self, name, studyProgram):
        self.name = name
        self.studyProgram = studyProgram

# 2. Create three instances. One for yourself, one for your left neighbour and one for our right neighbour.

me = Student("Luca", "Programmatore")
left_neighbour = Student("Pierre", "Osu proPlayer")
right_neighbour = Student("Lorenzo", "Producer")

# 3. Add a method printInfo that prints the name and studyProgram of a Student. Test your method on the objects!

class Student:
    def __init__(self, name, studyProgram):
        self.name = name
        self.studyProgram = studyProgram

    def printInfo(self):
        print(f"Name: {self.name}\nStudy Program: {self.studyProgram}")

me = Student("Luca", "Programmatore")
left_neighbour = Student("Pierre", "Osu proPlayer")
right_neighbour = Student("Lorenzo", "Producer")

me.printInfo()
left_neighbour.printInfo()
right_neighbour.printInfo()

# 4. Modify the code and add age and gender to the attributes. Modify you printing methods respectively too.

class Student:
    def __init__(self, name, studyProgram, age, gender):
        self.name = name
        self.studyProgram = studyProgram
        self.age = age
        self.gender = gender
    
    def printInfo(self):
        print(f"Name: {self.name}\nStudy Program: {self.studyProgram}\nAge: {self.age}\nGender: {self.gender}")
        print("-------------------")

me = Student("Luca", "Programmatore", 20, "Male")
left_neighbour = Student("Pierre", "Osu proPlayer", 21, "Asexual")
right_neighbour = Student("Lorenzo", "Producer", 19, "Unknown")

me.printInfo()
left_neighbour.printInfo()
right_neighbour.printInfo()
