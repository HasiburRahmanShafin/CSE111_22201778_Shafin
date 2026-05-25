# LAB-6: Class Methods, Static Methods, and Class Variables

# task-1: Student class with class variable ID and from_String classmethod
class Student:
    ID = 0
    def __init__(self, name, dept, age, cgpa):
        self.name = name
        self.dept = dept
        self.age = age
        self.cg = cgpa
        Student.ID += 1
    def showDetails(self):
        print(f"ID: {Student.ID}")
        print(f"Name: {self.name}\nDepartment: {self.dept}\nAge: {self.age}\nCGPA: {self.cg}")
    @classmethod
    def from_String(cls, data):
        name, dept, age, cg = data.split('-')
        return cls(name, dept, int(age), float(cg))
s1 = Student("Samin", "CSE", 21, 3.91)
s1.showDetails()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.showDetails()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.showDetails()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.showDetails()

# task-2: Assassin class with class methods
class Assassin:
    total = 0
    def __init__(self, name, success_rate):
        self.name = name
        self.srate = success_rate
        Assassin.total += 1
    def printDetails(self):
        print(f"Name: {self.name}\nSuccess rate: {self.srate}%")
        print(f"Total number of Assassin: {Assassin.total}")
    @classmethod
    def failureRate(cls, name, failure):
        return cls(name, 100 - failure)
    @classmethod
    def failurePercentage(cls, name, failure_str):
        return cls(name, 100 - int(failure_str[:-1]))
john_wick = Assassin('John Wick', 100)
john_wick.printDetails()
print('================================')
nagisa = Assassin.failureRate("Nagisa", 20)
nagisa.printDetails()
print('================================')
akabane = Assassin.failurePercentage("Akabane", "10%")
akabane.printDetails()

# task-3: Passenger with class variable count
class Passenger:
    count = 0
    def __init__(self, name):
        self.name = name
        self.fare = 450
        Passenger.count += 1
    def set_bag_weight(self, w):
        if 21 <= w <= 50:
            self.fare += 50
        elif w > 50:
            self.fare += 100
    def printDetail(self):
        print(f"Name: {self.name}\nBus Fare: {self.fare} taka")
print("Total Passenger:", Passenger.count)
p1 = Passenger("Jack")
p1.set_bag_weight(90)
p2 = Passenger("Carol")
p2.set_bag_weight(10)
p3 = Passenger("Mike")
p3.set_bag_weight(25)
print("=========================")
p1.printDetail()
print("=========================")
p2.printDetail()
print("=========================")
p3.printDetail()
print("=========================")
print("Total Passenger:", Passenger.count)

# task-4: Travel class
class Travel:
    count = 0
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
        self.time = 1
        Travel.count += 1
    def set_time(self, t): self.time = t
    def set_source(self, s): self.source = s
    def set_destination(self, d): self.dest = d
    def display_travel_info(self):
        return f"Source: {self.source}\nDestination: {self.dest}\nFlight Time: {self.time}:00"
print("No. of Traveller =", Travel.count)
print("=======================")
t1 = Travel("Dhaka", "India")
print(t1.display_travel_info())
print("=======================")
t2 = Travel("Kuala Lampur", "Dhaka")
t2.set_time(23)
print(t2.display_travel_info())
print("=======================")
t3 = Travel("Dhaka", "New_Zealand")
t3.set_time(15)
t3.set_destination("Germany")
print(t3.display_travel_info())
print("=======================")
t4 = Travel("Dhaka", "India")
t4.set_time(9)
t4.set_source("Malaysia")
t4.set_destination("Canada")
print(t4.display_travel_info())
print("=======================")
print("No. of Traveller =", Travel.count)

# task-5: Employee with classmethod and staticmethod
class Employee:
    def __init__(self, name, period):
        self.name = name
        self.workingPeriod = period
    @classmethod
    def employeeByJoiningYear(cls, name, year):
        return cls(name, 2023 - year)
    @staticmethod
    def experienceCheck(exp, gender):
        pronoun = "He" if gender == "male" else "She"
        if exp < 3:
            return f"{pronoun} is not experienced"
        return f"{pronoun} is experienced"
employee1 = Employee('Dororo', 3)
employee2 = Employee.employeeByJoiningYear('Harry', 2016)
print(employee1.workingPeriod)
print(employee2.workingPeriod)
print(employee1.name)
print(employee2.name)
print(Employee.experienceCheck(2, "male"))
print(Employee.experienceCheck(3, "female"))

# task-6: Laptop with static and class methods
class Laptop:
    laptopCount = 0
    def __init__(self, name, count):
        self.name = name
        self.count = count
        Laptop.laptopCount += count
    @staticmethod
    def advantage():
        print("Laptops are portable")
    @classmethod
    def resetCount(cls):
        cls.laptopCount = 0
lenovo = Laptop("Lenovo", 5)
dell = Laptop("Dell", 7)
print(lenovo.name, lenovo.count)
print(dell.name, dell.count)
print("Total number of Laptops", Laptop.laptopCount)
Laptop.advantage()
Laptop.resetCount()
print("Total number of Laptops", Laptop.laptopCount)

# task-7: Cat class with multiple constructors
class Cat:
    Number_of_cats = 0
    def __init__(self, color, action):
        self.color = color
        self.action = action
        Cat.Number_of_cats += 1
    @classmethod
    def no_parameter(cls):
        return cls("White", "sitting")
    @classmethod
    def first_parameter(cls, color):
        return cls(color, "sitting")
    @classmethod
    def second_parameter(cls, action):
        return cls("Grey", action)
    def changeColor(self, new_color):
        self.color = new_color
    def printCat(self):
        print(f"{self.color} cat is {self.action}")
print("Total number of cats:", Cat.Number_of_cats)
c1 = Cat.no_parameter()
c2 = Cat.first_parameter("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c5 = Cat.second_parameter("playing")
print("=======================")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c5.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()
print("=======================")
print("Total number of cats:", Cat.Number_of_cats)

# task-8: Cylinder class with class/static methods
import math
class Cylinder:
    radius = 5
    height = 18
    def __init__(self, r, h):
        print(f"Default radius={Cylinder.radius} and height={Cylinder.height}.")
        Cylinder.radius = r
        Cylinder.height = h
        print(f"Updated: radius={Cylinder.radius} and height={Cylinder.height}.")
    @classmethod
    def swap(cls, a, b):
        return cls(b, a)
    @classmethod
    def changeFormat(cls, data):
        r, h = map(float, data.split('-'))
        return cls(r, h)
    @staticmethod
    def area(r, h):
        print("Area:", 2 * math.pi * r**2 + 2 * math.pi * r * h)
    @staticmethod
    def volume(r, h):
        print("Volume:", math.pi * r**2 * h)
c1 = Cylinder(0, 0)
Cylinder.area(c1.radius, c1.height)
Cylinder.volume(c1.radius, c1.height)
print("===============================")
c2 = Cylinder.swap(8, 3)
c2.area(c2.radius, c2.height)
c2.volume(c2.radius, c2.height)
print("===============================")
c3 = Cylinder.changeFormat("7-13")
c3.area(c3.radius, c3.height)
c3.volume(c3.radius, c3.height)
print("===============================")
Cylinder(0.3, 5.56).area(Cylinder.radius, Cylinder.height)
print("===============================")
Cylinder(3, 5).volume(Cylinder.radius, Cylinder.height)

# task-9: Student with BRAC/other counters
class Student:
    total = 0
    brac = 0
    other = 0
    def __init__(self, name, dept, inst="BRAC University"):
        self.name = name
        self.dept = dept
        self.inst = inst
        Student.total += 1
        if inst == "BRAC University":
            Student.brac += 1
        else:
            Student.other += 1
    def individualDetail(self):
        print(f"Name: {self.name}\nDepartment: {self.dept}\nInstitution: {self.inst}")
    @classmethod
    def createStudent(cls, name, dept, inst="BRAC University"):
        return cls(name, dept, inst)
    @classmethod
    def printDetails(cls):
        print(f"Total Student(s): {cls.total}")
        print(f"BRAC University Student(s): {cls.brac}")
        print(f"Other Institution Student(s): {cls.other}")
Student.printDetails()
print('#########################')
mikasa = Student('Mikasa Ackerman', "CSE")
mikasa.individualDetail()
print('------------------------------------------')
Student.printDetails()
print('========================')
harry = Student.createStudent('Harry Potter', "Defence Against Dark Arts", "Hogwarts School")
harry.individualDetail()
print('-------------------------------------------')
Student.printDetails()
print('=========================')
levi = Student.createStudent("Levi Ackerman", "CSE")
levi.individualDetail()
print('--------------------------------------------')
Student.printDetails()

# task-10: SultansDine class
class SultansDine:
    total_branch = 0
    total_sell = 0
    branches = []
    def __init__(self, name):
        self.name = name
        SultansDine.branches.append(self)
        SultansDine.total_branch += 1
    def sellQuantity(self, qty):
        if qty < 10:
            self.sell = qty * 300
        elif qty < 20:
            self.sell = qty * 350
        else:
            self.sell = qty * 400
        SultansDine.total_sell += self.sell
    def branchInformation(self):
        print(f"Branch Name: {self.name}\nBranch Sell: {self.sell} Taka")
    @classmethod
    def details(cls):
        print(f"Total Number of branch(s): {cls.total_branch}")
        print(f"Total Sell: {cls.total_sell} Taka")
        for br in cls.branches:
            print(f"Branch Name: {br.name}, Branch Sell: {br.sell} Taka ")
            print(f"Branch consists of total sell's: {round((br.sell/cls.total_sell)*100, 2)}%")
SultansDine.details()
print('########################')
dhanmondi = SultansDine('Dhanmondi')
dhanmondi.sellQuantity(25)
dhanmondi.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()

# task-11: Puzzle class tracing
class Puzzle:
    x = 0
    def methodA(self):
        Puzzle.x = 5
        z = Puzzle.x + self.methodB(Puzzle.x)
        print(Puzzle.x, z)
        z = self.methodB(z + 2) + Puzzle.x
        print(Puzzle.x, z)
        self.methodB(Puzzle.x, z)
        print(Puzzle.x, z)
    def methodB(self, *args):
        if len(args) == 1:
            y = args[0]
            Puzzle.x = y + Puzzle.x
            print(Puzzle.x, y)
            return Puzzle.x + 3
        else:
            z, x = args
            z = z + 1
            x = x + 1
            print(z, x)
p = Puzzle()
p.methodA()
p.methodA()
p = Puzzle()
p.methodA()
p.methodB(7)

# task-12: FinalT6A tracing
class FinalT6A:
    temp = 3
    def __init__(self, x, p):
        self.sum, self.y = 0, 2
        FinalT6A.temp += 3
        self.y = self.temp - p
        self.sum = self.temp + x
        print(x, self.y, self.sum)
    def methodA(self):
        x, y = 0, 0
        y = y + self.y
        x = self.y + 2 + self.temp
        self.sum = x + y + self.methodB(self.temp, y)
        print(x, y, self.sum)
    def methodB(self, temp, n):
        x = 0
        FinalT6A.temp += 1
        self.y = self.y + (FinalT6A.temp)
        FinalT6A.temp -= 1
        x = x + 2 + n
        self.sum = self.sum + x + self.y
        print(x, self.y, self.sum)
        return self.sum
q1 = FinalT6A(2,1)
q1.methodA()
q1.methodA()

# task-13: Classes A and B tracing
class A:
    temp = 4
    def __init__(self):
        self.y = self.temp - 2
        self.sum = self.temp + 1
        A.temp -= 2
        self.methodA(3, 4)
    def methodA(self, m, n):
        x = 0
        self.y = self.y + m + (self.temp)
        A.temp += 1
        x = x + 1 + n
        self.sum = self.sum + x + self.y
        print(x, self.y, self.sum)
class B:
    x = 0
    def __init__(self, b=None):
        self.y, self.temp, self.sum = 5, -5, 2
        if b is None:
            self.y = self.temp + 3
            self.sum = 3 + self.temp + 2
            self.temp -= 2
        else:
            self.sum = b.sum
            B.x = b.x
            b.methodB(2, 3)
    def methodA(self, m, n):
        x = 2
        self.y = self.y + m + (self.temp)
        self.temp += 1
        x = x + 5 + n
        self.sum = self.sum + x + self.y
        print(x, self.y, self.sum)
    def methodB(self, m, n):
        y = 0
        y = y + self.y
        B.x = self.y + 2 + self.temp
        self.methodA(self.x, y)
        self.sum = self.x + y + self.sum
        print(self.x, y, self.sum)
a1 = A()
b1 = B()
b2 = B(b1)
b1.methodA(1,2)
b2.methodB(3,2)

# task-14: Quiz3 class tracing
class msgClass:
    def __init__(self):
        self.content = 0
class Quiz3:
    x = 0
    def __init__(self, k=None):
        self.sum, self.y = 0, 0
        if k is None:
            self.sum = 5
            Quiz3.x = 2
            self.y = 2
        else:
            self.sum = self.sum + k
            self.y = 3
            Quiz3.x += 2
    def methodA(self):
        x = 1
        y = 1
        msg = [None]
        myMsg = msgClass()
        myMsg.content = Quiz3.x
        msg[0] = myMsg
        msg[0].content = self.y + myMsg.content
        self.y = self.y + self.methodB(msg[0])
        y = self.methodB(msg[0]) + self.y
        x = y + self.methodB(msg, msg[0])
        self.sum = x + y + msg[0].content
        print(x, y, self.sum)
    def methodB(self, *args):
        if len(args) == 2:
            mg2, mg1 = args
            x = 2
            self.y = self.y + mg2[0].content
            mg2[0].content = self.y + mg1.content
            x = x + 2 + mg1.content
            self.sum = self.sum + x + self.y
            mg1.content = self.sum - mg2[0].content
            print(Quiz3.x, self.y, self.sum)
            return self.sum
        elif len(args) == 1:
            mg1 = args[0]
            x = 1
            y = 2
            y = self.sum + mg1.content
            self.y = y + mg1.content
            x = Quiz3.x + 5 + mg1.content
            self.sum = self.sum + x + y
            Quiz3.x = mg1.content + x + 3
            print(x, y, self.sum)
            return y
a1 = Quiz3()
a2 = Quiz3(5)
msg = msgClass()
a1.methodA()
a2.methodB(msg)

# Extra: Passenger class (repeated from earlier, but kept as is)
class Passenger:
    count = 0
    def __init__(self, name):
        self.name = name
        self.fare = 450
        Passenger.count += 1
    def set_bag_weight(self, w):
        if 21 <= w <= 50:
            self.fare += 50
        elif w > 50:
            self.fare += 100
    def printDetail(self):
        print("Name:", self.name)
        print("Bus Fare:", self.fare)
print("Total Passenger:", Passenger.count)
p1 = Passenger("Jack")
p1.set_bag_weight(90)
p2 = Passenger("Carol")
p2.set_bag_weight(10)
p3 = Passenger("Mike")
p3.set_bag_weight(25)
p1.printDetail()
print("ニニニニニニニニニニニニ")
p2.printDetail()
p3.printDetail()
print("================")
print("Total Passenger:", Passenger.count)
