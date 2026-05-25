# LAB-4: Advanced Class Exercises

# 1: Customer class with greet and purchase
class Customer:
    def __init__(self, name):
        self.name = name
    def greet(self, name=""):
        if name:
            print(f"Hello {name}!")
        else:
            print("Hello!")
    def purchase(self, *items):
        print(f"{self.name}, you purchased {len(items)} item(s):")
        for item in items:
            print(item)
customer_1 = Customer("Sam")
customer_1.greet()
customer_1.purchase("chips", "chocolate", "orange juice")
print("-----------------------------")
customer_2 = Customer("David")
customer_2.greet("David")
customer_2.purchase("orange juice")

# 2: Panda class with sleep method
class Panda:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    def sleep(self, hours=0):
        if hours == 0:
            return f"{self.name}'s duration is unknown thus should have only bamboo leaves"
        elif 3 <= hours <= 5:
            food = "Mixed Veggies"
        elif 6 <= hours <= 8:
            food = "Eggplant & Tofu"
        elif 9 <= hours <= 11:
            food = "Broccoli Chicken"
        return f"{self.name} sleeps {hours} hours daily and should have {food}"
panda1 = Panda("Kunfu", "Male", 5)
panda2 = Panda("Pan Pan", "Female", 3)
panda3 = Panda("Ming Ming", "Female", 8)
for p in [panda1, panda2, panda3]:
    print(f"{p.name} is a {p.gender} Panda Bear who is {p.age} years old")
print("===========================")
print(panda2.sleep(10))
print(panda1.sleep(4))
print(panda3.sleep())

# 3: Cat class with default values
class Cat:
    def __init__(self, color="White", action="sitting"):
        self.color = color
        self.action = action
    def printCat(self):
        print(f"{self.color} cat is {self.action}")
    def changeColor(self, new_color):
        self.color = new_color
c1 = Cat()
c2 = Cat("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
for c in [c1, c2, c3, c4]:
    c.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()

# 4: Student class with quiz average
class Student:
    def __init__(self, name="default student"):
        self.name = name
    def quizcalc(self, *scores):
        self.avg = sum(scores) / 3
    def printdetail(self):
        print(f"Hello {self.name}")
        print(f"Your average quiz score is {self.avg}")
s1 = Student()
s1.quizcalc(10)
print('--------------------------------')
s1.printdetail()
s2 = Student('Harry')
s2.quizcalc(10,8)
print('--------------------------------')
s2.printdetail()
s3 = Student('Hermione')
s3.quizcalc(10,9,10)
print('--------------------------------')
s3.printdetail()

# 5: Student class with daily effort suggestion
class Student:
    def __init__(self, name, sid, dept="CSE"):
        self.name = name
        self.id = sid
        self.dept = dept
    def dailyEffort(self, hours):
        self.effort = hours
        if hours <= 2:
            self.suggestion = "Should give more effort!"
        elif hours <= 4:
            self.suggestion = "Keep up the good work!"
        else:
            self.suggestion = "Excellent! Now motivate others"
    def printDetails(self):
        print(f"Name: {self.name}\nID: {self.id}\nDepartment: {self.dept}")
        print(f"Daily Effort: {self.effort} hour(s)\nSuggestion: {self.suggestion}")
harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()

# 6: Patient class with symptoms
class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def add_Symptom(self, *symptoms):
        self.symptoms = symptoms
    def printPatientDetail(self):
        print(f"Name: {self.name}\nAge: {self.age}\nSymptoms: {', '.join(self.symptoms)}")
p1 = Patient("Thomas", 23)
p1.add_Symptom("Headache")
p2 = Patient("Carol", 20)
p2.add_Symptom("Vomiting", "Coughing")
p3 = Patient("Mike", 25)
p3.add_Symptom("Fever", "Headache", "Coughing")
for p in [p1, p2, p3]:
    print("=========================")
    p.printPatientDetail()

# 7: Match class (cricket simulation)
class Match:
    def __init__(self, teams):
        self.bat, self.ball = teams.split('-')
        self.runs = 0
        self.wickets = 0
        self.overs = 0
        print("5..4..3..2..1.. Play !!!")
    def add_run(self, runs):
        self.runs += runs
    def add_over(self, overs):
        if overs < 5:
            self.overs += overs
        else:
            print(f"Warning! Cannot add {overs} over/s (5 over match)")
    def add_wicket(self, _):
        self.wickets += 1
    def print_scoreboard(self):
        return f"Batting Team: {self.bat}\nBowling Team: {self.ball}\nTotal Runs: {self.runs} Wickets: {self.wickets} Overs: {self.overs}"
match1 = Match("Rangpur Riders-Cumilla Victorians")
print("=========================")
match1.add_run(4)
match1.add_run(6)
match1.add_over(1)
print(match1.print_scoreboard())
print("=========================")
match1.add_over(5)
print("=========================")
match1.add_wicket(1)
print(match1.print_scoreboard())

# 8: ParcelKoro class
class ParcelKoro:
    def __init__(self, name="No name set", weight=0):
        self.name = name
        self.product_weight = weight
    def calculateFee(self, location=""):
        if self.product_weight == 0:
            self.fee = 0
        elif location == "":
            self.fee = (self.product_weight * 20) + 50
        else:
            self.fee = (self.product_weight * 20) + 100
    def printDetails(self):
        print(f"Customer Name: {self.name}\nProduct Weight: {self.product_weight}\nTotal fee: {self.fee}")
p1 = ParcelKoro()
p1.calculateFee()
p1.printDetails()
p2 = ParcelKoro('Bob The Builder')
p2.calculateFee()
p2.printDetails()
p2.product_weight = 15
p2.calculateFee()
p2.printDetails()
p3 = ParcelKoro('Dora The Explorer', 10)
p3.calculateFee('Dhanmondi')
p3.printDetails()

# 9: Batsman class
class Batsman:
    def __init__(self, *args):
        if len(args) == 2:
            self.name = "New Batsman"
            self.runs, self.balls = args
        else:
            self.name, self.runs, self.balls = args
    def printCareerStatistics(self):
        print(f"Name: {self.name}\nRuns Scored: {self.runs} , Balls Faced: {self.balls}")
    def battingStrikeRate(self):
        return self.runs / self.balls * 100
    def setName(self, new_name):
        self.name = new_name
b1 = Batsman(6101, 7380)
b1.printCareerStatistics()
print("============================")
b2 = Batsman("Liton Das", 678, 773)
b2.printCareerStatistics()
print("----------------------------")
print(b2.battingStrikeRate())
print("============================")
b1.setName("Shakib Al Hasan")
b1.printCareerStatistics()
print("----------------------------")
print(b1.battingStrikeRate())

# 10: EPL_Team class
class EPL_Team:
    def __init__(self, name, song="No Slogan", titles=0):
        self.name = name
        self.song = song
        self.title = titles
    def showClubInfo(self):
        return f"Name: {self.name}\nSong: {self.song}\nTotal No of title: {self.title}"
    def changeSong(self, new_song):
        self.song = new_song
    def increaseTitle(self):
        self.title += 1
manu = EPL_Team('Manchester United', 'Glory Glory Man United')
chelsea = EPL_Team('Chelsea')
print('===================')
print(manu.showClubInfo())
print('##################')
manu.increaseTitle()
print(manu.showClubInfo())
print('===================')
print(chelsea.showClubInfo())
chelsea.changeSong('Keep the blue flag flying high')
print(chelsea.showClubInfo())

# 11: Author class
class Author:
    def __init__(self, name="Default", *books):
        self.name = name
        self.books = list(books)
    def addBooks(self, *new_books):
        self.books.extend(new_books)
    def changeName(self, new_name):
        self.name = new_name
    def printDetails(self):
        print(f"Autor name: {self.name}\n--------\nList of Books:")
        for book in self.books:
            print(book)
auth1 = Author('Humayun Ahmed')
auth1.addBooks('Deyal', 'Megher Opor Bari')
auth1.printDetails()
print('===================')
auth2 = Author()
print(auth2.name)
auth2.changeName('Mario Puzo')
auth2.addBooks('The Godfather', 'Omerta', 'The Sicilian')
print('===================')
auth2.printDetails()
print('===================')
auth3 = Author('Paolo Coelho', 'The Alchemist', 'The Fifth Mountain')
auth3.printDetails()

# 12: TaxiLagbe class
class TaxiLagbe:
    def __init__(self, taxi_num, area):
        self.num = taxi_num
        self.area = area
        self.passengers = []
        self.total_fare = 0
    def addPassenger(self, *passengers):
        for p in passengers:
            if len(self.passengers) < 4:
                name, fare = p.split('_')
                self.passengers.append(name)
                self.total_fare += int(fare)
                print(f"Dear {name}! Welcome to TaxiLagbe.")
            else:
                print("Taxi Full! No more passengers can be added.")
    def printDetails(self):
        print(f"Trip info for Taxi number: {self.num}")
        print(f"This taxi can cover only {self.area} area.")
        print(f"Total passengers:{len(self.passengers)}")
        print("Passenger lists:", ", ".join(self.passengers))
        print(f"Total collected fare: {self.total_fare} Taka")
taxi1 = TaxiLagbe('1010-01', 'Dhaka')
print('-------------------------------')
taxi1.addPassenger('Walker_100', 'Wood_200')
taxi1.addPassenger('Matt_100')
taxi1.addPassenger('Wilson_105')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi1.addPassenger('Karen_200')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi2 = TaxiLagbe('1010-02', 'Khulna')
taxi2.addPassenger('Ronald_115')
taxi2.addPassenger('Parker_215')
print('-------------------------------')
taxi2.printDetails()

# 13: Account class with withdrawal constraint
class Account:
    def __init__(self, name="Default Account", balance=0):
        self.name = name
        self.balance = float(balance)
    def details(self):
        return f"{self.name}\n{self.balance}"
    def withdraw(self, amount):
        new_balance = self.balance - amount
        min_allowed = self.balance * 0.307
        if new_balance > min_allowed:
            self.balance = new_balance
            print("Withdraw successful! New balance is:", self.balance)
        else:
            print("Sorry, Withdraw unsuccessful! The account balance after deducting withdraw amount is equal to or less than minimum.")
a1 = Account()
print(a1.details())
print("------------------------")
a1.name = "Oliver"
a1.balance = 10000.0
print(a1.details())
print("------------------------")
a2 = Account("Liam")
print(a2.details())
print("------------------------")
a3 = Account("Noah", 400)
print(a3.details())
print("------------------------")
a1.withdraw(6930)
print("------------------------")
a2.withdraw(600)
print("------------------------")
a1.withdraw(6929)

# 14: StudentDatabase class
class StudentDatabase:
    def __init__(self, name, sid):
        self.name = name
        self.user = sid
        self.grades = {}
    def calculateGPA(self, courses, semester):
        total = 0
        course_names = []
        for c in courses:
            name, grade = c.split(": ")
            course_names.append(name)
            total += float(grade)
        gpa = round(total / len(course_names), 2)
        self.grades[semester] = {tuple(course_names): gpa}
    def printDetails(self):
        print(f"Name: {self.name}\nID: {self.user}")
        for sem, data in self.grades.items():
            print(f"Courses taken in {sem}")
            for courses, gpa in data.items():
                for course in courses:
                    print(course)
                print(f"GPA {gpa}")
s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0', 'MAT110: 4.0'], 'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'], 'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('------------------------------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7', 'ENG101: 4.0'], 'Summer2022')
print('------------------------------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('------------------------------------------------------')
s2.printDetails()

# 15: FinalT6A tracing
class FinalT6A:
    def __init__(self, x, p):
        self.temp, self.sum, self.y = 4, 0, 1
        self.temp += 1
        self.y = self.temp - p
        self.sum = self.temp + x
        print(x, self.y, self.sum)
    def methodA(self):
        x = 0
        y = 0
        y = y + self.y
        x = self.y + 2 + self.temp
        self.sum = x + y + self.methodB(self.temp, y)
        print(x, y, self.sum)
    def methodB(self, temp, n):
        x = 0
        temp += 1
        self.y = self.y + temp
        x = x + 3 + n
        self.sum = self.sum + x + self.y
        print(x, self.y, self.sum)
        return self.sum
q1 = FinalT6A(2,1)
q1.methodA()
q1.methodA()

# 16: Quiz3A tracing
class Quiz3A:
    def __init__(self, k=None):
        self.temp, self.sum, self.y = 4, 0, 0
        if k is not None:
            self.temp += 1
            self.sum = self.temp + k
            self.y = self.sum - 1
        else:
            self.y = self.temp - 1
            self.sum = self.temp + 1
            self.temp += 2
    def methodB(self, m, n):
        x = 0
        self.temp += 1
        self.y = self.y + m + self.temp
        x = x + 2 + n
        self.sum = self.sum + x + self.y
        print(x, self.y, self.sum)
        return self.sum
a1 = Quiz3A()
a1.methodB(1,2)
a2 = Quiz3A(3)
a2.methodB(2,4)
a1.methodB(2,1)
a2.methodB(1,3)

# 17: Test5 (another tracing)
class Test5:
    def __init__(self):
        self.sum = 0
        self.y = 0
    def methodA(self):
        x = y = k = 0
        msg = [5]
        while k < 2:
            y += msg[0]
            x = y + self.methodB(msg, k)
            self.sum = x + y + msg[0]
            print(x, y, self.sum)
            k += 1
    def methodB(self, mg2, mg1):
        x = 0
        self.y += mg2[0]
        x = x + 3 + mg1
        self.sum += x + self.y
        mg2[0] = self.y + mg1
        mg1 += x + 2
        print(x, self.y, self.sum)
        return mg1
t1 = Test5()
t1.methodA()
t1.methodA()
t1.methodA()

# 18: Test4 tracing
class Test4:
    def __init__(self):
        self.sum, self.y = 0, 0
    def methodA(self):
        x, y = 0, 0
        msg = [0]
        msg[0] = 5
        y = y + self.methodB(msg[0])
        x = y + self.methodB(msg, msg[0])
        self.sum = x + y + msg[0]
        print(x, y, self.sum)
    def methodB(self, *args):
        if len(args) == 1:
            mg1 = args[0]
            x, y = 0, 0
            y = y + mg1
            x = x + 33 + mg1
            self.sum = self.sum + x + y
            self.y = mg1 + x + 2
            print(x, y, self.sum)
            return y
        else:
            mg2, mg1 = args
            x = 0
            self.y = self.y + mg2[0]
            x = x + 33 + mg1
            self.sum = self.sum + x + self.y
            mg2[0] = self.y + mg1
            mg1 = mg1 + x + 2
            print(x, self.y, self.sum)
            return self.sum
t3 = Test4()
t3.methodA()
t3.methodA()
t3.methodA()
t3.methodA()

# 19: msgClass and Q5 tracing
class msgClass:
    def __init__(self):
        self.content = 0
class Q5:
    def __init__(self):
        self.sum = 1
        self.x = 2
        self.y = 3
    def methodA(self):
        x, y = 1, 1
        msg = []
        myMsg = msgClass()
        myMsg.content = self.x
        msg.append(myMsg)
        msg[0].content = self.y + myMsg.content
        self.y = self.y + self.methodB(msg[0])
        y = self.methodB(msg[0]) + self.y
        x = y + self.methodB(msg[0], msg)
        self.sum = x + y + msg[0].content
        print(x, y, self.sum)
    def methodB(self, mg1, mg2=None):
        if mg2 is None:
            x, y = 5, 6
            y = self.sum + mg1.content
            self.y = y + mg1.content
            x = self.x + 7 + mg1.content
            self.sum = self.sum + x + y
            self.x = mg1.content + x + 8
            print(x, y, self.sum)
            return y
        else:
            x = 1
            self.y += mg2[0].content
            mg2[0].content = self.y + mg1.content
            x = x + 4 + mg1.content
            self.sum += x + self.y
            mg1.content = self.sum - mg2[0].content
            print(self.x, self.y, self.sum)
            return self.sum
q = Q5()
q.methodA()

# 20: Student class with name/dept setting
class Student:
    def __init__(self, name="", dept=""):
        self.name = name
        self.dept = dept
        if not name and not dept:
            print("Student name and department need to be set")
        elif not dept:
            print(f"Department for {name} needs to be set")
        else:
            print(f"{name} is from {dept} department")
    def update_name(self, new_name):
        self.name = new_name
    def update_department(self, new_dept):
        self.dept = new_dept
    def enroll(self, *courses):
        self.courses = courses
    def printDetail(self):
        print(f"Name: {self.name}\nDepartment: {self.dept}")
        print(f"Jon enrolled in {len(self.courses)} course(s):")
        print(", ".join(self.courses))
s1 = Student()
print("=========================")
s2 = Student("Carol")
print("=========================")
s3 = Student("Jon", "EEE")
print("=========================")
s1.update_name("Bob")
s1.update_department("CSE")
s2.update_department("BBA")
s1.enroll("CSE110", "MAT110", "ENG091")
s2.enroll("BUS101")
s3.enroll("MAT110", "PHY111")
print("###########################")
s1.printDetail()
print("=========================")
s2.printDetail()
print("=========================")
s3.printDetail()

# 21: Student class with credit advising
class Student:
    def __init__(self, name, sid, dept):
        self.name = name
        self.sid = sid
        self.dept = dept
    def details(self):
        return f"Name: {self.name}\nID: {self.sid}\nDepartment: {self.dept}"
    def advise(self, *courses):
        self.courses = courses
        credits = len(courses) * 3.0
        print(f"{self.name}, you have taken {credits} credits.")
        print(f"List of courses: {', '.join(courses)}")
        print("Status:", end="")
        if 9 <= credits <= 12:
            print("Ok")
        elif credits < 9:
            need = int((9 - credits) / 3)
            print(f"You have to take at least {need} more course.")
        else:
            drop = int((credits - 12) / 3)
            print(f"You have to drop at least {drop} course.")
s1 = Student("Alice","20103012","CSE")
s2 = Student("Bob", "18301254","EEE")
s3 = Student("Carol", "17101238","CSE")
print("##########################")
print(s1.details())
print("##########################")
print(s2.details())
print("##########################")
s1.advise("CSE110", "MAT110", "PHY111")
print("##########################")
s2.advise("BUS101", "MAT120")
print("##########################")
s3.advise("MAT110", "PHY111", "ENG102", "CSE111", "CSE230")

# 22: Hotel class
class Hotel:
    def __init__(self, name):
        self.name = name
        self.staff = {}
        self.guests = {}
    def addStuff(self, name, age, phone="000"):
        sid = len(self.staff) + 1
        self.staff[sid] = [name, age, phone]
        print(f"Staff With ID {sid} is added")
    def addGuest(self, name, age, phone):
        gid = len(self.guests) + 1
        self.guests[gid] = [name, age, phone]
        print(f"Guest With ID {gid} is created")
    def getStuffById(self, sid):
        s = self.staff[sid]
        return f"Staff ID: {sid}\nName: {s[0]}\nAge: {s[1]}\nPhone no.: {s[2]}"
    def getGuestById(self, gid):
        g = self.guests[gid]
        return f"Guest ID: {gid}\nName: {g[0]}\nAge: {g[1]}\nPhone no.: {g[2]}"
    def allStaffs(self):
        print("All Staffs:")
        print(f"Number of Staff: {len(self.staff)}")
        for sid, s in self.staff.items():
            print(f"Staff ID: {sid} Name: {s[0]} Age: {s[1]} Phone no: {s[2]}")
    def allGuest(self):
        print("All Guest:")
        print(f"Number of Guest: {len(self.guests)}")
        for gid, g in self.guests.items():
            print(f"Guest ID: {gid} Name: {g[0]} Age: {g[1]} Phone no: {g[2]}")
h = Hotel("Lakeshore")
h.addStuff("Adam", 26)
print("=================================")
print(h.getStuffById(1))
print("=================================")
h.addGuest("Carol", 35, "123")
print("=================================")
print(h.getGuestById(1))
print("=================================")
h.addGuest("Diana", 32, "431")
print("=================================")
print(h.getGuestById(2))
print("=================================")
h.allStaffs()
print("=================================")
h.allGuest()

# 23: Author class with books by genre
class Author:
    def __init__(self, name=''):
        self.name = name
        self.books = {}
        self.total_books = 0
    def setName(self, new_name):
        self.name = new_name
    def addBook(self, title, genre):
        if not self.name:
            print("A book can not be added without author name")
            return
        if genre in self.books:
            self.books[genre] += ", " + title
        else:
            self.books[genre] = title
        self.total_books += 1
    def printDetail(self):
        print(f"Number of Book(s): {self.total_books}")
        print(f"Author Name: {self.name}")
        for genre, titles in self.books.items():
            print(f"{genre}: {titles}")
a1 = Author()
print("=================================")
a1.addBook('Ice', 'Science Fiction')
print("=================================")
a1.setName('Anna Kavan')
a1.addBook('Ice', 'Science Fiction')
a1.printDetail()
print("=================================")
a2 = Author('Humayun Ahmed')
a2.addBook('Onnobhubon', 'Science Fiction')
a2.addBook('Megher Upor Bari', 'Horror')
print("=================================")
a2.printDetail()
a2.addBook('Ireena', 'Science Fiction')
print("=================================")
a2.printDetail()
print("=================================")

# 24: Hospital, Doctor, Patient classes
class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = {}
        self.patients = {}
    def addDoctor(self, doc):
        self.doctors[doc.id] = doc.data
    def addPatient(self, pat):
        self.patients[pat.id] = pat.data
    def getDoctorByID(self, did):
        d = self.doctors[did]
        return f"Doctor's ID: {did}\nName: {d[0]}\nSpeciality: {d[1]}"
    def getPatientByID(self, pid):
        p = self.patients[pid]
        return f"Patient's ID: {pid}\nName: {p[0]}\nAge: {p[1]}\nPhone no.: {p[2]}"
    def allDoctors(self):
        print("All Doctors:\nNumber of Doctors:", len(self.doctors))
        print(self.doctors)
    def allPatients(self):
        print("All Patients:\nNumber of Patients:", len(self.patients))
        print(self.patients)
class Doctor:
    def __init__(self, doc_id, _, name, speciality):
        self.id = doc_id
        self.data = [name, speciality]
class Patient:
    def __init__(self, pat_id, _, name, age, phone):
        self.id = pat_id
        self.data = [name, age, phone]
h = Hospital("Evercare")
d1 = Doctor("1d", "Doctor", "Samar Kumar", "Neurologist")
h.addDoctor(d1)
print("=================================")
print(h.getDoctorByID("1d"))
print("=================================")
p1 = Patient("1p", "Patient", "Kashem Ahmed", 35, 12345)
h.addPatient(p1)
print("=================================")
print(h.getPatientByID("1p"))
print("=================================")
p2 = Patient("2p", "Patient", "Tanina Haque", 26, 33456)
h.addPatient(p2)
print("=================================")
print(h.getPatientByID("2p"))
print("=================================")
h.allDoctors()
h.allPatients()

# 25: Vaccine and Person classes
class Vaccine:
    def __init__(self, name, origin, days):
        self.name = name
        self.origin = origin
        self.days = days
class Person:
    def __init__(self, name, age, role=""):
        self.name = name
        self.age = age
        self.role = role
        self.vaccine = None
        self.dose1 = ""
        self.dose2 = ""
    def pushVaccine(self, vaccine, dose=""):
        if dose == "":
            if self.role == "Student" or self.age > 25:
                self.vaccine = vaccine.name
                self.dose1 = "Given"
                self.dose2 = f"Please come after {vaccine.days} days"
                print(f"1st dose done for {self.name}")
            else:
                print(f"Sorry {self.name}, Minimum age for taking vaccines is 25 years now.")
        else:
            if vaccine.name == self.vaccine:
                self.dose2 = "Given"
                print(f"2nd dose done for {self.name}")
            else:
                print(f"Sorry {self.name}, you can’t take 2 different vaccines")
    def showDetail(self):
        print(f"Name: {self.name} Age: {self.age} Type: {self.role}")
        print(f"Vaccine name: {self.vaccine}")
        print(f"1st dose: {self.dose1}")
        print(f"2nd dose: {self.dose2}")
astra = Vaccine("AstraZeneca", "UK", 60)
modr = Vaccine("Moderna", "UK", 30)
sin = Vaccine("Sinopharm", "China", 30)
p1 = Person("Bob", 21, "Student")
print("=================================")
p1.pushVaccine(astra)
print("=================================")
p1.showDetail()
print("=================================")
p1.pushVaccine(sin, "2nd Dose")
print("=================================")
p1.pushVaccine(astra, "2nd Dose")
print("=================================")
p1.showDetail()
print("=================================")
p2 = Person("Carol", 23, "Actor")
print("=================================")
p2.pushVaccine(sin)
print("=================================")
p3 = Person("David", 34)
print("=================================")
p3.pushVaccine(modr)
print("=================================")
p3.showDetail()
print("=================================")
p3.pushVaccine(modr, "2nd Dose")
