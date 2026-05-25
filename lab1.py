
---

## lab1.py (LAB-1: Strings, Lists, Dictionaries)
```python
# LAB-1: String and List Exercises

# str1: Convert string to upper/lower based on case count
a = input()
up = low = 0
for ch in a:
    if ch.islower():
        low += 1
    elif ch.isupper():
        up += 1
if up > low:
    print(a.upper())
else:
    print(a.lower())

# str2: Check if string is all digits, all letters, or mixed
a = input()
if a.isdigit():
    print("NUMBER")
elif a.isalpha():
    print("WORD")
else:
    print("MIXED")

# str3: Extract substring between first two uppercase letters
a = input()
b = ""
for i in range(len(a)):
    if a[i].isupper():
        for j in range(i+1, len(a)):
            if a[j].isupper():
                break
            b += a[j]
        break
if b == "":
    print("BLANK")
else:
    print(b)

# Alternative: Extract substring between first and second uppercase using indices
a = input()
indices = [i for i, ch in enumerate(a) if ch.isupper()]
if len(indices) >= 2:
    print(a[indices[0]+1:indices[1]])
else:
    print("BLANK")

# str4: Find common characters between two strings
a = input()
b = input()
common = []
for ch in a:
    if ch in b:
        common.append(ch)
for ch in b:
    if ch in a:
        common.append(ch)
if not common:
    print("Nothing in common.")
else:
    print(''.join(common))

# str5: Password strength checker (missing lowercase, uppercase, digit, special)
pw = input()
missing = []
if not any(ch.islower() for ch in pw):
    missing.append("Lowercase character missing")
if not any(ch.isupper() for ch in pw):
    missing.append("Uppercase character missing")
if not any(ch.isdigit() for ch in pw):
    missing.append("Digit missing")
special = "_$#@"
if not any(ch in special for ch in pw):
    missing.append("Special character missing")
if missing:
    print(", ".join(missing))
else:
    print("OK")

# list1: Count occurrences of numbers until STOP
lis = []
while True:
    val = input()
    if val == "STOP":
        break
    lis.append(int(val))
unique = []
for x in lis:
    if x not in unique:
        unique.append(x)
        print(f"{x} - {lis.count(x)} times")

# list2: Find sublist with maximum sum
n = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
max_sum = -float('inf')
best_row = []
for row in matrix:
    s = sum(row)
    if s > max_sum:
        max_sum = s
        best_row = row
print(max_sum)
print(best_row)

# list3: Cartesian product of two lists (element-wise multiplication)
a = list(map(int, input().split()))
b = list(map(int, input().split()))
products = [x*y for x in a for y in b]
print(products)

# list4: UB Jumper check (absolute differences ≤ len-1)
lis = []
while True:
    line = input()
    if line == "STOP":
        break
    arr = list(map(int, line.split()))
    lis.append(arr)
for arr in lis:
    n = len(arr)
    ok = True
    for i in range(n-1):
        if abs(arr[i] - arr[i+1]) > n-1:
            ok = False
            break
    print("UB Jumper" if ok else "Not UB Jumper")

# list5: Count groups of three where height+step ≤ 5
first = list(map(int, input().split()))
n = first[0]
k = first[1]
heights = list(map(int, input().split()))[:n]
count = 0
for h in heights:
    if h + k <= 5:
        count += 1
print(count // 3)

# dic1: Merge two dictionaries and sum values for common keys
dict1_input = input().split(", ")
dict2_input = input().split(", ")
d1 = {}
for item in dict1_input:
    k, v = item.split(": ")
    d1[k] = int(v)
d2 = {}
for item in dict2_input:
    k, v = item.split(": ")
    d2[k] = int(v)
merged = d1.copy()
for k, v in d2.items():
    merged[k] = merged.get(k, 0) + v
print(merged)
values = sorted(set(merged.values()))
print("Values:", tuple(values))

# dic2: Count frequency of inputs until STOP
freq = {}
while True:
    key = input()
    if key == "STOP":
        break
    freq[key] = freq.get(key, 0) + 1
for k, v in freq.items():
    print(f"{k} - {v} times")

# dic3: Invert dictionary (values become keys, keys become lists)
input_str = input().split(", ")
d = {}
for item in input_str:
    k, v = item.split(" : ")
    d.setdefault(v, []).append(k)
print(d)

# dic4: Old phone keypad mapping
keypad = {
    1: ".,?!:", 2: "ABC", 3: "DEF", 4: "GHI", 5: "JKL",
    6: "MNO", 7: "PQRS", 8: "TUV", 9: "WXYZ", 0: " "
}
text = input().upper()
output = ""
for ch in text:
    for num, letters in keypad.items():
        if ch in letters:
            output += str(num) * (letters.index(ch) + 1)
print(output)
