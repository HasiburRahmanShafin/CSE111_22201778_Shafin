# LAB-5: Encapsulation and Class Relationships

# Task1: Circle class with private radius
import math
class Circle:
    def __init__(self, r):
        self.__r = r
    def getRadius(self):
        return self.__r
    def area(self):
        return math.pi * self.__r ** 2
c1 = Circle(4)
print("First circle radius:", c1.getRadius())
print("First circle area:", c1.area())
c2 = Circle(5)
print("Second circle radius:", c2.getRadius())
print("Second circle area:", c2.area())
c3 = Circle(9)
print("Third circle radius:", c3.getRadius())
print("Third circle area:", c3.area())

# Task2: Triangle class
class Triangle:
    def __init__(self, base, height):
        self.__b = base
        self.__h = height
    def getBase(self): return self.__b
    def getHeight(self): return self.__h
    def area(self): return 0.5 * self.__b * self.__h
t1 = Triangle(10, 5)
print("First Triangle Base:", t1.getBase())
print("First Triangle Height:", t1.getHeight())
print("First Triangle area:", t1.area())
t2 = Triangle(5, 3)
print("Second Triangle Base:", t2.getBase())
print("Second Triangle Height:", t2.getHeight())
print("Second Triangle area:", t2.area())
t3 = Triangle(5, 2)
print("Third Triangle Base:", t3.getBase())
print("Third Triangle Height:", t3.getHeight())
print("Third Triangle area:", t3.area())

# Task3: Teacher and Course classes
class Teacher:
    def __init__(self, name, dept):
        self.__name = name
        self.__dept = dept
        self.__courses = []
    def addCourse(self, course):
        self.__courses.append(course.name)
    def printDetail(self):
        print("====================================")
        print(f"Name: {self.__name}\nDepartment: {self.__dept}\nList of courses")
        print("====================================")
        for c in self.__courses:
            print(c)
        print("====================================")
class Course:
    def __init__(self, name):
        self.name = name
t1 = Teacher("Saad Abdullah", "CSE")
t2 = Teacher("Mumit Khan", "CSE")
t3 = Teacher("Sadia Kazi", "CSE")
c1 = Course("CSE 110 Programming Language I")
c2 = Course("CSE 111 Programming Language-II")
c3 = Course("CSE 220 Data Structures")
c4 = Course("CSE 221 Algorithms")
c5 = Course("CSE 230 Discrete Mathematics")
c6 = Course("CSE 310 Object Oriented Programming")
c7 = Course("CSE 320 Data Communications")
c8 = Course("CSE 340 Computer Architecture")
t1.addCourse(c1); t1.addCourse(c2)
t2.addCourse(c3); t2.addCourse(c4); t2.addCourse(c5)
t3.addCourse(c6); t3.addCourse(c7); t3.addCourse(c8)
t1.printDetail()
t2.printDetail()
t3.printDetail()

# Task4: Team and Player classes
class Team:
    def __init__(self, name=""):
        self.__name = name
        self.__players = []
    def setName(self, name):
        self.__name = name
    def addPlayer(self, player):
        self.__players.append(player.name)
    def printDetail(self):
        print("=====================")
        print(f"Team: {self.__name}\nList of Players:\n{self.__players}")
        print("=====================")
class Player:
    def __init__(self, name):
        self.name = name
b = Team()
b.setName('Bangladesh')
mashrafi = Player("Mashrafi")
b.addPlayer(mashrafi)
tamim = Player("Tamim")
b.addPlayer(tamim)
b.printDetail()
a = Team("Australia")
ponting = Player("Ponting")
a.addPlayer(ponting)
lee = Player("Lee")
a.addPlayer(lee)
a.printDetail()

# Task5: Student and USIS classes
class Student:
    def __init__(self, name, sid, dept):
        self.__name = name
        self.__id = sid
        self.__dept = dept
        self.__courses = []
        self.email = None
        self.password = None
        print("Student object is created!")
    def getName(self): return self.__name
    def getId(self): return self.__id
    def getDepartment(self): return self.__dept
    def setCourse(self, course): self.__courses.append(course)
    def getCourse(self): return self.__courses
class Usis:
    def __init__(self):
        self.__logged_in = None
        print("USIS is ready to use!")
    def login(self, student):
        if student.email is None and student.password is None:
            print("Email and password need to be set.")
        else:
            self.__logged_in = student
            print("Login successful!")
    def advising(self, student, *courses):
        if self.__logged_in is None:
            print("Please login to advise courses!")
        elif len(courses) == 0:
            print("You haven't selected any courses.")
        elif len(courses) > 3:
            print("You need special approval to take more than 3 courses.")
        else:
            print("Advising successful!")
            for c in courses:
                student.setCourse(c)
    def individualDetails(self, student):
        return f"Name: {student.getName()}\nID: {student.getId()}\nDepartment: {student.getDepartment()}\nAdvised course: {', '.join(student.getCourse())}"
rakib = Student("Rakib", 12301455, "CSE")
print("1***********************")
usis_obj = Usis()
print("2***********************")
usis_obj.login(rakib)
print("3***********************")
usis_obj.advising(rakib)
print("4***********************")
rakib.email = "rakib@hotmail.com"
rakib.password = "1234"
print("5***********************")
usis_obj.login(rakib)
print("6***********************")
usis_obj.advising(rakib)
print("7***********************")
usis_obj.advising(rakib, "CSE110", "PHY111", "MAT110", "CSE260")
print("8***********************")
usis_obj.advising(rakib, "CSE110", "PHY111", "MAT110")
print("9***********************")
print(usis_obj.individualDetails(rakib))

# Task6: Passenger and Train classes
class Passenger:
    def __init__(self, name, start="", end=""):
        self.name = name
        self.start = start
        self.end = end
class Train:
    def __init__(self, name, *route):
        self.name = name
        self.route = route
        self.passengers = []
        print(f"Welcome aboard on {name}")
        print(f"Start: {route[0]}")
        print(f"Destination: {route[-1]}")
    def addPassenger(self, *passengers):
        for p in passengers:
            print(f"{p.name} welcome aboard")
            self.passengers.append(p)
            if p.start == "":
                p.start, p.end = self.route[0], self.route[-1]
            elif p.end == "":
                p.end = self.route[-1]
            start_idx = self.route.index(p.start)
            end_idx = self.route.index(p.end)
            p.fare = 100 * (end_idx - start_idx)
    def allPassengerDetails(self):
        for p in self.passengers:
            print(f"Name: {p.name},Start: {p.start},Destination: {p.end},Fair: ${p.fare}")
t1 = Train('T1-Express','New York','Manhattan','Brooklyn','Boston')
print("1=========================")
p1 = Passenger("Naruto")
t1.addPassenger(p1)
p2 = Passenger("Sasuke","Manhattan")
p3 = Passenger("Hinata","Manhattan","Brooklyn")
print("2=========================")
t1.addPassenger(p2,p3)
print("3=========================")
t1.allPassengerDetails()
print("4=========================")
t2 = Train('Europe-Express','London','Paris','Brussels','Turkey')
print("5=========================")
p4 = Passenger("Max","London","Brussels")
p5 = Passenger("Eleven","Paris")
p6 = Passenger("Mike","Brussels")
t2.addPassenger(p4,p5,p6)
print("6=========================")
t2.allPassengerDetails()

# Task7: BracuStudent and BracuBus classes
class BracuStudent:
    def __init__(self, name, home):
        self.name = name
        self.home = home
        self.pass_holder = False
    def show_details(self):
        print(f"Student Name: {self.name}\nLives in {self.home}\nHave Bus Pass? {self.pass_holder}")
    def get_pass(self):
        self.pass_holder = True
class BracuBus:
    def __init__(self, route, max_capacity=2):
        self.route = route
        self.max = max_capacity
        self.passengers = []
    def show_details(self):
        print(f"Bus Route: {self.route}")
        print(f"Passengers Count: {len(self.passengers)} (Max: {self.max})")
        print("Passengers On Board:", self.passengers)
    def board(self, *students):
        if not students:
            print("No passenger!")
        for s in students:
            if not s.pass_holder:
                print("You don't have bus pass!")
            elif s.home != self.route:
                print("You got on wrong bus!")
            elif len(self.passengers) >= self.max:
                print("Bus is full!")
            else:
                self.passengers.append(s.name)
                print(f"{s.name} boarded the bus.")
st1 = BracuStudent("Afif", "Mirpur")
st2 = BracuStudent("Shanto", "Motijheel")
st3 = BracuStudent("Taskin", "Mirpur")
st1.show_details()
st2.show_details()
st3.show_details()
bus1 = BracuBus("Mirpur")
bus2 = BracuBus("Azimpur", 5)
bus1.show_details()
bus2.show_details()
st2.get_pass()
st3.get_pass()
st2.show_details()
st3.show_details()
bus1.board()
bus1.board(st1, st2)
st1.get_pass()
st2.home = "Mirpur"
st1.show_details()
st2.show_details()
bus1.board(st1, st2, st3)
bus1.show_details()

# Task8: Library and Reader classes
class Library:
    def __init__(self, name, books):
        self.name = name
        self.books = books
        self.borrowers = {}
    def details(self):
        print(f"{self.name} Library details")
        print(f"Borrower details:\n{self.borrowers}")
        print(f"Books availability:\n{self.books}")
class Reader:
    def __init__(self, name):
        self.name = name
        self.borrowed = {}
        self.total_books = 0
    def borrow(self, library, *books):
        for b in books:
            if self.total_books >= 5:
                print("You cannot borrow more than 5 books.")
            elif library.books.get(b, 0) == 0:
                print(f"{b} books are not available at the moment.")
            else:
                self.total_books += 1
                self.borrowed[b] = self.borrowed.get(b, 0) + 1
                library.books[b] -= 1
                print(f"{b} book is borrowed successfully")
        library.borrowers[self.name] = self.total_books
    def readerInfo(self, book=""):
        if book == "":
            print(f"{self.name}, you have {self.total_books} book(s) with you.")
            for b, count in self.borrowed.items():
                print(f"Books on {b}: {count}")
        else:
            print(f"{self.name}, you have {self.borrowed.get(book, 0)} {book} book(s) with you.")
L1 = Library('Dhaka', {'Arts':15, 'Fiction':135, 'Politics':2, 'Science':11, 'Poetry':15})
L1.details()
print("1----------------------")
r1 = Reader('Aladdin')
r1.borrow(L1, 'Arts','Fiction','Fiction','Politics')
print("2----------------------")
r1.borrow(L1, 'Politics','Fiction')
print("3----------------------")
r1.readerInfo()
print("4----------------------")
r1.readerInfo('Fiction')
print("5----------------------")
L1.details()
print("6----------------------")
r2 = Reader('Jasmine')
r2.borrow(L1, 'Politics','Poetry')
print("7----------------------")
r2.readerInfo()
print("8----------------------")
L1.details()
