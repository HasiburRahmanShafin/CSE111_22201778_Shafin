# LAB-8: Inheritance and Operator Overloading

# Task-1: ComplexNumber inheriting RealNumber
class RealNumber:
    def __init__(self, r=0):
        self.__realValue = r
    def getRealValue(self): return self.__realValue
    def setRealValue(self, r): self.__realValue = r
    def __str__(self): return 'RealPart: '+str(self.getRealValue())
class ComplexNumber(RealNumber):
    def __init__(self, a=1, b=1):
        super().__init__(float(a))
        self.__imag = float(b)
    def getImaginaryValue(self): return self.__imag
    def setImaginaryValue(self, i): self.__imag = i
    def __str__(self):
        return f"{super().__str__()}\nImaginaryPart: {self.getImaginaryValue()}"
cn1 = ComplexNumber()
print(cn1)
print('---------')
cn2 = ComplexNumber(5,7)
print(cn2)

# Task-2: ComplexNumber with operator overloading (+ and -)
class RealNumber:
    def __init__(self, num=0): self.number = num
    def __add__(self, other): return self.number + other.number
    def __sub__(self, other): return self.number - other.number
    def __str__(self): return str(self.number)
class ComplexNumber(RealNumber):
    def __init__(self, a, b):
        if isinstance(a, RealNumber):
            a = a.number
        if isinstance(b, RealNumber):
            b = b.number
        super().__init__(a)
        self.b = b
    def __add__(self, other):
        real = super().__add__(other)
        imag = self.b + other.b
        return ComplexNumber(real, imag)
    def __sub__(self, other):
        real = super().__sub__(other)
        imag = self.b - other.b
        return ComplexNumber(real, imag)
    def __str__(self):
        sign = '+' if self.b >= 0 else '-'
        imag = abs(self.b)
        return f"{super().__str__()} {sign} {imag}i"
r1 = RealNumber(3)
r2 = RealNumber(5)
print(r1+r2)
cn1 = ComplexNumber(2, 1)
print(cn1)
cn2 = ComplexNumber(r1, 5)
print(cn2)
cn3 = cn1 + cn2
print(cn3)
cn4 = cn1 - cn2
print(cn4)

# Task-3: CheckingAccount inheriting Account
class Account:
    def __init__(self, balance): self._balance = balance
    def getBalance(self): return self._balance
class CheckingAccount(Account):
    numberOfAccount = 0
    def __init__(self, balance=0):
        super().__init__(float(balance))
        CheckingAccount.numberOfAccount += 1
    def __str__(self):
        return f"Account Balance: {self.getBalance()}"
print('Number of Checking Accounts: ', CheckingAccount.numberOfAccount)
print(CheckingAccount())
print(CheckingAccount(100.00))
print(CheckingAccount(200.00))
print('Number of Checking Accounts: ', CheckingAccount.numberOfAccount)

# Task-4: Mango and Jackfruit inheriting Fruit
class Fruit:
    def __init__(self, formalin=False, name=''):
        self.__formalin = formalin
        self.name = name
    def getName(self): return self.name
    def hasFormalin(self): return self.__formalin
class testFruit:
    def test(self, f):
        print('----Printing Detail----')
        if f.hasFormalin():
            print(f"Do not eat the {f.getName()}.")
        else:
            print(f'Eat the {f.getName()}.')
        print(f)
class Mango(Fruit):
    def __init__(self):
        super().__init__(True, "Mango")
    def __str__(self): return f"{self.getName()}s are bad for you"
class Jackfruit(Fruit):
    def __init__(self):
        super().__init__(False, "Jackfruit")
    def __str__(self): return f"{self.getName()}s are good for you"
m = Mango()
j = Jackfruit()
t1 = testFruit()
t1.test(m)
t1.test(j)

# Task-5: ScienceExam inheriting Exam
class Exam:
    def __init__(self, marks):
        self.marks = marks
        self.time = 60
    def examSyllabus(self): return "Maths , English"
    def examParts(self): return "Part 1 - Maths\nPart 2 - English\n"
class ScienceExam(Exam):
    def __init__(self, marks, time, *extra_subjects):
        super().__init__(marks)
        self.time = time
        self.extra = extra_subjects
        self.parts = 2 + len(extra_subjects)
    def __str__(self):
        return f"Marks: {self.marks} Time: {self.time} minutes Number of Parts: {self.parts}"
    def examSyllabus(self):
        base = super().examSyllabus()
        if self.extra:
            base += ", " + ", ".join(self.extra)
        return base
    def examParts(self):
        base = super().examParts()
        for i, sub in enumerate(self.extra, start=3):
            base += f"Part {i} - {sub}\n"
        return base
engineering = ScienceExam(100, 90, "Physics", "HigherMaths")
print(engineering)
print('----------------------------------')
print(engineering.examSyllabus())
print(engineering.examParts())
print('==================================')
architecture = ScienceExam(100, 120, "Physics", "HigherMaths", "Drawing")
print(architecture)
print('----------------------------------')
print(architecture.examSyllabus())
print(architecture.examParts())

# Task-6: Sphere and Cylinder inheriting Shape3D
class Shape3D:
    pi = 3.14159
    def __init__(self, name='Default', radius=0):
        self._area = 0
        self._name = name
        self._height = 'No need'
        self._radius = radius
    def calc_surface_area(self):
        return 2 * Shape3D.pi * self._radius
    def __str__(self):
        return "Radius: "+str(self._radius)
class Sphere(Shape3D):
    def __init__(self, name, radius):
        super().__init__(name, radius)
        print(f"Shape name: {name}, Area Formula: 4 * pi * r * r")
    def calc_surface_area(self):
        self.area = super().calc_surface_area() * 2 * self._radius
    def __str__(self):
        return f"{super().__str__()}, Height: No need\nArea: {self.area}"
class Cylinder(Shape3D):
    def __init__(self, name, radius, height):
        super().__init__(name, radius)
        self._height = height
        print(f"Shape name: {name}, Area Formula: 2 * pi * r * (r + h)")
    def calc_surface_area(self):
        self.area = super().calc_surface_area() * (self._radius + self._height)
    def __str__(self):
        return f"{super().__str__()}, Height: {self._height}\nArea: {self.area}"
sph = Sphere('Sphere', 5)
print('----------------------------------')
sph.calc_surface_area()
print(sph)
print('==================================')
cyl = Cylinder('Cylinder', 5, 10)
print('----------------------------------')
cyl.calc_surface_area()
print(cyl)

# Task-7: PokemonExtra inheriting PokemonBasic
class PokemonBasic:
    def __init__(self, name='Default', hp=0, weakness='None', ptype='Unknown'):
        self.name = name
        self.hit_point = hp
        self.weakness = weakness
        self.type = ptype
    def get_type(self): return 'Main type: ' + self.type
    def get_move(self): return 'Basic move: ' + 'Quick Attack'
    def __str__(self):
        return f"Name: {self.name}, HP: {self.hit_point}, Weakness: {self.weakness}"
class PokemonExtra(PokemonBasic):
    def __init__(self, name, hp, weakness, ptype, sec_type="", other_moves=()):
        super().__init__(name, hp, weakness, ptype)
        self.sec_type = sec_type
        self.other_moves = other_moves
    def get_type(self):
        base = super().get_type()
        if self.sec_type:
            base += f", Secondary type: {self.sec_type}"
        return base
    def get_move(self):
        base = super().get_move()
        if self.other_moves:
            base += "\nOther move: " + ", ".join(self.other_moves)
        return base
print('\n------------Basic Info:--------------')
pk = PokemonBasic()
print(pk)
print(pk.get_type())
print(pk.get_move())
print('\n------------Pokemon 1 Info:-------------')
charmander = PokemonExtra('Charmander', 39, 'Water', 'Fire')
print(charmander)
print(charmander.get_type())
print(charmander.get_move())
print('\n------------Pokemon 2 Info:-------------')
charizard = PokemonExtra('Charizard', 78, 'Water', 'Fire', 'Flying', ('Fire Spin', 'Fire Blaze'))
print(charizard)
print(charizard.get_type())
print(charizard.get_move())

# Task-8: FootBallTeam and CricketTeam inheriting Team
class Team:
    def __init__(self, name):
        self.name = "default"
        self.total_player = 5
    def info(self):
        print("We love sports")
class FootBallTeam(Team):
    def __init__(self, name, sport="Football"):
        super().__init__(name)
        self.name = name
        self.sport = sport
        self.total_player = 11
    def info(self):
        print(f"Our name is {self.name}")
        print(f"We play {self.sport}")
        super().info()
class CricketTeam(FootBallTeam):
    def __init__(self, name):
        super().__init__(name, "Cricket")
class Team_test:
    def check(self, tm):
        print("=========================")
        print("Total Player: ", tm.total_player)
        tm.info()
f = FootBallTeam("Brazil")
c = CricketTeam("Bangladesh")
test = Team_test()
test.check(f)
test.check(c)

# Task-9: Pikachu and Charmander inheriting Pokemon
class Pokemon:
    def __init__(self, p):
        self.pokemon = p
        self.pokemon_type = "Needs to be set"
        self.pokemon_weakness = "Needs to be set"
    def kind(self): return self.pokemon_type
    def weakness(self): return self.pokemon_weakness
    def what_am_i(self): print("I am a Pokemon.")
class Pikachu(Pokemon):
    def __init__(self, name="Pikachu", ptype="Electric", weakness="Ground"):
        super().__init__(name)
        self.pokemon_type = ptype
        self.pokemon_weakness = weakness
    def what_am_i(self):
        super().what_am_i()
        print(f"I am {self.pokemon}")
class Charmander(Pikachu):
    def __init__(self):
        super().__init__("Charmander", "Fire", "Water, Ground and Rock")
pk1 = Pikachu()
print("Pokemon:", pk1.pokemon)
print("Type:", pk1.kind())
print("Weakness:", pk1.weakness())
pk1.what_am_i()
print("========================")
c1 = Charmander()
print("Pokemon:", c1.pokemon)
print("Type:", c1.kind())
print("Weakness:", c1.weakness())
c1.what_am_i()

# Task-10: CSE and EEE inheriting Department
class Department:
    def __init__(self, semester):
        self.semester = semester
        self.name = "Default"
        self.id = -1
    def student_info(self):
        print("Name:", self.name)
        print("ID:", self.id)
    def courses(self, c1, c2, c3):
        print("No courses Approved yet!")
class CSE(Department):
    def __init__(self, name, sid, semester, dept="CSE"):
        super().__init__(semester)
        self.name = name
        self.id = sid
        self.dept = dept
    def courses(self, c1, c2, c3):
        print(f"Courses Approved to this {self.dept} student in {self.semester} semester:\n{c1}\n{c2}\n{c3}")
class EEE(CSE):
    def __init__(self, name, sid, semester):
        super().__init__(name, sid, semester, "EEE")
s1 = CSE("Rahim", 16101328, "Spring2016")
s1.student_info()
s1.courses("CSE110", "MAT110", "ENG101")
print("==================")
s2 = EEE("Tanzim", 18101326, "Spring2018")
s2.student_info()
s2.courses("Mat110", "PHY111", "ENG101")
print("==================")
s3 = CSE("Rudana", 18101326, "Fall2017")
s3.student_info()
s3.courses("CSE111", "PHY101", "MAT120")
print("==================")
s4 = EEE("Zainab", 19201623, "Summer2019")
s4.student_info()
s4.courses("EEE201", "PHY112", "MAT120")

# Task-11: Class A and B tracing
class A:
    def __init__(self):
        self.temp = 4
        self.sum = 1
        self.y = 2
        self.y = self.temp - 2
        self.sum = self.temp + 3
        self.temp -= 2
    def methodA(self, m, n):
        x = 0
        self.y = self.y + m + self.temp
        self.temp += 1
        x = x + 2 + n
        self.sum = self.sum + x + self.y
        print(x, self.y, self.sum)
class B(A):
    def __init__(self, b=None):
        super().__init__()
        self.x = 1
        self.sum = 2
        if b is None:
            self.y = self.temp + 3
            self.sum = 3 + self.temp + 2
            self.temp -= 1
        else:
            self.sum = b.sum
            self.x = b.x
    def methodB(self, m, n):
        y = 0
        y = y + self.y
        self.x = y + 2 + self.temp
        self.methodA(self.x, y)
        self.sum = self.x + y + self.sum
        print(self.x, y, self.sum)
a1 = A()
b1 = B()
b2 = B(b1)
a1.methodA(1, 1)
b1.methodA(1, 2)
b2.methodB(3, 2)

# Task-12: Another A/B tracing
class A:
    temp = 4
    def __init__(self):
        self.sum = 0
        self.y = 0
        self.y = A.temp - 2
        self.sum = A.temp + 1
        A.temp -= 2
    def methodA(self, m, n):
        x = 0
        self.y = self.y + m + (A.temp)
        A.temp += 1
        x = x + 1 + n
        self.sum = self.sum + x + self.y
        print(x, self.y, self.sum)
class B(A):
    x = 0
    def __init__(self, b=None):
        super().__init__()
        self.sum = 0
        if b is None:
            self.y = A.temp + 3
            self.sum = 3 + A.temp + 2
            A.temp -= 2
        else:
            self.sum = b.sum
            B.x = b.x
            b.methodB(2, 3)
    def methodB(self, m, n):
        y = 0
        y = y + self.y
        B.x = self.y + 2 + A.temp
        self.methodA(B.x, y)
        self.sum = B.x + y + self.sum
        print(B.x, y, self.sum)
a1 = A()
b1 = B()
b2 = B(b1)
b1.methodA(1, 2)
b2.methodB(3, 2)

# Task-13: A/B with list modification
class A:
    temp = 3
    def __init__(self):
        self.sum = 0
        self.y = 0
        self.y = A.temp - 1
        self.sum = A.temp + 2
        A.temp -= 2
    def methodA(self, m, n):
        x = 0
        n[0] += 1
        self.y = self.y + m + A.temp
        A.temp += 1
        x = x + 2 + n[0]
        n[0] = self.sum + 2
        print(f"{x} {self.y} {self.sum}")
class B(A):
    x = 1
    def __init__(self, b=None):
        super().__init__()
        self.sum = 2
        if b is None:
            self.y = self.temp + 1
            B.x = 3 + A.temp + self.x
            A.temp -= 2
        else:
            self.sum = self.sum + self.sum
            B.x = b.x + self.x
    def methodB(self, m, n):
        y = [0]
        self.y = y[0] + self.y + m
        B.x = self.y + 2 + self.temp - n
        self.methodA(self.x, y)
        self.sum = self.x + y[0] + self.sum
        print(f"{self.x} {y[0]} {self.sum}")
x = [23]
a1 = A()
b1 = B()
b2 = B(b1)
a1.methodA(1, x)
b2.methodB(3, 2)
a1.methodA(1, x)

# Task-14: Another A/B with updates
class A:
    temp = 7
    def __init__(self):
        self.sum, self.y = 0, 0
        self.y = A.temp - 1
        self.sum = A.temp + 2
        A.temp -= 3
    def methodA(self, m, n):
        x = 4
        n[0] += 1
        self.y = self.y + m + A.temp
        A.temp += 2
        x = x + 3 + n[0]
        n[0] = self.sum + 2
        print(f"{x} {self.y} {self.sum}")
    def get_A_sum(self): return self.sum
    def update_A_y(self, val): self.y = val
class B(A):
    x = 2
    def __init__(self, b=None):
        super().__init__()
        self.sum = 2
        if b is None:
            self.y = self.temp + 1
            B.x = 4 + A.temp + self.x
            A.temp -= 2
        else:
            self.sum = self.sum + self.get_A_sum()
            B.x = b.x + self.x
    def methodB(self, m, n):
        y = [0]
        self.update_A_y(y[0] + self.y + m)
        B.x = self.y + 4 + self.temp - n
        self.methodA(self.x, y)
        self.sum = self.x + y[0] + self.get_A_sum()
        print(f"{self.x} {y[0]} {self.sum}")
x = [32]
a1 = A()
b1 = B()
b2 = B(b1)
a1.methodA(2, x)
b2.methodB(2, 3)
a1.methodA(3, x)
