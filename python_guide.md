# The Complete Python Guide
### From Zero to Python Wizard — Everything You Need

---

## How to Use This Guide

Read it top to bottom once to build the mental map.  
Then use it as a reference when you get stuck or forget something.  
Every section explains the **what**, the **how**, and the **why behind it**.

---

# PART 1 — Python Philosophy

Python has a design philosophy called **The Zen of Python**. Run `import this` in any Python file to see it. The most important lines:

```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Readability counts.
There should be one obvious way to do it.
```

This is not decoration. It is the actual reason Python looks the way it does. Every style rule, every built-in choice, every library convention follows from this. When you are unsure how to write something, ask: is this readable? Is this obvious? Is this simple?

---

# PART 2 — Environment Setup

## Installing Python

```bash
# check if you have it
python3 --version

# install via Homebrew (Mac)
brew install python3

# install via pyenv (manage multiple versions)
brew install pyenv
pyenv install 3.12.0
pyenv global 3.12.0
```

## Virtual Environments

Every project should have its own isolated environment. Without this, packages from different projects conflict.

```bash
# create
python3 -m venv venv

# activate (Mac/Linux)
source venv/bin/activate

# you are now inside the env — your terminal shows:
(venv) $

# install packages
pip install pyyaml cbor2

# save what this project needs
pip freeze > requirements.txt

# anyone else can reproduce your environment
pip install -r requirements.txt

# leave the environment
deactivate
```

## Package Management

```bash
pip install package_name        # install
pip uninstall package_name      # remove
pip list                        # see all installed
pip show pyyaml                 # info about one package
pip install --upgrade pyyaml    # upgrade
```

---

# PART 3 — Data Types

## The Basic Types

Every value in Python has a type. This is fundamental — the type determines what you can do with a value.

```python
# int — whole numbers
age = 26
port = 5432
negative = -10

# float — decimal numbers
temp = 22.4
pi = 3.14159

# str — text, always in quotes
name = "Fahid"
city = 'Tampere'
empty = ""

# bool — only two possible values
active = True
enabled = False

# None — absence of any value (not zero, not empty — literally nothing)
result = None
email = None
```

## Type Checking

```python
type(42)           # <class 'int'>
type("hello")      # <class 'str'>

# always prefer isinstance over type ==
isinstance(42, int)              # True
isinstance("hi", str)            # True
isinstance("hi", (str, bytes))   # True — check multiple types at once
```

## Type Conversion

```python
int("42")           # 42
int(3.9)            # 3   — truncates, does NOT round
float("3.14")       # 3.14
str(100)            # "100"
bool(0)             # False
bool(1)             # True
bool("")            # False
bool("hello")       # True
bool(None)          # False
bool([])            # False
bool([1, 2])        # True
list("abc")         # ["a", "b", "c"]
list((1, 2, 3))     # [1, 2, 3]
tuple([1, 2, 3])    # (1, 2, 3)
set([1, 2, 2, 3])   # {1, 2, 3}
```

## Truthiness — What Counts as True or False

```python
# Falsy — evaluates to False in conditions
False, None, 0, 0.0, "", [], {}, set(), ()

# Truthy — everything else
True, 1, "hello", [1], {"a": 1}

# this is why you can write:
if data:           # instead of: if len(data) > 0
    process(data)

if not result:     # instead of: if result is None or result == ""
    handle_missing()
```

---

# PART 4 — Variables, Naming, and Operators

## Naming Rules

```python
# snake_case for variables and functions
user_name = "Fahid"
def get_config(): ...

# PascalCase for classes
class ConfigLoader: ...

# UPPER_CASE for constants
MAX_RETRIES = 3
REQUIRED_FIELDS = ["name", "email"]

# leading underscore — internal/private convention
_internal_value = 42

# double underscore — name-mangled, truly private in classes
self.__balance = 1000
```

## Operators

```python
# arithmetic
5 + 2    # 7
5 - 2    # 3
5 * 2    # 10
5 / 2    # 2.5   — always float
5 // 2   # 2     — floor division, drops decimal
5 % 2    # 1     — modulo, remainder
5 ** 2   # 25    — power

# comparison — always returns bool
==   !=   <   >   <=   >=

# logical
and    or    not

# identity — checks if same object in memory
is        is not

# membership — checks if value exists in collection
in        not in

# augmented assignment
x += 1    # same as x = x + 1
x -= 1
x *= 2
x //= 2
```

## String Operations

```python
name = "fahid"

name.upper()           # "FAHID"
name.lower()           # "fahid"
name.capitalize()      # "Fahid"
name.strip()           # remove whitespace from both ends
name.lstrip()          # left only
name.rstrip()          # right only
name.replace("a", "e") # "fehid"
name.split(",")        # split into list by delimiter
",".join(["a","b","c"]) # "a,b,c"
name.startswith("fa")  # True
name.endswith("id")    # True
name.isdigit()         # False
"42".isdigit()         # True
len(name)              # 5

# f-strings — the modern way to build strings
age = 26
city = "Tampere"
print(f"My name is {name}, I am {age} years old, living in {city}")
print(f"Pi is approximately {3.14159:.2f}")   # format to 2 decimals
print(f"Count: {1000000:,}")                  # 1,000,000
```

---

# PART 5 — Control Flow

## if / elif / else

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

# one-liner (ternary) — use only when truly simple
grade = "pass" if score >= 60 else "fail"
```

## for Loops

```python
# loop over a list
for name in ["alice", "bob", "charlie"]:
    print(name)

# loop with index
for i, name in enumerate(["alice", "bob", "charlie"]):
    print(i, name)    # 0 alice, 1 bob, 2 charlie

# loop over a dict
config = {"host": "localhost", "port": 5432}
for key, value in config.items():
    print(key, value)

# loop a number of times
for i in range(5):       # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 8, 2): # 2, 4, 6
    print(i)
```

## while Loops

```python
count = 0
while count < 5:
    print(count)
    count += 1

# loop until condition breaks
while True:
    data = get_next_packet()
    if data is None:
        break
    process(data)
```

## break / continue / pass

```python
# break — exit the loop immediately
for n in range(10):
    if n == 5:
        break        # stops at 5, never reaches 6-9

# continue — skip this iteration, go to next
for n in range(10):
    if n % 2 == 0:
        continue     # skip even numbers
    print(n)         # prints 1, 3, 5, 7, 9

# pass — do nothing, placeholder
def load_config():
    pass             # fill in later
```

---

# PART 5b — Loops and Conditions — Deep Dive

Most people get lost with loops and conditions not because they don't understand them, but because they lose track of **what is happening at each step** when code gets bigger. This section fixes that.

---

## The Mental Model

**A condition is just Python asking a yes/no question.**
**A loop is just Python doing the same thing multiple times, one item at a time.**

That is all they are.

---

## Conditions — Traced Step by Step

```python
age = 20

if age >= 18:
    print("adult")
else:
    print("minor")
```

What Python does in its head:

```
1. Look at age → it is 20
2. Ask: is 20 >= 18?  YES
3. Go into the if block → print "adult"
4. Skip the else block entirely
5. Continue
```

Change age to 15 and the path flips:

```
1. Look at age → it is 15
2. Ask: is 15 >= 18?  NO
3. Skip the if block
4. Go into the else block → print "minor"
```

### elif — Python stops at the first YES

```python
score = 72

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

```
Is 72 >= 90?  NO  → skip
Is 72 >= 80?  NO  → skip
Is 72 >= 70?  YES → grade = "C", stop checking, jump out
```

The `else` only fires if **every condition above it was NO**.

---

## for Loop — Traced Step by Step

```python
names = ["Alice", "Bob", "Charlie"]

for name in names:
    print(name)
```

```
Round 1:  name = "Alice"    → print "Alice"
Round 2:  name = "Bob"      → print "Bob"
Round 3:  name = "Charlie"  → print "Charlie"
Nothing left → loop ends
```

`name` is just a temporary container. Every round it gets the next item.

### Looping over a dict

```python
user = {"name": "Fahid", "age": 26, "city": "Tampere"}

for key, value in user.items():
    print(key, "→", value)
```

```
Round 1:  key = "name",  value = "Fahid"    → "name → Fahid"
Round 2:  key = "age",   value = 26         → "age → 26"
Round 3:  key = "city",  value = "Tampere"  → "city → Tampere"
```

`.items()` gives you pairs. `for key, value` unpacks each pair into two variables automatically.

---

## Condition Inside a Loop — Full Manual Trace

This is the pattern that confuses people most. Trace it one round at a time.

```python
data = {"name": "Fahid", "email": None, "city": "Tampere", "phone": ""}

result = {}
for key, value in data.items():
    if value is not None and value != "":
        result[key] = value
```

```
result starts as: {}

--- Round 1 ---
key = "name", value = "Fahid"
  Is "Fahid" not None?  YES
  Is "Fahid" != ""?     YES
  Both YES → result["name"] = "Fahid"
  result: {"name": "Fahid"}

--- Round 2 ---
key = "email", value = None
  Is None not None?  NO  ← fails immediately
  Skip.
  result: {"name": "Fahid"}

--- Round 3 ---
key = "city", value = "Tampere"
  Is "Tampere" not None?  YES
  Is "Tampere" != ""?     YES
  Both YES → result["city"] = "Tampere"
  result: {"name": "Fahid", "city": "Tampere"}

--- Round 4 ---
key = "phone", value = ""
  Is "" not None?  YES
  Is "" != ""?     NO  ← fails here
  Skip.
  result: {"name": "Fahid", "city": "Tampere"}

Loop ends.
```

---

## Loop Inside a Function Inside a Class — How to Read It

When you see a loop buried inside a class and function, your brain tries to read all of it at once. Don't. **Read it in layers.**

```python
class DataCleaner:
    def __init__(self, data):
        self.data = data

    def remove_empty(self):
        result = {}
        for key, value in self.data.items():
            if value is not None and value != "":
                result[key] = value
        return result
```

**Layer 1 — ignore the class, what does the function do?**
Takes data in, returns cleaned result.

**Layer 2 — ignore the condition, what does the loop do?**
Goes through every key-value pair in the data.

**Layer 3 — what does the condition do?**
For each pair, keeps it only if the value is real.

**All together in one sentence:**
> For every key-value pair, if the value is not empty, keep it.

`self.data` just means "the data this object was created with." Replace it mentally with a plain variable and it reads identically to any other loop.

---

## Nested Conditions — Read Outer First, Then Inner

```python
for value in [22, -5, 150, 37]:
    if isinstance(value, int):          # outer: is it a number?
        if 0 <= value <= 100:           # inner: is it in range?
            print(f"{value} is valid")
        else:
            print(f"{value} is out of range")
    else:
        print(f"{value} is not a number")
```

```
22  → is int? YES → 0 <= 22 <= 100?  YES → "22 is valid"
-5  → is int? YES → 0 <= -5 <= 100?  NO  → "-5 is out of range"
150 → is int? YES → 0 <= 150 <= 100? NO  → "150 is out of range"
37  → is int? YES → 0 <= 37 <= 100?  YES → "37 is valid"
```

---

## Nested Loops — the Clock Mental Model

A loop inside a loop. The inner loop **completes fully** before the outer loop moves one step.

```python
teams = ["red", "blue"]
players = ["Alice", "Bob", "Charlie"]

for team in teams:
    for player in players:
        print(f"{player} is on team {team}")
```

```
Outer round 1: team = "red"
    Inner round 1: player = "Alice"   → "Alice is on team red"
    Inner round 2: player = "Bob"     → "Bob is on team red"
    Inner round 3: player = "Charlie" → "Charlie is on team red"

Outer round 2: team = "blue"
    Inner round 1: player = "Alice"   → "Alice is on team blue"
    Inner round 2: player = "Bob"     → "Bob is on team blue"
    Inner round 3: player = "Charlie" → "Charlie is on team blue"
```

Think of it as a clock. The inner loop is the seconds hand — full spin before the outer loop (minutes hand) moves one tick.

---

## break and continue

```python
# break — exit the loop immediately
for n in [1, 2, 3, 4, 5]:
    if n == 3:
        break
    print(n)
# prints: 1, 2
# loop dies the moment n hits 3

# continue — skip this round, keep going
for n in [1, 2, 3, 4, 5]:
    if n == 3:
        continue
    print(n)
# prints: 1, 2, 4, 5
# round 3 is skipped but loop continues
```

---

## while Loop — Traced Step by Step

A `while` loop asks its question **before every single round**. If the answer is NO, it stops.

```python
count = 0

while count < 4:
    print(count)
    count += 1
```

```
Before round 1: is 0 < 4?  YES → print 0, count → 1
Before round 2: is 1 < 4?  YES → print 1, count → 2
Before round 3: is 2 < 4?  YES → print 2, count → 3
Before round 4: is 3 < 4?  YES → print 3, count → 4
Before round 5: is 4 < 4?  NO  → stop
```

Always make sure something inside the loop changes the condition — otherwise it runs forever.

---

## The Mental Toolkit — What to Do When You Get Lost

```
1. Find the loop or condition that is confusing you
2. Ignore everything outside it for now
3. Ask: what collection is being looped? / what question is being asked?
4. Pick ONE specific value and trace through manually on paper
5. Write down what each variable holds at each step
6. Read the result for that one value
7. Repeat with a different value
8. Zoom back out and read the whole thing
```

The moment you trace one example by hand, the fog clears.
**Always trace manually when confused. It works every time.**

---

# PART 6 — Functions

## Basic Function

```python
def greet(name):
    return f"Hello, {name}"

result = greet("Fahid")
print(result)   # Hello, Fahid
```

## Default Parameters

```python
def connect(host, port=5432, timeout=30):
    print(f"Connecting to {host}:{port} (timeout={timeout}s)")

connect("localhost")              # uses defaults for port and timeout
connect("localhost", 3306)        # overrides port
connect("localhost", timeout=10)  # overrides only timeout by name
```

## *args — Variable Positional Arguments

When you don't know how many arguments will be passed, use `*args`. It collects all extra positional arguments into a **tuple**.

```python
def add(*args):
    return sum(args)

add(1, 2)          # 3
add(1, 2, 3, 4, 5) # 15


def log(level, *messages):
    for msg in messages:
        print(f"[{level}] {msg}")

log("INFO", "Starting up", "Loading config", "Ready")
# [INFO] Starting up
# [INFO] Loading config
# [INFO] Ready
```

## **kwargs — Variable Keyword Arguments

Collects all extra keyword arguments into a **dict**.

```python
def create_user(**kwargs):
    print(kwargs)

create_user(name="Fahid", age=26, city="Tampere")
# {"name": "Fahid", "age": 26, "city": "Tampere"}


def configure(host, port, **options):
    print(f"Connecting to {host}:{port}")
    for key, val in options.items():
        print(f"  {key} = {val}")

configure("localhost", 5432, timeout=30, retries=3, ssl=True)
```

## Combining *args and **kwargs

```python
def pipeline(data, *transforms, **options):
    verbose = options.get("verbose", False)
    for fn in transforms:
        data = fn(data)
        if verbose:
            print(f"After {fn.__name__}: {data}")
    return data

result = pipeline(
    {"name": " fahid ", "age": "26"},
    normalize_values,
    remove_empty,
    verbose=True
)
```

## Unpacking Arguments

The `*` and `**` operators also work in the other direction — unpacking a list or dict into function arguments.

```python
def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
add(*nums)      # same as add(1, 2, 3)

settings = {"host": "localhost", "port": 5432}
connect(**settings)   # same as connect(host="localhost", port=5432)
```

## Lambda Functions

A lambda is a small anonymous function — one expression, no `return` keyword needed.

```python
double = lambda x: x * 2
double(5)    # 10

# most useful as an argument to another function
names = ["Charlie", "Alice", "Bob"]
sorted(names, key=lambda x: len(x))    # sort by length
# ["Bob", "Alice", "Charlie"]

data = [{"name": "Bob", "age": 30}, {"name": "Alice", "age": 25}]
sorted(data, key=lambda x: x["age"])   # sort dicts by age
```

## Closures

A closure is a function that remembers the environment it was created in, even after that environment is gone.

```python
def make_multiplier(factor):
    def multiply(x):          # inner function
        return x * factor     # uses 'factor' from outer scope
    return multiply           # returns the inner function

double = make_multiplier(2)
triple = make_multiplier(3)

double(5)   # 10
triple(5)   # 15
```

The inner `multiply` function carries `factor` with it. This is a closure.

## Decorators

A decorator is a function that wraps another function to add behavior before or after it, without modifying the original function.

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Done")
        return result
    return wrapper


@logger                          # this is syntax sugar for:
def add(a, b):                   # add = logger(add)
    return a + b

add(2, 3)
# Calling add
# Done
# 5
```

A decorator with arguments:

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def greet(name):
    print(f"Hello {name}")

greet("Fahid")
# Hello Fahid
# Hello Fahid
# Hello Fahid
```

Real-world decorators you will encounter:

```python
@staticmethod       # method belongs to class, not instance
@classmethod        # method receives class, not instance
@property           # method acts like an attribute
@functools.lru_cache(maxsize=128)   # cache function results
```

## Generators

A generator is a function that produces values one at a time using `yield`. It does not compute everything upfront — it is **lazy**. This saves memory when dealing with large data.

```python
def count_up(start, end):
    current = start
    while current <= end:
        yield current         # pause here, return value, resume next call
        current += 1

counter = count_up(1, 5)
next(counter)   # 1
next(counter)   # 2

# most commonly used in a for loop
for n in count_up(1, 1000000):   # never stores all million numbers at once
    process(n)


# generator expression (like list comprehension but lazy)
squares = (x ** 2 for x in range(1000000))   # no memory cost
```

## Higher-Order Functions

A higher-order function takes a function as an argument, or returns a function. You have already seen these.

```python
# map — apply function to every item
list(map(str, [1, 2, 3]))         # ["1", "2", "3"]

# filter — keep only items where function returns True
list(filter(None, [0, 1, "", "hi", None, 42]))   # [1, "hi", 42]

# sorted with key
sorted(["banana", "apple", "kiwi"], key=len)     # ["kiwi", "apple", "banana"]

# functools.reduce — accumulate
from functools import reduce
reduce(lambda acc, x: acc + x, [1, 2, 3, 4])    # 10
```

## Type Hints in Functions

Type hints do not enforce types at runtime — they are documentation for humans and tools like linters.

```python
def clean(data: dict) -> dict:
    return {k: v for k, v in data.items() if v is not None}

def validate(config: dict, required: list[str]) -> list[str]:
    return [field for field in required if field not in config]

def get_port(config: dict, default: int = 5432) -> int:
    return config.get("port", default)
```

---

# PART 7 — Data Structures Deep Dive

## List

Ordered, mutable, allows duplicates.

```python
items = [3, 1, 4, 1, 5, 9]

# access
items[0]      # 3      — first
items[-1]     # 9      — last
items[1:4]    # [1, 4, 1]  — slice
items[:3]     # [3, 1, 4]
items[::2]    # [3, 4, 5]  — every second

# modify
items.append(2)           # add to end
items.insert(0, 99)       # insert at index
items.extend([7, 8])      # add multiple
items.remove(1)           # remove first occurrence of value
items.pop()               # remove and return last
items.pop(0)              # remove and return at index
items.sort()              # sort in place
items.reverse()           # reverse in place
items.index(4)            # find index of value
items.count(1)            # count occurrences
len(items)                # length

# copy — important
copy = items[:]           # shallow copy
copy = items.copy()       # same
import copy
deep = copy.deepcopy(items)   # deep copy (for nested structures)
```

## Tuple

Ordered, immutable. Use when data should not change.

```python
point = (52.5, 13.4)
rgb = (255, 128, 0)

point[0]          # 52.5
x, y = point      # unpacking

# namedtuple — tuple with named fields
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
p.x    # 10
p.y    # 20
```

## Set

Unordered, no duplicates. Fast membership testing.

```python
tags = {"python", "data", "python"}   # duplicate dropped
tags.add("yaml")
tags.discard("data")        # remove if exists, no error if not
tags.remove("data")         # remove, raises error if not found

"python" in tags            # True  — O(1) lookup

# set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a | b     # union:        {1, 2, 3, 4, 5, 6}
a & b     # intersection: {3, 4}
a - b     # difference:   {1, 2}
a ^ b     # symmetric diff: {1, 2, 5, 6}
```

## Dictionary

Key-value pairs. Keys must be unique. Ordered since Python 3.7.

```python
user = {"name": "Fahid", "age": 26, "city": "Tampere"}

# access
user["name"]                  # "Fahid" — raises KeyError if missing
user.get("email")             # None    — safe, no error
user.get("email", "N/A")      # "N/A"   — with default

# modify
user["country"] = "Finland"   # add or update
del user["city"]              # remove key
user.pop("age")               # remove and return value
user.pop("age", None)         # safe remove — no error if missing

# iterate
user.keys()      # all keys
user.values()    # all values
user.items()     # all (key, value) pairs

# merge (Python 3.9+)
defaults = {"timeout": 30, "retries": 3}
settings = {"timeout": 10}
merged = defaults | settings    # {"timeout": 10, "retries": 3}

# check membership
"name" in user       # True
"email" in user      # False
```

## collections Module — Specialized Containers

```python
from collections import defaultdict, Counter, OrderedDict, deque

# defaultdict — dict with default value for missing keys
counts = defaultdict(int)
counts["a"] += 1     # no KeyError — starts at 0 automatically

groups = defaultdict(list)
groups["admin"].append("Fahid")    # starts with empty list

# Counter — count occurrences
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
c = Counter(words)
# Counter({"apple": 3, "banana": 2, "cherry": 1})
c.most_common(2)   # [("apple", 3), ("banana", 2)]

# deque — fast append/pop from both ends
from collections import deque
q = deque([1, 2, 3])
q.appendleft(0)    # [0, 1, 2, 3]
q.popleft()        # 0
```

---

# PART 8 — Comprehensions

Comprehensions come from mathematics — set-builder notation. They describe **what you want** instead of how to build it step by step.

```
Math:    { x | x ∈ numbers, x > 0 }
Python:  [x for x in numbers if x > 0]
```

## List Comprehension

```python
numbers = [1, 2, 3, 4, 5]

doubled = [x * 2 for x in numbers]
# [2, 4, 6, 8, 10]

evens = [x for x in numbers if x % 2 == 0]
# [2, 4]

transformed = [x * 2 for x in numbers if x > 2]
# [6, 8, 10]
```

## Dictionary Comprehension

```python
data = {"name": "Fahid", "age": None, "city": "Tampere", "email": ""}

# filter out None
cleaned = {k: v for k, v in data.items() if v is not None}

# transform keys
upper_keys = {k.upper(): v for k, v in data.items()}

# swap keys and values
inverted = {v: k for k, v in data.items()}
```

## Set Comprehension

```python
names = ["alice", "bob", "alice", "charlie"]
unique_upper = {name.upper() for name in names}
# {"ALICE", "BOB", "CHARLIE"}
```

## Generator Expression

Like a list comprehension but lazy — computes one value at a time. No memory cost for large data.

```python
total = sum(x * 2 for x in range(1000000))   # no list built in memory

# when to use list vs generator
results = [process(x) for x in data]    # use list if you need to reuse the results
total = sum(process(x) for x in data)   # use generator if you only need one pass
```

## When to Use Comprehension vs Loop

```python
# use comprehension — simple filter or transform
valid = {k: v for k, v in data.items() if v and isinstance(v, str)}

# use a loop — complex logic, multiple steps, side effects
result = {}
for k, v in data.items():
    if v is None:
        continue
    if isinstance(v, str):
        v = v.strip()
    if isinstance(v, dict):
        v = clean_nested(v)
    result[k] = v
```

---

# PART 9 — Object-Oriented Programming

## The Core Idea

OOP lets you bundle related data and behavior into a single unit called a **class**. A class is a blueprint. An **object** (instance) is something built from that blueprint.

## Basic Class

```python
class Sensor:
    def __init__(self, sensor_id, location):   # constructor
        self.sensor_id = sensor_id             # instance attributes
        self.location = location
        self.readings = []

    def add_reading(self, value):              # method
        self.readings.append(value)

    def average(self):
        if not self.readings:
            return 0
        return sum(self.readings) / len(self.readings)

    def __str__(self):                         # string representation
        return f"Sensor({self.sensor_id} @ {self.location})"


s = Sensor("A1", "Warehouse")
s.add_reading(22.4)
s.add_reading(23.1)
print(s.average())   # 22.75
print(s)             # Sensor(A1 @ Warehouse)
```

## Class Variables vs Instance Variables

```python
class Employee:
    company = "TechCorp"      # class variable — shared by ALL instances

    def __init__(self, name, salary):
        self.name = name       # instance variable — unique per object
        self.salary = salary

e1 = Employee("Fahid", 60000)
e2 = Employee("Sara", 75000)
print(e1.company)   # TechCorp
print(e2.company)   # TechCorp
print(e1.name)      # Fahid
print(e2.name)      # Sara
```

## Inheritance

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)    # call parent constructor
        self.breed = breed

    def bark(self):
        print(f"{self.name} barks!")

    def eat(self):                     # override parent method
        print(f"{self.name} wolfs it down")


dog = Dog("Rex", 3, "Labrador")
dog.eat()    # Rex wolfs it down  (overridden)
dog.bark()   # Rex barks!
```

## Encapsulation

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance      # private — name-mangled

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

    @property                         # access like attribute, not method
    def balance(self):
        return self.__balance


account = BankAccount("Fahid", 1000)
account.deposit(500)
print(account.balance)     # 1500  (via @property)
```

## Dunder (Magic) Methods

These let your class integrate with Python's built-in operations.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):           # print(v)
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):          # in console, for debugging
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, other):    # v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):     # v1 == v2
        return self.x == other.x and self.y == other.y

    def __len__(self):           # len(v)
        return 2

    def __getitem__(self, index): # v[0]
        return (self.x, self.y)[index]
```

## Abstract Classes

Force subclasses to implement specific methods.

```python
from abc import ABC, abstractmethod

class Exporter(ABC):
    @abstractmethod
    def export(self, data: dict) -> str:
        pass

    def save(self, data, path):          # concrete method — shared by all
        content = self.export(data)
        with open(path, "w") as f:
            f.write(content)


class JsonExporter(Exporter):
    def export(self, data):              # must implement this
        import json
        return json.dumps(data, indent=4)


class YamlExporter(Exporter):
    def export(self, data):              # must implement this
        import yaml
        return yaml.dump(data)

# Exporter()   ← TypeError — cannot instantiate abstract class
JsonExporter().export({"a": 1})    # works fine
```

## dataclasses — Cleaner Class Syntax

For classes that are mostly data containers, `dataclass` removes boilerplate.

```python
from dataclasses import dataclass, field

@dataclass
class Config:
    host: str
    port: int = 5432
    enabled: bool = True
    tags: list = field(default_factory=list)

c = Config(host="localhost")
print(c)     # Config(host='localhost', port=5432, enabled=True, tags=[])
print(c.port)  # 5432

# dataclass automatically gives you __init__, __str__, __repr__, __eq__
```

---

# PART 10 — Modules and Imports

## Import Styles

```python
import json                       # import whole module
import json as j                  # alias
from json import loads, dumps     # import specific names
from json import *                # import everything (avoid this)

# relative imports (inside a package)
from . import utils               # from same directory
from ..config import settings     # from parent directory
```

## Creating Your Own Module

Any `.py` file is a module. Any folder with an `__init__.py` is a package.

```
myproject/
    __init__.py
    loader.py
    validator.py
    transformer.py
    main.py
```

```python
# loader.py
def load_config(path): ...

# main.py
from loader import load_config
config = load_config("config.yaml")
```

## `__name__ == "__main__"`

```python
# this block only runs when you execute the file directly
# it does NOT run when someone imports your file as a module

if __name__ == "__main__":
    main()
```

---

# PART 11 — File Handling

## Reading and Writing Text

```python
# read entire file
with open("data.txt", "r") as f:
    content = f.read()

# read line by line (memory efficient for large files)
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())

# read all lines into a list
with open("data.txt", "r") as f:
    lines = f.readlines()

# write
with open("output.txt", "w") as f:     # "w" overwrites
    f.write("hello\n")

with open("output.txt", "a") as f:     # "a" appends
    f.write("world\n")
```

## JSON Files

```python
import json

with open("data.json", "r") as f:
    data = json.load(f)                       # file → dict

with open("output.json", "w") as f:
    json.dump(data, f, indent=4, sort_keys=True)   # dict → file

# string operations
text = json.dumps(data, indent=4)             # dict → string
data = json.loads('{"name": "Fahid"}')        # string → dict
```

## YAML Files

```python
import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)      # always use safe_load, not load

with open("output.yaml", "w") as f:
    yaml.dump(config, f, default_flow_style=False)
```

## Paths with pathlib

```python
from pathlib import Path

p = Path("data/config.yaml")

p.exists()          # True/False
p.is_file()         # True/False
p.is_dir()          # True/False
p.suffix            # ".yaml"
p.stem              # "config"
p.parent            # Path("data")
p.name              # "config.yaml"

p.read_text()       # read content
p.write_text("hi")  # write content

# build paths safely (handles / on Mac, \ on Windows)
base = Path("projects")
full = base / "10_projects" / "prj3.py"
```

---

# PART 12 — Error Handling

## try / except

```python
try:
    data = json.load(open("missing.json"))
except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
except Exception as e:            # catch-all — use sparingly
    print(f"Unexpected error: {e}")
else:
    print("Loaded successfully")  # runs only if no exception
finally:
    print("Always runs")          # cleanup code goes here
```

## Raising Exceptions

```python
def validate_age(age):
    if not isinstance(age, int):
        raise TypeError(f"age must be int, got {type(age).__name__}")
    if age < 0 or age > 120:
        raise ValueError(f"age must be between 0 and 120, got {age}")
    return age
```

## Custom Exceptions

```python
class ConfigError(Exception):
    pass

class MissingFieldError(ConfigError):
    def __init__(self, field):
        super().__init__(f"Required field missing: '{field}'")
        self.field = field


raise MissingFieldError("email")
# MissingFieldError: Required field missing: 'email'
```

## Fail Fast Pattern

Catch problems at the entry point, before they travel deep.

```python
def run_pipeline(config):
    if "database" not in config:
        raise MissingFieldError("database")
    if not isinstance(config["database"].get("port"), int):
        raise TypeError("database.port must be int")
    # only reaches here if config is valid
    process(config)
```

---

# PART 13 — Built-in Functions

```python
# type conversion
int()  float()  str()  bool()  list()  dict()  set()  tuple()  bytes()

# math
abs(-5)               # 5
round(3.14159, 2)     # 3.14
min(3, 1, 4)          # 1
max(3, 1, 4)          # 4
sum([1, 2, 3])        # 6
pow(2, 10)            # 1024
divmod(10, 3)         # (3, 1)

# sequences
len([1, 2, 3])        # 3
range(5)              # 0-4
range(2, 8, 2)        # 2, 4, 6
sorted([3,1,2])       # [1, 2, 3]
reversed([1,2,3])     # iterator: 3, 2, 1
enumerate(["a","b"])  # (0,"a"), (1,"b")
zip([1,2],[3,4])      # (1,3), (2,4)

# functional
map(str, [1,2,3])           # ["1","2","3"]
filter(None, [0,1,"",2])    # [1, 2]
any([False, True, False])   # True
all([True, True, True])     # True

# inspection
type(x)
isinstance(x, int)
dir(x)               # all methods/attributes
hasattr(obj, "name") # True/False
getattr(obj, "name", default)
callable(x)          # True if x can be called as a function

# I/O
print("hello", end="", sep=",")
input("Enter: ")
open("file.txt", "r")
```

---

# PART 14 — Standard Library

These are built in — no install needed.

```python
import json          # JSON parsing and serialization
import os            # OS interface, file system
import sys           # interpreter, sys.exit(), sys.argv
import re            # regular expressions
import datetime      # dates and times
import pathlib       # modern file paths
import collections   # defaultdict, Counter, deque, namedtuple
import itertools     # chain, groupby, product, combinations
import functools     # reduce, lru_cache, partial
import typing        # type hints: List, Dict, Optional, Union
import base64        # base64 encode/decode
import struct        # binary data packing
import io            # in-memory file objects
import copy          # copy.deepcopy()
import hashlib       # md5, sha256 hashing
import uuid          # unique IDs
import time          # time.time(), time.sleep()
import logging       # proper logging instead of print
import argparse      # command-line argument parsing
import csv           # CSV file reading and writing
import math          # math.floor(), math.ceil(), math.sqrt()
import random        # random.choice(), random.shuffle()
import string        # string.ascii_letters, string.digits
import textwrap      # wrap and format text blocks
```

---

# PART 15 — Advanced Function Writing

## Partial Functions

Fix some arguments of a function and create a new one.

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube   = partial(power, exponent=3)

square(4)   # 16
cube(3)     # 27
```

## Function Caching (Memoization)

Cache the result of expensive function calls so they are not recomputed.

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(50)   # fast — results are cached after first computation
```

## Function Composition

```python
def compose(*functions):
    def composed(data):
        for fn in functions:
            data = fn(data)
        return data
    return composed


clean = compose(normalize_values, remove_empty, rename_keys)
result = clean(raw_data)   # all three functions applied in order
```

## Recursive Functions

A function that calls itself. Must have a base case or it runs forever.

```python
def remove_empty(data):
    cleaned = {}
    for key, value in data.items():
        if isinstance(value, dict):
            value = remove_empty(value)    # recurse into nested dict
        if value is not None and value != "" and value != {}:
            cleaned[key] = value
    return cleaned


def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))   # recurse
        else:
            result.append(item)
    return result

flatten([1, [2, [3, 4]], 5])   # [1, 2, 3, 4, 5]
```

## Context Managers

A context manager controls setup and teardown around a block of code. `with` is the keyword.

```python
# using a context manager
with open("file.txt") as f:
    data = f.read()
# file is automatically closed here, even if an exception occurred

# writing your own with a class
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, *args):
        import time
        self.elapsed = time.time() - self.start
        print(f"Took {self.elapsed:.3f}s")


with Timer() as t:
    result = expensive_operation()

# writing your own with a generator (simpler)
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    yield
    print(f"Took {time.time() - start:.3f}s")

with timer():
    result = expensive_operation()
```

## Iterators

An iterator is any object with `__iter__` and `__next__`. Python's `for` loop uses these internally.

```python
class CountUp:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


for n in CountUp(1, 5):
    print(n)   # 1, 2, 3, 4, 5
```

---

# PART 16 — Type Hints

Type hints are annotations that describe what types a function expects and returns. They do not enforce anything at runtime — they are for humans, linters, and IDEs.

```python
# basic hints
def greet(name: str) -> str:
    return f"Hello, {name}"

def add(a: int, b: int) -> int:
    return a + b

# optional — value can be None
from typing import Optional

def find_user(user_id: int) -> Optional[dict]:
    ...

# union — can be one of several types
from typing import Union

def parse(value: Union[str, int]) -> int:
    return int(value)

# Python 3.10+ shorthand for Union
def parse(value: str | int) -> int:
    return int(value)

# collections
from typing import List, Dict, Tuple

def process(items: List[str]) -> Dict[str, int]:
    ...

# any type
from typing import Any

def log(data: Any) -> None:
    print(data)
```

---

# PART 17 — Functional Programming

Functional programming is a style built around three core operations:

```
map    → transform every item
filter → keep only matching items
reduce → collapse to a single value
```

## Pure Functions

A pure function always returns the same output for the same input and has no side effects.

```python
# impure — depends on external state
total = 0
def add_to_total(n):
    global total
    total += n

# pure — predictable and testable
def add(a, b):
    return a + b
```

## Immutability

Prefer not modifying input data. Return new data instead.

```python
# mutates input — risky
def add_field(data):
    data["processed"] = True
    return data

# creates new dict — safe
def add_field(data):
    return {**data, "processed": True}
```

## Chaining Transformations

```python
data = load("data.json")
data = normalize_values(data)
data = remove_empty(data)
data = rename_keys(data, RENAME_MAP)
save("output.json", data)

# or as a pipeline
pipeline = [normalize_values, remove_empty, lambda d: rename_keys(d, RENAME_MAP)]
for transform in pipeline:
    data = transform(data)
```

---

# PART 18 — Advanced Coding Style and Theory

## DRY — Don't Repeat Yourself

Every piece of knowledge should exist in exactly one place.

```python
# bad — age validation in 3 places
# good — once
def validate_age(age):
    if age < 0 or age > 120:
        raise ValueError(f"Invalid age: {age}")
```

## KISS — Keep It Simple

The simplest solution that works is almost always the best.

```python
# bad — clever but unreadable
is_even = lambda n: not n & 1

# good
def is_even(n):
    return n % 2 == 0
```

## SOLID

| Letter | Name | Rule |
|--------|------|------|
| S | Single Responsibility | One class, one job |
| O | Open/Closed | Extend without modifying existing code |
| L | Liskov Substitution | Subclasses must be usable as their parent |
| I | Interface Segregation | Small focused interfaces over large ones |
| D | Dependency Inversion | Depend on abstractions, not concrete classes |

## Separation of Concerns

```python
# bad — I/O, logic, and output mixed
def run():
    data = json.load(open("data.json"))
    cleaned = {k: v for k, v in data.items() if v}
    print(json.dumps(cleaned, indent=4))

# good — each concern isolated
def load(path): ...        # I/O
def clean(data): ...       # logic
def display(data): ...     # output
```

## Fail Fast

Catch errors at the boundary, not deep in the code.

```python
def run(config):
    if "database" not in config:
        raise ConfigError("Missing 'database' section")
    # only reaches processing if config is valid
```

## Composition Over Inheritance

```python
# inheritance — fragile deep chains
class TrainedHuntingDog(HuntingDog): ...

# composition — flexible
class Dog:
    def __init__(self):
        self.trainer = Trainer()
        self.hunter = Hunter()
```

## Law of Demeter

Only talk to direct neighbors. Avoid long method chains.

```python
# bad
user.get_account().get_wallet().get_balance()

# good
user.get_balance()
```

---

# PART 19 — Problem Decomposition

## The 5-Step Mental Process

Before writing code:

```
1. What is the INPUT?
2. What is the OUTPUT?
3. What are the STEPS between them?
4. What can GO WRONG?
5. What are the PIECES (functions)?
```

## Top-Down Design

Start with `main`, then fill in each function.

```python
def main():
    data = load("data.json")       # step 1
    data = normalize(data)         # step 2
    data = validate(data)          # step 3
    save("output.json", data)      # step 4

# now implement each function one at a time
```

## Rules for Functions

- One function, one job
- Name the function before writing the body
- Input flows in, output flows out
- No more than ~20 lines — if longer, split it

## Testing as You Build

```python
# test each function in isolation before wiring up
data = {"name": "fahid", "age": "26", "active": "true"}
result = normalize_values(data)
assert result["age"] == 26
assert result["active"] == True
print("normalize_values: OK")
```

---

# PART 20 — Testing

## Writing Tests with pytest

```python
# test_cleaner.py
import pytest
from prjct2 import remove_empty, normalize_values

def test_remove_empty_removes_none():
    data = {"name": "Fahid", "email": None}
    result = remove_empty(data)
    assert "email" not in result
    assert result["name"] == "Fahid"

def test_remove_empty_removes_empty_string():
    data = {"name": "Fahid", "city": ""}
    result = remove_empty(data)
    assert "city" not in result

def test_normalize_converts_string_int():
    data = {"age": "26"}
    result = normalize_values(data)
    assert result["age"] == 26
    assert isinstance(result["age"], int)

def test_normalize_converts_true_string():
    data = {"active": "true"}
    result = normalize_values(data)
    assert result["active"] is True
```

Run with: `pytest test_cleaner.py -v`

## Testing Exceptions

```python
def test_validate_raises_on_missing_field():
    with pytest.raises(ValueError):
        validate_config({}, required=["name"])
```

---

# PART 21 — Logging

Never use `print` in production code. Use `logging`.

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger(__name__)

logger.debug("Loading config file")     # detailed debug info
logger.info("Config loaded")            # normal operation
logger.warning("Missing optional field 'theme', using default")
logger.error("Failed to connect to database")
logger.critical("Cannot start — config is invalid")
```

Levels in order: `DEBUG < INFO < WARNING < ERROR < CRITICAL`

---

# PART 22 — Data Formats Reference

These formats all map to Python types when loaded.

| Format | Python type after loading | Library |
|--------|--------------------------|---------|
| JSON | `dict`, `list` | `json` (built-in) |
| YAML | `dict`, `list` | `pyyaml` |
| CBOR | `dict`, `bytes` | `cbor2` |
| Base64 | `bytes` | `base64` (built-in) |
| CSV | `list` of `dict` | `csv` (built-in) |
| Binary | `bytes` | built-in |

```python
# Base64
import base64
encoded = base64.b64encode(b"hello world")    # b"aGVsbG8gd29ybGQ="
decoded = base64.b64decode(encoded)           # b"hello world"

# CBOR
import cbor2
data = {"temp": 22.4, "id": "A1"}
encoded = cbor2.dumps(data)                   # bytes
decoded = cbor2.loads(encoded)                # dict back

# CSV
import csv
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)    # each row is a dict
```

---

# PART 23 — Modular Coding

Modular coding means splitting your program into separate files where **each file has one responsibility and one only**. No file does two jobs.

---

## The Problem With One Big File

Imagine writing everything in a single `main.py` — 500 lines of constants, data shapes, parsing logic, state management, and orchestration all mixed together.

- To change one thing, you scroll through everything else
- You cannot test one piece without loading the whole program
- Two people editing the same file at the same time creates conflicts
- A bug in the parsing logic is buried next to the display logic

Modular code solves all of these.

---

## The Six Layers Every Project Has

Every non-trivial Python project naturally splits into these layers. Not every project needs all six, but recognising them tells you where each piece of code belongs.

```
constants.py   → fixed values used across the project
enums.py       → valid named states (no magic strings)
models.py      → what the data looks like (shapes only)
helpers.py     → pure functions that transform data
state.py       → classes that remember things between calls
main.py        → orchestrator — calls everything in order
```

---

## Layer 1 — constants.py

Stores values that never change and are used in more than one place.

```python
# constants.py
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30
REQUIRED_FIELDS = ["name", "email", "age"]
API_BASE_URL = "https://api.example.com/v1"
```

**Why it matters:** Without this, `30` appears in 6 different files. When the timeout changes to `60`, you hunt through all 6. With constants, you change one line.

**Rule:** If a value is used in more than one place, it does not belong inside a function — it belongs in constants.

---

## Layer 2 — enums.py

Stores a fixed set of valid named states. Replaces raw strings and magic numbers.

```python
# enums.py
from enum import Enum

class Status(str, Enum):
    ACTIVE   = "active"
    INACTIVE = "inactive"
    PENDING  = "pending"

class Environment(str, Enum):
    DEV     = "dev"
    STAGING = "staging"
    PROD    = "prod"
```

**Without enums — fragile:**
```python
if status == "actve":    # typo — silently never matches
    ...
```

**With enums — safe:**
```python
if status == Status.ACTIVE:   # typo here is a NameError caught immediately
    ...
```

Your editor also autocompletes `Status.` and shows every valid value.

**Rule:** Any field with a fixed set of valid values belongs in an enum, not a raw string.

---

## Layer 3 — models.py

Defines the shape of your data. No logic, no calculations, no file I/O. Just structure.

```python
# models.py
from dataclasses import dataclass
from typing import Optional
from datetime import datetime
from .enums import Status

@dataclass
class Address:
    street: str
    city:   str
    country: str

@dataclass
class User:
    id:         int
    name:       str
    email:      str
    status:     Status
    address:    Optional[Address]
    created_at: datetime
```

**Why it matters:** When any part of your code receives a `User` object, everyone knows exactly what fields it has and what types they are. No guessing. No `dict.get("nmae")` typos. Your editor knows the shape too.

**Rule:** Data structures belong here. Never put transformation logic in a model.

---

## Layer 4 — helpers.py (or decoder.py, utils.py)

Pure functions that transform data. Takes something in, returns something out. No state. No file I/O.

```python
# helpers.py
from typing import Optional
from .models import Address, User
from .enums import Status

def normalize_name(name: str) -> str:
    return name.strip().title()

def is_valid_email(email: str) -> bool:
    return "@" in email and "." in email.split("@")[-1]

def format_created_date(user: User) -> str:
    return user.created_at.strftime("%d %B %Y")

def validate_required_fields(data: dict, required: list[str]) -> list[str]:
    return [field for field in required if field not in data]
```

**Why pure functions:** Pure means same input → same output, always. No hidden state, no side effects. This makes them trivial to test:

```python
assert normalize_name("  fahid khan ") == "Fahid Khan"
assert is_valid_email("bad-email") == False
```

No database, no file, no network needed. Just call the function with a value.

**Rule:** One function, one job. If you cannot describe what a function does in one sentence, split it.

---

## Layer 5 — state.py (or tracker.py, cache.py)

Classes that need to **remember things between calls**. This cannot be a pure function because it holds memory.

```python
# state.py
from typing import Optional

class RateLimiter:
    def __init__(self, max_calls: int, window_seconds: int):
        self._max_calls = max_calls
        self._window    = window_seconds
        self._calls: dict[str, list] = {}   # remembers per user

    def is_allowed(self, user_id: str) -> bool:
        import time
        now = time.time()
        history = self._calls.get(user_id, [])
        recent = [t for t in history if now - t < self._window]
        self._calls[user_id] = recent
        if len(recent) >= self._max_calls:
            return False
        self._calls[user_id].append(now)
        return True
```

**Why it lives separately:** Keeping stateful objects isolated means you can test them in isolation, swap them out easily, and reason about them without reading the rest of the codebase.

**Rule:** If something needs memory between calls, it becomes its own class in its own file.

---

## Layer 6 — main.py (or app.py, pipeline.py)

The orchestrator. Calls all the other layers in the right order. Does not implement logic itself — it delegates.

```python
# main.py
from .constants import REQUIRED_FIELDS
from .helpers   import validate_required_fields, normalize_name
from .models    import User
from .state     import RateLimiter

limiter = RateLimiter(max_calls=100, window_seconds=60)

def handle_request(user_id: str, data: dict) -> dict:
    if not limiter.is_allowed(user_id):
        return {"error": "Rate limit exceeded"}

    errors = validate_required_fields(data, REQUIRED_FIELDS)
    if errors:
        return {"error": f"Missing fields: {errors}"}

    data["name"] = normalize_name(data["name"])
    return {"status": "ok", "data": data}
```

The orchestrator is thin. It glues pieces together. If you find yourself writing complex logic here, it means a piece belongs in helpers.py instead.

---

## The Dependency Rule

The most important rule in modular design: **dependencies only flow in one direction.**

```
main.py / app.py       ← imports from everything below
      │
  helpers.py           ← imports from models, enums, constants
      │
  state.py             ← imports from models, constants
      │
  models.py            ← imports from enums
      │
  enums.py             ← imports nothing local
      │
  constants.py         ← imports nothing local
```

`constants.py` never imports from `helpers.py`. `models.py` never imports from `main.py`. Lower layers never know about higher layers.

**Why:** If two files import each other, you get a circular import — Python cannot load either one. More importantly, you can no longer test a lower layer without loading the whole program.

---

## Practical File Structure

For a small project:

```
myproject/
├── __init__.py         expose the public API
├── constants.py        fixed values
├── enums.py            named states
├── models.py           data shapes
├── helpers.py          pure transformation functions
├── state.py            stateful classes (if needed)
├── main.py             orchestrator
└── tests/
    ├── test_helpers.py
    └── test_models.py
```

For a larger project, group by feature:

```
myproject/
├── config/
│   ├── constants.py
│   └── enums.py
├── data/
│   ├── models.py
│   └── helpers.py
├── pipeline/
│   ├── loader.py
│   ├── transformer.py
│   └── exporter.py
└── main.py
```

---

## The `__init__.py` — Your Public API

Every Python package folder needs an `__init__.py`. It controls what the outside world can import from your package.

```python
# __init__.py
from .main   import Pipeline
from .models import User, Address
from .enums  import Status

__all__ = ["Pipeline", "User", "Address", "Status"]
```

Now a user of your package writes:

```python
from myproject import Pipeline, User
```

They do not need to know which internal file things live in. The `__init__.py` is the front door.

---

## Why Not Just One Big File — Concrete Comparison

**One big file:**
```
To change timeout value    → search through 300 lines
To test email validation   → need to load the whole app
To add a new status type   → search for every if/elif chain
Two devs working together  → constant merge conflicts
```

**Modular:**
```
To change timeout value    → open constants.py, change one line
To test email validation   → import is_valid_email(), pass a string
To add a new status type   → open enums.py, add one line
Two devs working together  → one on helpers.py, one on models.py
```

**Modular coding is not organisation for its own sake. It makes change cheap and safe.**

---

## The Mindmap

```
YOUR PROJECT
│
├── constants.py    "what are the fixed values?"
│                   → no imports from your own code
│
├── enums.py        "what are the valid named states?"
│                   → imports nothing local
│
├── models.py       "what shape does the data have?"
│                   → imports enums
│                   → no logic, no I/O
│
├── helpers.py      "how do we transform data?"
│                   → pure functions only
│                   → imports models, enums, constants
│                   → testable with plain values
│
├── state.py        "what needs to remember things?"
│                   → stateful classes
│                   → imports models, constants
│
└── main.py         "in what order does it all run?"
                    → imports from all layers
                    → thin — delegates, does not implement
```

---

# PART 24 — Quick Reference Card

## Python Data Types

```
int        float      str        bool       None
list       tuple      set        dict       bytes
```

## Most Used Built-ins

```
print   len    range  type   isinstance  sorted  enumerate
zip     map    filter any    all         sum     min  max
open    input  abs    round  dict   list  set
```

## Control Flow

```python
if x: ... elif y: ... else: ...
for x in collection: ...
while condition: ...
break  continue  pass
```

## Function Signatures

```python
def fn(a, b=default, *args, **kwargs): ...
fn(*list_to_unpack, **dict_to_unpack)
lambda x: expression
```

## Comprehensions

```python
[x for x in items if condition]           # list
{k: v for k, v in d.items() if condition} # dict
{x for x in items}                        # set
(x for x in items)                        # generator
```

## File Handling

```python
with open("file", "r") as f: f.read()
with open("file", "w") as f: f.write()
json.load(f)    json.dump(data, f, indent=4)
yaml.safe_load(f)    yaml.dump(data, f)
```

## Error Handling

```python
try: ...
except SomeError as e: ...
else: ...          # runs if no error
finally: ...       # always runs
raise ValueError("message")
```

## Class Structure

```python
class Name(Parent):
    class_var = value

    def __init__(self, x):
        super().__init__()
        self.x = x

    def method(self): ...
    def __str__(self): ...
    def __repr__(self): ...
```

---

# The Mindmap — How It All Connects

```
PYTHON
│
├── DATA
│   ├── Types: int float str bool None
│   ├── Collections: list tuple set dict
│   ├── Bytes: bytes bytearray
│   └── Formats: JSON YAML CBOR Base64 CSV
│
├── LOGIC
│   ├── Control flow: if for while break continue
│   ├── Comprehensions: list dict set generator
│   └── Error handling: try except raise
│
├── FUNCTIONS
│   ├── Basic: def return
│   ├── Advanced: *args **kwargs lambda closure decorator
│   ├── Generators: yield lazy evaluation
│   └── Higher-order: map filter reduce partial
│
├── CLASSES
│   ├── OOP: class __init__ self
│   ├── Inheritance: super() override
│   ├── Encapsulation: __private
│   ├── Dunder methods: __str__ __add__ __eq__
│   └── Abstractions: ABC abstractmethod dataclass
│
├── SYSTEM
│   ├── Modules: import from as
│   ├── Files: open read write json yaml pathlib
│   ├── Environment: venv pip requirements.txt
│   └── Logging: logger.info warning error
│
├── STYLE
│   ├── DRY KISS SOLID
│   ├── Separation of Concerns
│   ├── Pure Functions
│   ├── Composition over Inheritance
│   └── Fail Fast
│
└── THINKING
    ├── Input → Steps → Output
    ├── Name before you code
    ├── One function, one job
    ├── Test each piece in isolation
    └── Simple over clever
```

---

*This guide is a living document. Add to it as you learn. The goal is not to memorize — it is to build a mental model that lets you reason through any problem.*
