# PROBLEM: Bus simulation from the "PROBLEM" section
class Bus:
    def __init__(self, name, route):
        self.name = name
        self.route = route
        self.stops = route.split('-')
        self.current = self.stops[0]
        self.passengers = {}
        self.fare_collected = 0
        print(f"{name} is currently at {self.stops[0]}")
    def addPassenger(self, *args):
        for i in range(0, len(args), 2):
            name = args[i]
            dest = args[i+1]
            if dest in bus_fare:
                if dest in self.stops:
                    fare = bus_fare[dest] - bus_fare[self.current]
                    self.passengers[name] = f"{self.current} to {dest}"
                    self.fare_collected += fare
                    print(f"{name} please get on the bus.")
                else:
                    print(f"Sorry {name}, this bus does not go to {dest}")
            else:
                print(f"Sorry {name}, this bus does not go to {dest}")
    def printDetails(self):
        print(f"Bus Name:{self.name}")
        print(f"Route:{self.route}")
        print(f"Total passengers:{len(self.passengers)}")
        print(f"Total fare collected:{self.fare_collected} taka")
        print("Passenger List:")
        for name, journey in self.passengers.items():
            print(f"{journey}: {name}")
    def reach(self, stop):
        self.current = stop
        print("Reached", stop)
        to_remove = []
        for name, journey in self.passengers.items():
            if stop in journey:
                print(f"{name} please get down")
                to_remove.append(name)
        for name in to_remove:
            del self.passengers[name]
bus_fare = {"Gabtoli":0, "Shyamoli":10, "Dhanmondi 27":15, "Science Lab":20, "Shahabag":25, "Motsho bhaban":30, "Stadium":35}
b1 = Bus("7 no bus", "Gabtoli-Gulistan")
b1.addPassenger("Alice","Science Lab","Bob","Dhanmondi 27")
b1.addPassenger("Jack","Stadium","Aeron","Shyamoli")
b1.printDetails()
b1.addPassenger("Robin","New Market")
b1.reach("Shyamoli")
b1.addPassenger("Jon","Stadium","Beck","Shahabag")
b1.printDetails()
b1.reach("Dhanmondi 27")
b1.addPassenger("Ethan","Stadium")
b1.printDetails()

# Another bus with different fare map
bus_fare2 = {"Gabtoli":0,"Shyamoli":10,"Dhanmondi":15,"Farmgate":20,"Kaoran bazar":25,"Shahabag":30,"Stadium":35}
b2 = Bus("8 no bus", "Gabtoli-Gulistan")
b2.addPassenger("Alice","Kaoran bazar","Bob","Dhanmondi")
b2.addPassenger("Jack","Stadium","Aeron","Shyamoli")
b2.printDetails()
b2.addPassenger("Robin","Science Lab")
b2.reach("Shyamoli")
b2.addPassenger("Jon","Stadium","Beck","Shahabag")
b2.printDetails()
b2.reach("Farmgate")
b2.addPassenger("Ethan","Stadium")
b2.printDetails()

# Exam class
class Exam:
    def __init__(self, typ, questions, per_mark):
        self.typ = typ
        self.questions = questions
        self.per_mark = per_mark
        self.total = questions * per_mark
    def detail(self):
        return f"Exam Type: {self.typ}\nNumber of questions: {self.questions}\nMarks per questions: {self.per_mark}\nTotal Marks: {self.total}"
e1 = Exam('Midterm', 2, 10)
print(e1.detail())
print("===========================")
e2 = Exam('Final', 3, 10)
print(e2.detail())

# MidA tracing
class MidA:
    def __init__(self):
        self.x = 3
        self.y = 7
        self.sum = 0
    def methodA(self, x):
        self.y = x + self.sum + self.x
        self.sum = x + self.y
        z = MidA()
        z.sum = self.sum + self.y
        self.methodB(z)
        print(self.x, self.y, self.sum)
    def methodB(self, a):
        y = 3
        a.x = self.x + self.sum
        self.sum = a.x + a.y + y
        print(a.x, a.y, a.sum)
a = MidA()
a.methodA(5)

# RickMote class (cable box remote)
class RickMote:
    def __init__(self):
        self.cbox = "OFF"
        self.vol = 3
        self.chan = 0
        self.chanum = 1
    def power(self):
        self.cbox = "ON" if self.cbox == "OFF" else "OFF"
    def changeChannel(self, num=None):
        channels = [0,2,3,6,7,9]
        if self.cbox == "OFF":
            print("Power is turned off. Cannot change channel.")
        else:
            if num is None:
                self.chanum += 1
                self.chan = channels[self.chanum-1]
            elif 1 <= num <= len(channels):
                self.chanum = num
                self.chan = channels[num-1]
            else:
                print("TV channel does not exist.")
    def changeVolumeLevel(self, delta=1):
        if self.cbox == "OFF":
            print("Power is turned off. Cannot change volume.")
        else:
            self.vol += delta
    def showInfo(self):
        print("ID Cable Box Status:\nCable Box is:", self.cbox)
        if self.cbox == "ON":
            print(f"Channel:{self.chan}\nVolume:{self.vol}")
oTV = RickMote()
oTV.power()
oTV.showInfo()
oTV.changeChannel()
oTV.changeVolumeLevel()
oTV.showInfo()
oTV.power()
oTV.showInfo()
oTV.power()
oTV.changeVolumeLevel(4)
oTV.changeChannel(3)
oTV.showInfo()
oTV.changeVolumeLevel(-2)
oTV.showInfo()
oTV.power()
oTV.changeChannel(9)
oTV.changeVolumeLevel(-1)
oTV.showInfo()
oTV.power()
oTV.changeChannel(11)
oTV.showInfo()

# PizzaMachine class
class PizzaMachine:
    def __init__(self, typ="regular", size=6):
        self.typ = typ
        self.size = size
    def customizePizza(self, toppings, spice="Regular"):
        if not isinstance(toppings, list):
            return "No toppings specified! Can't bake pizza."
        allowed = ["Regular", "Hot", "Super Naga"]
        if spice not in allowed:
            return "Sorry! Spice level not allowed. Can't bake pizza."
        topping_str = ",".join(toppings)
        return f"Your {self.size}-inch {spice} spicy {self.typ} Pizza is ready with {topping_str} toppings. Enjoy!"
pizza1 = PizzaMachine()
order1 = pizza1.customizePizza(["Cheese", "Pepperoni"], "Hot")
print(order1)
pizza2 = PizzaMachine("Vege")
order2 = pizza2.customizePizza("Super Naga")
print(order2)
pizza3 = PizzaMachine("Chicken Blast", 12)
order3 = pizza3.customizePizza(["Mushroom"])
print(order3)
pizza4 = PizzaMachine("Beef Bonanza", 16)
order4 = pizza4.customizePizza(["Cheese", "Beef kalabhuna"], "Mild")
print(order4)

# PlayerEarning class (task1)
class PlayerEarning:
    def __init__(self, name):
        self.name = name
    def calculateTotal(self, earnings, goals=0):
        self.earnings = earnings
        self.bonus = int(0.05 * earnings)
        if goals > 30:
            self.bonus += 10000
    def printDetails(self):
        print(f"Player Name: {self.name}")
        print(f"Player Season Earning without bonus: {self.earnings}")
        print(f"Bonus: {self.bonus}")
        print(f"Player Season Earning After Bonus: {self.earnings + self.bonus}")
player1 = PlayerEarning('Buffon')
player1.calculateTotal(250000)
player1.printDetails()
player2 = PlayerEarning('Dybala')
player2.calculateTotal(250000, 31)
player2.printDetails()
player3 = PlayerEarning('Cuadrado')
player3.calculateTotal(250000, 20)
player3.printDetails()

# myList class (task2)
class myList:
    def __init__(self, *items):
        self.items = list(items)
    def sum(self):
        self.total = sum(self.items)
        print("Sum:", self.total)
    def merge(self, *new_items):
        self.items.extend(new_items)
    def average(self):
        if not self.items:
            print("Average: 0")
        else:
            print("Average:", self.total / len(self.items))
l1 = myList(2,3,4,5,6)
l1.sum()
l1.merge(4,5,9)
l1.sum()
l1.average()
print("-----------------------------")
l2 = myList()
l2.average()
l2.merge(1,2,4,8)
l2.sum()

# Transport, Bus, Train (task11)
class Transport:
    total_traveller = 0
    def __init__(self, name, fare):
        self.name = name
        self.baseFare = fare
    def __str__(self):
        return f"Name: {self.name}, Base fare: {self.baseFare}"
class Bus(Transport):
    def __init__(self, name, fare):
        super().__init__(name, fare)
        self.passengers = {}
        self.passenger_count = 0
        print(f"Base-fare of {self.name} is {self.baseFare} Taka ")
    def addPassengerWithBags(self, *args):
        for i in range(0, len(args), 2):
            name = args[i]
            bags = args[i+1]
            extra = 0
            if 3 <= bags <= 5:
                extra = 60
            elif bags > 5:
                extra = 105
            self.passengers[name] = self.baseFare + extra
            Transport.total_traveller += 1
            self.passenger_count += 1
    def __str__(self):
        details = ""
        for name, fare in self.passengers.items():
            details += f"\nName: {name}, Fare: {fare}"
        return f"{super().__str__()}\nTotal Passenger(s): {self.passenger_count}\nPassenger Details:{details}"
class Train(Bus):
    def __init__(self, name, fare):
        super().__init__(name, fare)
t1 = Bus("Volvo", 950)
t1.addPassengerWithBags("David", 6, "Mike", 1, "Carol", 3)
print(t1)
t2 = Train("Silk City", 850)
t2.addPassengerWithBags("Bob", 2, "Simon", 4)
print(t2)
print("Total Passengers in Transport: ", Transport.total_traveller)

# AppleProduct, MacBookPro2020, iPhone12 (task12)
class AppleProduct:
    def __init__(self, name, model, base_price):
        self.name = name
        self.model = model
        self.base_price = base_price
    def companyInfo(self):
        return ("Company Name: Apple\nFouder: Steve Jobs, Steve Wozniak, Ronald Wayne\n"
                "Current CEO: Tim Cook\nAddress: Apple Inc, 2511 Laguna Blvd, Elk Grove, CA 95758, United States")
    def feature(self):
        return f"Name: {self.name}\nProduct Model: {self.model}\nHardware Quality: Excellent Hardwares\nGuarantee/ Warranty: Apple Care"
    def __str__(self):
        print('This is apple product.')
    def calculatePrice(self):
        print('Total Price:', self.base_price)
class MacBookPro2020(AppleProduct):
    def __init__(self, name, model, ram, chip, tax, base_price=1299):
        super().__init__(name, model, base_price)
        self.ram = ram
        self.chip = chip
        self.tax = tax
    def __str__(self):
        return f"{self.feature()}\nRam: {self.ram}GB\nChip: {self.chip}\n{self.companyInfo()}"
    def calculatePrice(self):
        print("Calculating Total Price:")
        print(f"Base Price: {self.base_price}")
        print(f"Tax: {self.tax}%")
        self.base_price += (self.base_price * self.tax) / 100
        super().calculatePrice()
    def __add__(self, other):
        return self.base_price + other.base_price
class iPhone12(MacBookPro2020):
    def __init__(self, name, model, ram, chip, tax, base_price=799):
        super().__init__(name, model, ram, chip, tax, base_price)
m1 = MacBookPro2020('MacBook', 'MacBookPro2020', 8, 'M1', 10)
print(m1)
m1.calculatePrice()
iphone = iPhone12('iPhone', 'iPhone 12', 8, 'A14', 5)
print(iphone)
iphone.calculatePrice()
print('Total Price of these two products: %.2f Dollars' % (m1 + iphone))

# University, Department (task from "PROBLEM" with database)
class University:
    database = {}
    Fac_count = 0
    Std_count = 0
    def __init__(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def addToDB(self, other):
        print(f'Successfully added {self.__name} to {other.__name} database')
    def __str__(self):
        return f'{self.__name} has a total of {University.Fac_count} faculty members and {University.Std_count} students'
class Department(University):
    def __init__(self, name, uni, fac, stu):
        super().__init__(name)
        self.uni = uni
        self.fac = fac
        self.stu = stu
        University.Fac_count += fac
        University.Std_count += stu
    def __str__(self):
        return f"The {self.getName()} Department of {self.uni} has {self.fac} faculty members and {self.stu} students"
    def addToDB(self, uni_obj):
        if uni_obj.getName() not in University.database:
            University.database[uni_obj.getName()] = [self.getName()]
            super().addToDB(uni_obj)
        elif self.getName() in University.database[uni_obj.getName()]:
            print(f"{self.getName()} is already present. Cannot add to database")
        else:
            University.database[uni_obj.getName()].append(self.getName())
            super().addToDB(uni_obj)
    def newStudent(self, num, semester):
        self.stu += num
        University.Std_count += num
        print(f"{num} students have been admitted in {semester} semester")
bracu = University('BracU')
print(bracu)
cse = Department('CSE', 'BracU', 84, 4360)
print(cse)
bbs = Department('BBS', 'BracU', 65, 1398)
print(bbs)
cse.newStudent(550, 'Spring 23')
print(cse)
print(bracu)
University.Fac_count = 0
University.Std_count = 0
buet = University('BUET')
print(buet)
eee = Department('EEE', 'BUET', 24, 140)
print(eee)
print(buet)
cse.addToDB(bracu)
bbs.addToDB(bracu)
bbs.addToDB(bracu)
eee.addToDB(buet)
print(University.database)

# Tinder, Profile classes (project)
class Tinder:
    profiles = []
    @staticmethod
    def welcome():
        print("<3~~~ Welcome to Tinder ~~~<3\n")
    def __init__(self, name="", food="", music="", work="", pref_gender=""):
        self.name = name
        self.food = food
        self.music = music
        self.work = work
        self.preferred_gender = pref_gender
        self.points = 0
    def matchmaker(self, a, b):
        print(f"Trying to ship {a.name} and {b.name}!")
        if a.get_gender() not in b.preferred_gender or b.get_gender() not in a.preferred_gender:
            print("Gender Mismatch. Abort mission!\n")
            return
        age_gap = abs(a.get_age() - b.get_age())
        if age_gap <= 5:
            self.points += 5
        if a.food == b.food:
            self.points += 1
        for m in a.music:
            if m in b.music:
                self.points += 1
        if a.work != b.work:
            self.points += 2
        if a.work == b.work:
            if a.work == "Unemployed":
                self.points -= 1
            else:
                self.points += 5
        print(f"Total points for {a.name} and {b.name} after matchmaking: {self.points}")
        if self.points > 6:
            print("Good Match. Swipe Right!\n")
            a.matches[b] = self.points
            b.matches[a] = self.points
        else:
            print("Not Going to Work! Swipe Left!\n")
        self.points = 0
    def __str__(self):
        names = "\n".join(p.name for p in Tinder.profiles)
        return f"Profiles:\n{names}\nTotal profile(s) created: {len(Tinder.profiles)}\n"
    def find_best_match(self, profile):
        if not profile.matches:
            return "No match found\n"
        best = max(profile.matches.items(), key=lambda x: x[1])
        return f"Best match for {profile.name}: {best[0].name}\n"
    @classmethod
    def add_profile(cls, *profiles):
        cls.profiles.extend(profiles)
class Profile(Tinder):
    profile_no = 0
    def __init__(self, name="Samiha", age=21, food=" Non-Vegetarian", music=['Classical','Jazz'], work="Unemployed", gender="Female", pref_gender="Male"):
        super().__init__(name, food, music, work, pref_gender)
        self.__age = age
        self.__gender = gender
        self.matches = {}
        Profile.profile_no += 1
        print(f"Profile no. {Profile.profile_no} Created!\n")
    def get_age(self): return self.__age
    def get_gender(self): return self.__gender
    def __str__(self):
        matches_str = "\n".join(p.name for p in self.matches.keys()) if self.matches else "None"
        return (f"Name: {self.name}\nAge: {self.get_age()}\nFood Habit: {self.food}\n"
                f"Music Taste: {self.music}\nWork Status: {self.work}\n"
                f"Total Matches: {len(self.matches)}\nGood
