# LAB-3: Basic Class Definitions

# 1: DataType class
class DataType:
    def __init__(self, name, value):
        self.name = name
        self.value = value
data_type1 = DataType('Integer', 1234)
print(data_type1.name)
print(data_type1.value)
print('=====================')
data_type2 = DataType('String', 'Hello')
print(data_type2.name)
print(data_type2.value)
print('=====================')
data_type3 = DataType('Float', 4.0)
print(data_type3.name)
print(data_type3.value)

# 2: Joker class with equality check
class Joker:
    def __init__(self, name, power, is_psycho):
        self.name = name
        self.power = power
        self.is_he_psycho = is_psycho
j1 = Joker('Heath Ledger', 'Mind Game', False)
j2 = Joker('Joaquin Phoenix', 'Laughing out Loud', True)
print(j1.name, j1.power, j1.is_he_psycho)
print(j2.name, j2.power, j2.is_he_psycho)
if j1 == j2:
    print('same')
else:
    print('different')
j2.name = 'Heath Ledger'
if j1.name == j2.name:
    print('same')
else:
    print('different')

# 3: Pokemon class
class Pokemon:
    def __init__(self, name1, name2, power1, power2, damage):
        self.pokemon1_name = name1
        self.pokemon2_name = name2
        self.pokemon1_power = power1
        self.pokemon2_power = power2
        self.damage_rate = damage
team_pika = Pokemon('pikachu', 'charmander', 90, 60, 10)
print('=======Team 1=======')
print('Pokemon 1:', team_pika.pokemon1_name, team_pika.pokemon1_power)
print('Pokemon 2:', team_pika.pokemon2_name, team_pika.pokemon2_power)
pika_combined_power = (team_pika.pokemon1_power + team_pika.pokemon2_power) * team_pika.damage_rate
print('Combined Power:', pika_combined_power)
team_bulb = Pokemon('bulbasaur', 'squirtle', 80, 70, 9)
print('=======Team 2=======')
print('Pokemon 1:', team_bulb.pokemon1_name, team_bulb.pokemon1_power)
print('Pokemon 2:', team_bulb.pokemon2_name, team_bulb.pokemon2_power)
bulb_combined_power = (team_bulb.pokemon1_power + team_bulb.pokemon2_power) * team_bulb.damage_rate
print('Combined Power:', bulb_combined_power)

# 4: Country class
class Country:
    def __init__(self):
        self.name = "Bangladesh"
        self.continent = "Asia"
        self.capital = "Dhaka"
        self.fifa_ranking = 187
country = Country()
print('Name:', country.name)
print('Continent:', country.continent)
print('Capital:', country.capital)
print('Fifa Ranking:', country.fifa_ranking)
print('===================')
country.name = "Belgium"
country.continent = "Europe"
country.capital = "Brussels"
country.fifa_ranking = 1
print('Name:', country.name)
print('Continent:', country.continent)
print('Capital:', country.capital)
print('Fifa Ranking:', country.fifa_ranking)

# 5: DemonSlayer class
class DemonSlayer:
    def __init__(self, name, style, techniques, kills):
        self.name = name
        self.style = style
        self.number_of_technique = techniques
        self.kill = kills
tanjiro = DemonSlayer("Tanjiro", "Water Breathing", 10, 10)
zenitsu = DemonSlayer("Zenitsu", "Thunder Breathing", 1, 4)
inosuke = DemonSlayer("Inosuke", "Beast Breathing", 5, 7)
for slayer in [tanjiro, zenitsu, inosuke]:
    print('Name:', slayer.name)
    print('Fighting Style:', slayer.style)
    print(f'Knows {slayer.number_of_technique} technique(s) and has killed {slayer.kill} demon(s)')
    print('===================')
total_tech = tanjiro.number_of_technique + zenitsu.number_of_technique + inosuke.number_of_technique
total_kills = tanjiro.kill + zenitsu.kill + inosuke.kill
print(f'{tanjiro.name}, {zenitsu.name}, {inosuke.name} knows total {total_tech} techniques')
print(f'They have killed total {total_kills} demons')

# 6: Box class
class Box:
    def __init__(self, dims):
        self.height = dims[0]
        self.width = dims[1]
        self.breadth = dims[2]
        print(f"Creating a Box!\nVolume of the box is {self.height * self.width * self.breadth} cubic units.")
b1 = Box([10,10,10])
print("Height:", b1.height, "Width:", b1.width, "Breadth:", b1.breadth)
b2 = Box((30,10,10))
b2.height = 300
b3 = b2
print("Box 3 Height:", b3.height)

# 7: Buttons class
class Button:
    def __init__(self, name, spaces, border_char):
        self.name = name
        self.spaces = spaces
        self.border = border_char
        self.top_bottom = border_char * (2 + spaces + len(name) + spaces + 1)
        print(f"{name} Button Specifications:")
        print("Button name:", name)
        print(f"Number of the border characters for the top and the bottom: {len(self.top_bottom)}")
        print(f"Number of spaces between the left side border and the first character of the button name: {spaces}")
        print(f"Number of spaces between the right side border and the last character of the button name: {spaces}")
        print(f"Characters representing the borders: {border_char}\n")
        print(self.top_bottom)
        print(border_char + " " * spaces + name + " " * spaces + border_char)
        print(self.top_bottom)
b1 = Button("CANCEL", 10, 'x')
b2 = Button("Notify", 3, '!')
b3 = Button("SAVE PROGRESS", 5, '$')

# 8: Calculator class (instance)
class Calculator:
    def __init__(self):
        print("Let’s Calculate!")
    def add(self): print("Result:", self.a + self.c)
    def subtract(self): print("Result:", self.a - self.c)
    def multiply(self): print("Result:", self.a * self.c)
    def divide(self): print("Result:", self.a / self.c)
calc = Calculator()
calc.a = int(input("Value 1: "))
calc.b = input("Operator: ")
calc.c = int(input("Value 2: "))
if calc.b == "+": calc.add()
elif calc.b == "-": calc.subtract()
elif calc.b == "*": calc.multiply()
elif calc.b == "/": calc.divide()

# 9: Patient class with BMI
class Patient:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.bmi = weight / (height/100) ** 2
    def printDetails(self):
        print(f"Name: {self.name}\nAge: {self.age}\nWeight: {self.weight} kg\nHeight: {self.height} cm\nBMI: {self.bmi}")
p1 = Patient("A", 55, 63.0, 158.0)
p1.printDetails()
print("====================")
p2 = Patient("B", 53, 61.0, 149.0)
p2.printDetails()

# 10: Vehicle class with movement
class Vehicle:
    def __init__(self):
        self.x = 0
        self.y = 0
    def moveUp(self): self.y += 1
    def moveDown(self): self.y -= 1
    def moveRight(self): self.x += 1
    def moveLeft(self): self.x -= 1
    def print_position(self): print((self.x, self.y))
car = Vehicle()
car.print_position()
car.moveUp()
car.print_position()
car.moveLeft()
car.print_position()
car.moveDown()
car.print_position()
car.moveRight()
car.print_position()

# 11: Shape class with area
class Shape:
    def __init__(self, typ, x, y):
        self.typ = typ
        self.x = x
        self.y = y
    def area(self):
        if self.typ in ("Triangle", "Rhombus"):
            print("Area:", self.x * self.y / 2)
        elif self.typ in ("Rectangle", "Square"):
            print("Area:", self.x * self.y)
        else:
            print("Area: Shape unknown")
triangle = Shape("Triangle", 10, 25)
triangle.area()
square = Shape("Square", 10, 10)
square.area()
rhombus = Shape("Rhombus", 18, 25)
rhombus.area()
rectangle = Shape("Rectangle", 15, 30)
rectangle.area()
trapezium = Shape("Trapezium", 15, 30)
trapezium.area()

# 12: Calculator with chaining
class Calculator:
    def __init__(self):
        print("Calculator is ready!")
    def calculate(self, a, b, op):
        self.num1 = a
        self.num2 = b
        self.op = op
        if op == '+': self.res = a + b
        elif op == '-': self.res = a - b
        elif op == '*': self.res = a * b
        elif op == '/': self.res = a / b
        return self.res
    def showCalculation(self):
        print(f"{self.num1} {self.op} {self.num2} = {self.res}")
c1 = Calculator()
val = c1.calculate(10, 20, '+')
print("Returned value:", val)
c1.showCalculation()
val = c1.calculate(val, 10, '-')
print("Returned value:", val)
c1.showCalculation()
val = c1.calculate(val, 5, '*')
print("Returned value:", val)
c1.showCalculation()
val = c1.calculate(val, 16, '/')
print("Returned value:", val)
c1.showCalculation()

# 13: Programmer class
class Programmer:
    def __init__(self, name, lang, exp):
        self.name = name
        self.lan = lang
        self.exp = exp
        print("Horray! A new programmer is born")
    def printDetails(self):
        print(f"Name: {self.name}\nLanguage: {self.lan}\nExperience: {self.exp} years")
    def addExp(self, years):
        print(f"Updating experience of {self.name}")
        self.exp += years
p1 = Programmer("Ethen Hunt", "Java", 10)
p1.printDetails()
p2 = Programmer("James Bond", "C++", 7)
p2.printDetails()
p3 = Programmer("Jon Snow", "Python", 4)
p3.printDetails()
p3.addExp(5)
p3.printDetails()

# 14: Tracing class Test
class Test:
    def __init__(self):
        self.sum = 0
        self.y = 0
    def methodA(self):
        x = 0
        y = 0
        y = y + 7
        x = y + 11
        self.sum = x + y
        print(x , y, self.sum)
    def methodB(self):
        x = 0
        self.y = self.y + 11
        x = x + 33 + self.y
        self.sum = self.sum + x + self.y
        print(x , self.y, self.sum)
t1 = Test()
t1.methodA()
t1.methodA()
t1.methodB()
t1.methodB()

# 15: Tracing class Scope
class Scope:
    def __init__(self):
        self.x, self.y = 1, 100
    def met1(self):
        x = 3
        x = self.x + 1
        self.y = self.y + self.x + 1
        x = self.y + self.met2() + self.y
        print(x, self.y)
    def met2(self):
        y = 0
        print(self.x, y)
        self.x = self.x + y
        self.y = self.y + 200
        return self.x + y
q2 = Scope()
q2.met1()
q2.met2()
q2.met1()
q2.met2()

# 16: Tracing class Test3
class Test3:
    def __init__(self):
        self.sum, self.y = 0, 0
    def methodA(self):
        x, y = 2, 3
        msg = [0]
        msg[0] = 3
        y = self.y + msg[0]
        self.methodB(msg, msg[0])
        x = self.y + msg[0]
        self.sum = x + y + msg[0]
        print(x, y, self.sum)
    def methodB(self, mg2, mg1):
        x = 0
        self.y = self.y + mg2[0]
        x = x + 33 + mg1
        self.sum = self.sum + x + self.y
        mg2[0] = self.y + mg1
        mg1 = mg1 + x + 2
        print(x, self.y, self.sum)
t3 = Test3()
t3.methodA()
t3.methodA()
t3.methodA()
t3.methodA()

# 17: Tracing class Test5
class Test5:
    def __init__(self):
        self.sum, self.y = 0, 0
    def methodA(self):
        x = 0
        z = 0
        while z < 5:
            self.y = self.y + self.sum
            x = self.y + 1
            print(x, self.y, self.sum)
            self.sum = self.sum + self.methodB(x, self.y)
            z += 1
    def methodB(self, m, n):
        x = 0
        sum_val = 0
        self.y = self.y + m
        x = n - 4
        sum_val = sum_val + self.y
        print(x, self.y, sum_val)
        return self.sum
t5 = Test5()
t5.methodA()
