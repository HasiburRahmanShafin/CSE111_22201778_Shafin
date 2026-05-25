# LAB-2: Function Definitions

# 1: Fractional part of division
def frac(a, b):
    if a == 0 or b == 0:
        return 0
    return (a / b) % 1
print(frac(5, 2))

# 2: BMI calculator
def BMI(height_cm, weight_kg):
    h = height_cm / 100
    bmi = weight_kg / (h ** 2)
    if bmi < 18.5:
        status = "Underweight"
    elif bmi <= 24.9:
        status = "Normal"
    elif bmi <= 30:
        status = "Overweight"
    else:
        status = "Obese"
    print(f"Score is {bmi:.1f}. You are {status}")
BMI(152, 48)

# 3: Sum of multiples of c in range [a, b)
def sum_multiples(a, b, c):
    total = 0
    for i in range(a, b):
        if i % c == 0:
            total += i
    return total
print(sum_multiples(0, 10, 2))

# 4: Burger order with delivery
def burger_cost(item, location="Mohakhali"):
    prices = {"BBQ Chicken Cheese Burger": 250, "Beef Burger": 170, "Naga Drums": 200}
    cost = prices.get(item, 0)
    cost += cost * 0.08  # tax
    if location == "Mohakhali" or location == "":
        cost += 40
    else:
        cost += 60
    return cost
burg = input()
loc = input()
print(burger_cost(burg, loc))

# 5: Replace email domain
def replace_domain(email, new_domain, old_domain="Unchanged"):
    if new_domain not in email:
        at_pos = email.find('@')
        new_email = email[:at_pos+1] + new_domain
        print(f"Changed: {new_email}")
    else:
        print(f"Unchanged: {email}")
replace_domain('alice@kaaj.com', 'sheba.xyz', 'kaaj.com')
replace_domain('bob@sheba.xyz', 'sheba.xyz')
replace_domain('tawsif@nsu.bba', 'bracu.cse', 'nsu.bba')
replace_domain('omar@du.math', 'bu.cse', 'du.math')

# 6: Count vowels
def count_vowels(name):
    vowels = "aeiouAEIOU"
    found = [ch for ch in name if ch in vowels]
    if found:
        print(f"Vowels: {','.join(found)}. Total number of vowels: {len(found)}")
    else:
        print("No vowels in the name")
count_vowels(input())

# 7: Palindrome check (ignoring spaces)
def is_palindrome(s):
    clean = ''.join(ch for ch in s if ch != ' ')
    if clean == clean[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")
is_palindrome("hell0")

# 8: Convert days to years, months, days
def convert_days(days):
    years = days // 365
    months = (days % 365) // 30
    days_left = (days % 365) % 30
    print(f"{years} years, {months} months and {days_left} days")
convert_days(int(input()))

# 9: Capitalize sentences and "i"
def capitalize_text(text):
    result = []
    i = 0
    capitalize_next = True
    while i < len(text):
        ch = text[i]
        if capitalize_next and ch.isalpha():
            result.append(ch.upper())
            capitalize_next = False
        elif ch == '.' or ch == '!' or ch == '?':
            result.append(ch)
            capitalize_next = True
        elif ch == ' ' and i+2 < len(text) and text[i+1] == 'i' and text[i+2] == ' ':
            result.append(ch)
            result.append('I')
            i += 1
            capitalize_next = False
        else:
            result.append(ch)
            if ch == ' ':
                capitalize_next = False
            else:
                capitalize_next = False
        i += 1
    return ''.join(result)
para = input()
print(capitalize_text(para))
