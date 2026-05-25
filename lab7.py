# LAB-7: Inheritance

# 1: BBA_Student inheriting Student
class Student:
    def __init__(self, name='Just a student', dept='nothing'):
        self.__name = name
        self.__department = dept
    def set_department(self, dept): self.__department = dept
    def get_name(self): return self.__name
    def set_name(self, name): self.__name = name
    def __str__(self):
        return 'Name: '+self.__name+' Department: '+self.__department
class BBA_Student(Student):
    def __init__(self, name="default", dept="BBA"):
        super().__init__(name, dept)
print(BBA_Student())
print(BBA_Student('Humpty Dumpty'))
print(BBA_Student('Little Bo Peep'))

# 2: Vehicle2010 inheriting Vehicle
class Vehicle:
    def __init__(self):
        self.x = 0
        self.y = 0
    def moveUp(self): self.y += 1
    def moveDown(self): self.y -= 1
    def moveRight(self): self.x += 1
    def moveLeft(self): self.x -= 1
    def __str__(self): return '('+str(self.x)+' , '+str(self.y)+')'
class Vehicle2010(Vehicle):
    def moveUpperRight(self): self.x += 1; self.y += 1
    def moveUpperLeft(self): self.x -= 1; self.y += 1
    def moveLowerRight(self): self.x += 1; self.y -= 1
    def moveLowerLeft(self): self.x -= 1; self.y -= 1
    def equals(self, other): return self.x == other.x and self.y == other.y
print('Part 1')
print('------')
car = Vehicle()
print(car)
car.moveUp()
print(car)
car.moveLeft()
print(car)
car.moveDown()
print(car)
car.moveRight()
print(car)
print('------')
print('Part 2')
print('------')
car1 = Vehicle2010()
print(car1)
car1.moveLowerLeft()
print(car1)
car2 = Vehicle2010()
car2.moveLeft()
print(car1.equals(car2))
car2.moveDown()
print(car1.equals(car2))

# 3: Cricket_Tournament and Tennis_Tournament inheriting Tournament
class Tournament:
    def __init__(self, name='Default'):
        self.__name = name
    def set_name(self, name): self.__name = name
    def get_name(self): return self.__name
class Cricket_Tournament(Tournament):
    def __init__(self, name="Default", teams=0, typ="No type"):
        super().__init__(name)
        self.teams = teams
        self.typ = typ
    def detail(self):
        return f"Cricket Tournament Name: {self.get_name()}\nNumber of Teams: {self.teams}\nType: {self.typ}"
class Tennis_Tournament(Tournament):
    def __init__(self, name, players):
        super().__init__(name)
        self.players = players
    def detail(self):
        return f"Tennis Tournament Name: {self.get_name()}\nNumber of Players: {self.players}"
ct1 = Cricket_Tournament()
print(ct1.detail())
print("-----------------------")
ct2 = Cricket_Tournament("IPL", 10, "t20")
print(ct2.detail())
print("-----------------------")
tt = Tennis_Tournament("Roland Garros", 128)
print(tt.detail())

# 4: Book and CD inheriting Product
class Product:
    def __init__(self, pid, title, price):
        self.__id = pid
        self.__title = title
        self.__price = price
    def get_id_title_price(self):
        return f"ID: {self.__id} Title:{self.__title} Price: {self.__price}"
class Book(Product):
    def __init__(self, pid, title, price, isbn, publisher):
        super().__init__(pid, title, price)
        self.isbn = isbn
        self.publisher = publisher
    def printDetail(self):
        return f"{self.get_id_title_price()}\nISBN: {self.isbn} Publisher: {self.publisher}"
class CD(Product):
    def __init__(self, pid, title, price, band, duration, genre):
        super().__init__(pid, title, price)
        self.band = band
        self.duration = duration
        self.genre = genre
    def printDetail(self):
        return f"{self.get_id_title_price()}\nBand: {self.band} Duration: {self.duration} minutes Genre: {self.genre}"
book = Book(1, "The Alchemist", 500, "97806", "HarperCollins")
print(book.printDetail())
print("-----------------------")
cd = CD(2, "Shotto", 300, "Warfaze", 50, "Hard Rock")
print(cd.printDetail())

# 5: Dog and Cat inheriting Animal
class Animal:
    def __init__(self, sound):
        self.__sound = sound
    def makeSound(self):
        return self.__sound
class Printer:
    def printSound(self, animal):
        print(animal.makeSound())
class Dog(Animal):
    def __init__(self, sound):
        super().__init__(sound)
class Cat(Animal):
    def __init__(self, sound):
        super().__init__(sound)
d1 = Dog('bark')
c1 = Cat('meow')
a1 = Animal('Animal does not make sound')
pr = Printer()
pr.printSound(a1)
pr.printSound(c1)
pr.printSound(d1)

# 6: triangle and trapezoid inheriting Shape
class Shape:
    def __init__(self, name='Default', height=0, base=0):
        self.area = 0
        self.name = name
        self.height = height
        self.base = base
    def get_height_base(self):
        return f"Height: {self.height}, Base: {self.base}"
class triangle(Shape):
    def __init__(self, name='Default', height=0, base=0):
        super().__init__(name, height, base)
    def calcArea(self):
        self.area = 0.5 * self.height * self.base
    def printDetail(self):
        return f"Shape name: {self.name}\n{self.get_height_base()}\nArea: {self.area}"
class trapezoid(Shape):
    def __init__(self, name='Default', height=0, base=0, side=0):
        super().__init__(name, height, base)
        self.side = side
    def calcArea(self):
        self.area = 0.5 * (self.side + self.base) * self.height
    def printDetail(self):
        return f"Shape name: {self.name}\n{self.get_height_base()}, Side_A:{self.side}\nArea: {self.area}"
tri_default = triangle()
tri_default.calcArea()
print(tri_default.printDetail())
print('--------------------------')
tri = triangle('Triangle', 10, 5)
tri.calcArea()
print(tri.printDetail())
print('---------------------------')
trap = trapezoid('Trapezoid', 10, 6, 4)
trap.calcArea()
print(trap.printDetail())

# 7: Player and Manager inheriting SportsPerson
class SportsPerson:
    def __init__(self, team_name, name, role):
        self.__team = team_name
        self.__name = name
        self.role = role
        self.earning_per_match = 0
    def get_name_team(self):
        return f'Name: {self.__name}, Team Name: {self.__team}'
class Player(SportsPerson):
    def __init__(self, team, name, role, goals, played):
        super().__init__(team, name, role)
        self.goal = goals
        self.play = played
        self.earning_per_match = (goals * 1000) + (played * 10)
    def calculate_ratio(self):
        self.ratio = self.goal / self.play
    def print_details(self):
        print(self.get_name_team())
        print(f"Team Role: {self.role}")
        print(f"Total Goal: {self.goal}, Total Played: {self.play}")
        print(f"Goal Ratio: {self.ratio}")
        print(f"Match Earning: {self.earning_per_match}k")
class Manager(SportsPerson):
    def __init__(self, team, name, role, wins):
        super().__init__(team, name, role)
        self.win = wins
        self.earning_per_match = wins * 1000
    def print_details(self):
        print(self.get_name_team())
        print(f"Team Role: {self.role}")
        print(f"Total Win: {self.win}")
        print(f"Match Earning: {self.earning_per_match}k")
player_one = Player('Juventus', 'Ronaldo', 'Striker', 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print('------------------------------------------')
manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
manager_one.print_details()

# Extra: Simple brac class for testing
class brac:
    def __init__(self, name="stu", age=19):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}"
s1 = brac("a", 16)
print(s1)
print("========================")
print(brac())
