# Data Mining - HackerRank Python homework
# Solutions to the HackerRank "Python" track exercises.
# Each solution is preceded by a comment with the exercise name.
# Exercises are grouped by the sections of the HackerRank Python track.


# =====================================================================
# INTRODUCTION
# =====================================================================

# ---------------------------------------------------------------------
# Say "Hello, World!" With Python
# ---------------------------------------------------------------------
print("Hello, World!")


# ---------------------------------------------------------------------
# Python If-Else
# ---------------------------------------------------------------------
if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 == 1 or 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")


# ---------------------------------------------------------------------
# Arithmetic Operators
# ---------------------------------------------------------------------
if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a + b)
    print(a - b)
    print(a * b)


# ---------------------------------------------------------------------
# Python: Division
# ---------------------------------------------------------------------
if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a // b)
    print(a / b)


# ---------------------------------------------------------------------
# Loops
# ---------------------------------------------------------------------
if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print(i ** 2)


# ---------------------------------------------------------------------
# Write a function
# ---------------------------------------------------------------------
def is_leap(year):
    leap = False

    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True

    return leap

year = int(input())
print(is_leap(year))


# ---------------------------------------------------------------------
# Print Function
# ---------------------------------------------------------------------
if __name__ == '__main__':
    n = int(input())
    print(*range(1, n + 1), sep='')


# =====================================================================
# BASIC DATA TYPES
# =====================================================================

# ---------------------------------------------------------------------
# List Comprehensions
# ---------------------------------------------------------------------
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print([[i, j, k]
           for i in range(x + 1)
           for j in range(y + 1)
           for k in range(z + 1)
           if i + j + k != n])


# ---------------------------------------------------------------------
# Find the Runner-Up Score!
# ---------------------------------------------------------------------
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    scores = sorted(set(arr))
    print(scores[-2])


# ---------------------------------------------------------------------
# Nested Lists
# ---------------------------------------------------------------------
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    second_lowest = sorted(set(score for name, score in students))[1]

    for name in sorted(name for name, score in students if score == second_lowest):
        print(name)


# ---------------------------------------------------------------------
# Finding the percentage
# ---------------------------------------------------------------------
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    marks = student_marks[query_name]
    average = sum(marks) / len(marks)
    print(f"{average:.2f}")


# ---------------------------------------------------------------------
# Lists
# ---------------------------------------------------------------------
if __name__ == '__main__':
    N = int(input())
    lst = []

    for _ in range(N):
        command, *args = input().split()
        args = list(map(int, args))

        if command == 'print':
            print(lst)
        else:
            getattr(lst, command)(*args)


# ---------------------------------------------------------------------
# Tuples
# (tuple hash computed with the pre-Python-3.8 algorithm,
#  which is what the expected output was generated with)
# ---------------------------------------------------------------------
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    t = tuple(integer_list)

    MASK = (1 << 64) - 1
    x = 0x345678
    mult = 1000003
    length = len(t)
    for item in t:
        length -= 1
        y = hash(item) & MASK
        x = ((x ^ y) * mult) & MASK
        mult = (mult + 82520 + length + length) & MASK
    x = (x + 97531) & MASK
    if x >= 1 << 63:
        x -= 1 << 64
    if x == -1:
        x = -2
    print(x)


# =====================================================================
# STRINGS
# =====================================================================

# ---------------------------------------------------------------------
# sWAP cASE
# ---------------------------------------------------------------------
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# ---------------------------------------------------------------------
# String Split and Join
# ---------------------------------------------------------------------
def split_and_join(line):
    return "-".join(line.split())

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# ---------------------------------------------------------------------
# What's Your Name?
# ---------------------------------------------------------------------
def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# ---------------------------------------------------------------------
# Mutations
# ---------------------------------------------------------------------
def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# ---------------------------------------------------------------------
# Find a string
# ---------------------------------------------------------------------
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)


# ---------------------------------------------------------------------
# String Validators
# ---------------------------------------------------------------------
if __name__ == '__main__':
    s = input()

    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))


# ---------------------------------------------------------------------
# Text Alignment
# ---------------------------------------------------------------------
thickness = int(input())  # This must be an odd number
c = 'H'

# Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

# Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# ---------------------------------------------------------------------
# Text Wrap
# ---------------------------------------------------------------------
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# ---------------------------------------------------------------------
# Designer Door Mat
# ---------------------------------------------------------------------
n, m = map(int, input().split())

for i in range(n // 2):
    print(('.|.' * (2 * i + 1)).center(m, '-'))

print('WELCOME'.center(m, '-'))

for i in range(n // 2 - 1, -1, -1):
    print(('.|.' * (2 * i + 1)).center(m, '-'))


# ---------------------------------------------------------------------
# String Formatting
# ---------------------------------------------------------------------
def print_formatted(number):
    width = len(bin(number)) - 2
    for i in range(1, number + 1):
        print(f"{i:>{width}d} {i:>{width}o} {i:>{width}X} {i:>{width}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# ---------------------------------------------------------------------
# Alphabet Rangoli
# ---------------------------------------------------------------------
import string

def print_rangoli(size):
    letters = string.ascii_lowercase
    width = 4 * size - 3
    lines = []

    for i in range(size):
        left = letters[size - 1:i:-1]
        row = '-'.join(left + letters[i:size])
        lines.append(row.center(width, '-'))

    print('\n'.join(lines[::-1] + lines[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


# ---------------------------------------------------------------------
# Capitalize!
# ---------------------------------------------------------------------
import os

def solve(s):
    return ' '.join(word[:1].upper() + word[1:] for word in s.split(' '))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


# ---------------------------------------------------------------------
# The Minion Game
# ---------------------------------------------------------------------
def minion_game(string):
    vowels = 'AEIOU'
    n = len(string)
    kevin = 0
    stuart = 0

    for i, letter in enumerate(string):
        if letter in vowels:
            kevin += n - i
        else:
            stuart += n - i

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)


# ---------------------------------------------------------------------
# Merge the Tools!
# ---------------------------------------------------------------------
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        block = string[i:i + k]
        print(''.join(dict.fromkeys(block)))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


# =====================================================================
# SETS
# =====================================================================

# ---------------------------------------------------------------------
# Introduction to Sets
# ---------------------------------------------------------------------
def average(array):
    distinct = set(array)
    return round(sum(distinct) / len(distinct), 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


# ---------------------------------------------------------------------
# No Idea!
# ---------------------------------------------------------------------
input()
arr = input().split()
a = set(input().split())
b = set(input().split())

print(sum((x in a) - (x in b) for x in arr))


# ---------------------------------------------------------------------
# Symmetric Difference
# ---------------------------------------------------------------------
input()
a = set(map(int, input().split()))
input()
b = set(map(int, input().split()))

for x in sorted(a.symmetric_difference(b)):
    print(x)


# ---------------------------------------------------------------------
# Set .add()
# ---------------------------------------------------------------------
n = int(input())
stamps = set()

for _ in range(n):
    stamps.add(input().strip())

print(len(stamps))


# ---------------------------------------------------------------------
# Set .discard(), .remove() & .pop()
# ---------------------------------------------------------------------
n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    command, *args = input().split()
    if command == 'pop':
        s.remove(min(s))
    else:
        getattr(s, command)(*map(int, args))

print(sum(s))


# ---------------------------------------------------------------------
# Set .union() Operation
# ---------------------------------------------------------------------
input()
english = set(input().split())
input()
french = set(input().split())

print(len(english.union(french)))


# ---------------------------------------------------------------------
# Set .intersection() Operation
# ---------------------------------------------------------------------
input()
english = set(input().split())
input()
french = set(input().split())

print(len(english.intersection(french)))


# ---------------------------------------------------------------------
# Set .difference() Operation
# ---------------------------------------------------------------------
input()
english = set(input().split())
input()
french = set(input().split())

print(len(english.difference(french)))


# ---------------------------------------------------------------------
# Set .symmetric_difference() Operation
# ---------------------------------------------------------------------
input()
english = set(input().split())
input()
french = set(input().split())

print(len(english.symmetric_difference(french)))


# ---------------------------------------------------------------------
# Set Mutations
# ---------------------------------------------------------------------
input()
a = set(map(int, input().split()))

for _ in range(int(input())):
    operation, _ = input().split()
    other = set(map(int, input().split()))
    getattr(a, operation)(other)

print(sum(a))


# ---------------------------------------------------------------------
# The Captain's Room
# ---------------------------------------------------------------------
k = int(input())
rooms = list(map(int, input().split()))

unique = set(rooms)
print((k * sum(unique) - sum(rooms)) // (k - 1))


# ---------------------------------------------------------------------
# Check Subset
# ---------------------------------------------------------------------
for _ in range(int(input())):
    input()
    a = set(input().split())
    input()
    b = set(input().split())

    print(a.issubset(b))


# ---------------------------------------------------------------------
# Check Strict Superset
# ---------------------------------------------------------------------
a = set(input().split())
n = int(input())

print(all(a > set(input().split()) for _ in range(n)))


# =====================================================================
# COLLECTIONS
# =====================================================================

# ---------------------------------------------------------------------
# collections.Counter()
# ---------------------------------------------------------------------
from collections import Counter

input()
stock = Counter(map(int, input().split()))
earned = 0

for _ in range(int(input())):
    size, price = map(int, input().split())
    if stock[size] > 0:
        stock[size] -= 1
        earned += price

print(earned)


# ---------------------------------------------------------------------
# DefaultDict Tutorial
# ---------------------------------------------------------------------
from collections import defaultdict

n, m = map(int, input().split())

positions = defaultdict(list)
for i in range(1, n + 1):
    positions[input().strip()].append(i)

for _ in range(m):
    word = input().strip()
    if word in positions:
        print(*positions[word])
    else:
        print(-1)


# ---------------------------------------------------------------------
# Collections.namedtuple()
# ---------------------------------------------------------------------
from collections import namedtuple
n, Student = int(input()), namedtuple('Student', input().split())
students = [Student(*input().split()) for _ in range(n)]
print(f"{sum(int(s.MARKS) for s in students) / n:.2f}")


# ---------------------------------------------------------------------
# Collections.OrderedDict()
# ---------------------------------------------------------------------
from collections import OrderedDict

n = int(input())
totals = OrderedDict()

for _ in range(n):
    *name_parts, price = input().split()
    name = ' '.join(name_parts)
    totals[name] = totals.get(name, 0) + int(price)

for name, net_price in totals.items():
    print(name, net_price)


# ---------------------------------------------------------------------
# Word Order
# ---------------------------------------------------------------------
from collections import Counter

n = int(input())
counts = Counter(input().strip() for _ in range(n))

print(len(counts))
print(*counts.values())


# ---------------------------------------------------------------------
# Collections.deque()
# ---------------------------------------------------------------------
from collections import deque

d = deque()
for _ in range(int(input())):
    method, *args = input().split()
    getattr(d, method)(*args)

print(*d)


# ---------------------------------------------------------------------
# Company Logo
# ---------------------------------------------------------------------
from collections import Counter

if __name__ == '__main__':
    s = input()

    counts = Counter(s)
    top_three = sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:3]

    for char, count in top_three:
        print(char, count)


# ---------------------------------------------------------------------
# Piling Up!
# ---------------------------------------------------------------------
from collections import deque

for _ in range(int(input())):
    input()  # number of cubes, not needed
    cubes = deque(map(int, input().split()))

    top = float('inf')
    possible = True

    while cubes:
        if cubes[0] >= cubes[-1]:
            current = cubes.popleft()
        else:
            current = cubes.pop()

        if current > top:
            possible = False
            break
        top = current

    print('Yes' if possible else 'No')


# =====================================================================
# DATE AND TIME
# =====================================================================

# ---------------------------------------------------------------------
# Calendar Module
# ---------------------------------------------------------------------
import calendar

month, day, year = map(int, input().split())

print(calendar.day_name[calendar.weekday(year, month, day)].upper())


# ---------------------------------------------------------------------
# Time Delta
# ---------------------------------------------------------------------
import os
from datetime import datetime

def time_delta(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'
    d1 = datetime.strptime(t1, fmt)
    d2 = datetime.strptime(t2, fmt)
    return str(int(abs((d1 - d2).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()


# =====================================================================
# ERRORS AND EXCEPTIONS
# =====================================================================

# ---------------------------------------------------------------------
# Exceptions
# ---------------------------------------------------------------------
for _ in range(int(input())):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:", e)


# ---------------------------------------------------------------------
# Incorrect Regex
# (Python 3.11+ accepts possessive quantifiers and atomic groups,
#  so they are rejected explicitly to match the expected output)
# ---------------------------------------------------------------------
import re

for _ in range(int(input())):
    s = input()
    try:
        re.compile(s)
        new_syntax = re.search(r'(?<!\\)[*+?}]\+', s) or '(?>' in s
        print(not new_syntax)
    except re.error:
        print(False)


# =====================================================================
# CLASSES
# =====================================================================

# ---------------------------------------------------------------------
# Class 2 - Find the Torsional Angle
# ---------------------------------------------------------------------
import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        return self.x * no.x + self.y * no.y + self.z * no.z

    def cross(self, no):
        return Points(self.y * no.z - self.z * no.y,
                      self.z * no.x - self.x * no.z,
                      self.x * no.y - self.y * no.x)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))


# =====================================================================
# BUILT-INS
# =====================================================================

# ---------------------------------------------------------------------
# Zipped!
# ---------------------------------------------------------------------
n, x = map(int, input().split())
subjects = [map(float, input().split()) for _ in range(x)]

for marks in zip(*subjects):
    print(f"{sum(marks) / x:.1f}")


# ---------------------------------------------------------------------
# Input()
# ---------------------------------------------------------------------
x, k = map(int, input().split())
print(eval(input()) == k)


# ---------------------------------------------------------------------
# Python Evaluation
# ---------------------------------------------------------------------
var = input()
eval(var)


# ---------------------------------------------------------------------
# Athlete Sort
# ---------------------------------------------------------------------
if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    for row in sorted(arr, key=lambda row: row[k]):
        print(*row)


# ---------------------------------------------------------------------
# ginortS
# ---------------------------------------------------------------------
s = input()

print(''.join(sorted(s, key=lambda c: (c.isdigit(),
                                       c.isupper(),
                                       c.isdigit() and int(c) % 2 == 0,
                                       c))))


# ---------------------------------------------------------------------
# Any or All
# ---------------------------------------------------------------------
n = int(input())
nums = input().split()
print(all(int(x) > 0 for x in nums) and any(x == x[::-1] for x in nums))


# =====================================================================
# PYTHON FUNCTIONALS
# =====================================================================

# ---------------------------------------------------------------------
# Map and Lambda Function
# ---------------------------------------------------------------------
cube = lambda x: x ** 3

def fibonacci(n):
    fib = []
    a, b = 0, 1
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b
    return fib

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


# ---------------------------------------------------------------------
# Validating Email Addresses With a Filter
# ---------------------------------------------------------------------
def fun(s):
    import re
    return bool(re.fullmatch(r'[A-Za-z0-9_-]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}', s))

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)


# ---------------------------------------------------------------------
# Reduce Function
# ---------------------------------------------------------------------
from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)


# =====================================================================
# REGEX AND PARSING
# =====================================================================

# ---------------------------------------------------------------------
# Detect Floating Point Number
# ---------------------------------------------------------------------
import re

for _ in range(int(input())):
    print(bool(re.match(r'^[+-]?\d*\.\d+$', input().strip())))


# ---------------------------------------------------------------------
# Re.split()
# ---------------------------------------------------------------------
regex_pattern = r"[,.]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))


# ---------------------------------------------------------------------
# Group(), Groups() & Groupdict()
# ---------------------------------------------------------------------
import re

m = re.search(r'([a-zA-Z0-9])\1', input())
print(m.group(1) if m else -1)


# ---------------------------------------------------------------------
# Re.findall() & Re.finditer()
# ---------------------------------------------------------------------
import re

consonants = 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
vowels = 'aeiouAEIOU'

matches = re.findall(rf'(?<=[{consonants}])[{vowels}]{{2,}}(?=[{consonants}])', input())

print('\n'.join(matches) if matches else -1)


# ---------------------------------------------------------------------
# Re.start() & Re.end()
# ---------------------------------------------------------------------
import re

s = input()
k = input()

matches = list(re.finditer(rf'(?=({re.escape(k)}))', s))

if matches:
    for m in matches:
        print((m.start(1), m.end(1) - 1))
else:
    print((-1, -1))


# ---------------------------------------------------------------------
# Regex Substitution
# ---------------------------------------------------------------------
import re

def replace(match):
    return 'and' if match.group(0) == '&&' else 'or'

for _ in range(int(input())):
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', replace, input()))


# ---------------------------------------------------------------------
# Validating Roman Numerals
# ---------------------------------------------------------------------
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))


# ---------------------------------------------------------------------
# Validating phone numbers
# ---------------------------------------------------------------------
import re

for _ in range(int(input())):
    number = input().strip()
    print('YES' if re.fullmatch(r'[789]\d{9}', number) else 'NO')


# ---------------------------------------------------------------------
# Validating and Parsing Email Addresses
# ---------------------------------------------------------------------
import re
import email.utils

pattern = re.compile(r'^[A-Za-z][A-Za-z0-9._-]*@[A-Za-z]+\.[A-Za-z]{1,3}$')

n = int(input())
for _ in range(n):
    name, address = email.utils.parseaddr(input())
    if pattern.match(address):
        print(email.utils.formataddr((name, address)))


# ---------------------------------------------------------------------
# Hex Color Code
# ---------------------------------------------------------------------
import re

pattern = re.compile(r'#(?:[0-9a-fA-F]{3}){1,2}(?![0-9a-fA-F])')
inside = False

for _ in range(int(input())):
    line = input()
    if '{' in line:
        inside = True
    elif '}' in line:
        inside = False
    elif inside:
        for color in pattern.findall(line):
            print(color)


# ---------------------------------------------------------------------
# HTML Parser - Part 1
# ---------------------------------------------------------------------
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def print_attrs(self, attrs):
        for name, value in attrs:
            print(f"-> {name} > {value}")

    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        self.print_attrs(attrs)

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        self.print_attrs(attrs)

n = int(input())
html = "\n".join(input() for _ in range(n))

parser = MyHTMLParser()
parser.feed(html)
parser.close()


# ---------------------------------------------------------------------
# HTML Parser - Part 2
# ---------------------------------------------------------------------
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)

    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)

html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()


# ---------------------------------------------------------------------
# Detect HTML Tags, Attributes and Attribute Values
# ---------------------------------------------------------------------
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print(f"-> {name} > {value}")

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

n = int(input())
html = "\n".join(input() for _ in range(n))

parser = MyHTMLParser()
parser.feed(html)
parser.close()


# ---------------------------------------------------------------------
# Validating UID
# ---------------------------------------------------------------------
import re

t = int(input())
for _ in range(t):
    uid = input().strip()

    valid = (
        len(uid) == 10 and
        re.fullmatch(r'[A-Za-z0-9]+', uid) is not None and
        len(set(uid)) == len(uid) and
        len(re.findall(r'[A-Z]', uid)) >= 2 and
        len(re.findall(r'[0-9]', uid)) >= 3
    )

    print('Valid' if valid else 'Invalid')


# ---------------------------------------------------------------------
# Validating Credit Card Numbers
# ---------------------------------------------------------------------
import re

valid_format = re.compile(r'^[456]\d{3}(-?\d{4}){3}$')
repeated = re.compile(r'(\d)\1{3}')

for _ in range(int(input())):
    card = input().strip()

    if valid_format.match(card) and not repeated.search(card.replace('-', '')):
        print('Valid')
    else:
        print('Invalid')


# ---------------------------------------------------------------------
# Validating Postal Codes
# ---------------------------------------------------------------------
regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"


import re
P = input()

print (bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


# ---------------------------------------------------------------------
# Matrix Script
# ---------------------------------------------------------------------
import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decoded = ''.join(row[j] for j in range(m) for row in matrix)
print(re.sub(r'(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])', ' ', decoded))


# =====================================================================
# XML
# =====================================================================

# ---------------------------------------------------------------------
# XML 1 - Find the Score
# ---------------------------------------------------------------------
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    return sum(len(elem.attrib) for elem in node.iter())

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


# ---------------------------------------------------------------------
# XML2 - Find the Maximum Depth
# ---------------------------------------------------------------------
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    maxdepth = max(maxdepth, level)
    for child in elem:
        depth(child, level)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)


# =====================================================================
# CLOSURES AND DECORATORS
# =====================================================================

# ---------------------------------------------------------------------
# Standardize Mobile Number Using Decorators
# ---------------------------------------------------------------------
def wrapper(f):
    def fun(l):
        f(['+91 ' + n[-10:-5] + ' ' + n[-5:] for n in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)


# ---------------------------------------------------------------------
# Decorators 2 - Name Directory
# ---------------------------------------------------------------------
import operator

def person_lister(f):
    def inner(people):
        return map(f, sorted(people, key=lambda person: int(person[2])))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


# =====================================================================
# NUMPY
# =====================================================================

# ---------------------------------------------------------------------
# Arrays
# ---------------------------------------------------------------------
import numpy

def arrays(arr):
    return numpy.array(arr[::-1], float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


# ---------------------------------------------------------------------
# Shape and Reshape
# ---------------------------------------------------------------------
import numpy

arr = numpy.array(input().split(), int)
print(numpy.reshape(arr, (3, 3)))


# ---------------------------------------------------------------------
# Transpose and Flatten
# ---------------------------------------------------------------------
import numpy

n, m = map(int, input().split())
arr = numpy.array([input().split() for _ in range(n)], int)

print(numpy.transpose(arr))
print(arr.flatten())


# ---------------------------------------------------------------------
# Concatenate
# ---------------------------------------------------------------------
import numpy

n, m, p = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(m)], int)

print(numpy.concatenate((a, b), axis=0))


# ---------------------------------------------------------------------
# Zeros and Ones
# ---------------------------------------------------------------------
import numpy

shape = tuple(map(int, input().split()))

print(numpy.zeros(shape, dtype=int))
print(numpy.ones(shape, dtype=int))


# ---------------------------------------------------------------------
# Eye and Identity
# ---------------------------------------------------------------------
import numpy
numpy.set_printoptions(legacy='1.13')

n, m = map(int, input().split())
print(numpy.eye(n, m))


# ---------------------------------------------------------------------
# Array Mathematics
# ---------------------------------------------------------------------
import numpy

n, m = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a ** b)


# ---------------------------------------------------------------------
# Floor, Ceil and Rint
# ---------------------------------------------------------------------
import numpy
numpy.set_printoptions(legacy='1.13')

a = numpy.array(input().split(), float)

print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))


# ---------------------------------------------------------------------
# Sum and Prod
# ---------------------------------------------------------------------
import numpy

n, m = map(int, input().split())
arr = numpy.array([input().split() for _ in range(n)], int)

print(numpy.prod(numpy.sum(arr, axis=0)))


# ---------------------------------------------------------------------
# Min and Max
# ---------------------------------------------------------------------
import numpy

n, m = map(int, input().split())
arr = numpy.array([input().split() for _ in range(n)], int)

print(numpy.max(numpy.min(arr, axis=1)))


# ---------------------------------------------------------------------
# Mean, Var, and Std
# ---------------------------------------------------------------------
import numpy

n, m = map(int, input().split())
arr = numpy.array([input().split() for _ in range(n)], int)

print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(round(numpy.std(arr), 11))


# ---------------------------------------------------------------------
# Dot and Cross
# ---------------------------------------------------------------------
import numpy

n = int(input())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)

print(numpy.dot(a, b))


# ---------------------------------------------------------------------
# Inner and Outer
# ---------------------------------------------------------------------
import numpy

a = numpy.array(input().split(), int)
b = numpy.array(input().split(), int)

print(numpy.inner(a, b))
print(numpy.outer(a, b))


# ---------------------------------------------------------------------
# Polynomials
# ---------------------------------------------------------------------
import numpy

coefficients = list(map(float, input().split()))
x = float(input())

print(numpy.polyval(coefficients, x))


# ---------------------------------------------------------------------
# Linear Algebra
# ---------------------------------------------------------------------
import numpy

n = int(input())
a = numpy.array([input().split() for _ in range(n)], float)

print(round(numpy.linalg.det(a), 2))


# =====================================================================
# OTHER PROBLEMS
# =====================================================================

# ---------------------------------------------------------------------
# Birthday Cake Candles
# ---------------------------------------------------------------------
import os

def birthdayCakeCandles(candles):
    return candles.count(max(candles))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


# ---------------------------------------------------------------------
# Number Line Jumps
# ---------------------------------------------------------------------
import os

def kangaroo(x1, v1, x2, v2):
    if v1 > v2 and (x2 - x1) % (v1 - v2) == 0:
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


# ---------------------------------------------------------------------
# Viral Advertising
# ---------------------------------------------------------------------
import os

def viralAdvertising(n):
    shared = 5
    cumulative = 0
    for _ in range(n):
        liked = shared // 2
        cumulative += liked
        shared = liked * 3
    return cumulative

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


# ---------------------------------------------------------------------
# Recursive Digit Sum
# ---------------------------------------------------------------------
import os

def superDigit(n, k):
    total = sum(int(d) for d in n) * k
    if total < 10:
        return total
    return superDigit(str(total), 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


# ---------------------------------------------------------------------
# Insertion Sort - Part 1
# ---------------------------------------------------------------------
def insertionSort1(n, arr):
    e = arr[-1]
    i = n - 2
    while i >= 0 and arr[i] > e:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1
    arr[i + 1] = e
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


# ---------------------------------------------------------------------
# Insertion Sort - Part 2
# ---------------------------------------------------------------------
def insertionSort2(n, arr):
    for i in range(1, n):
        e = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > e:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = e
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
