# Exercise 02: Conditionals and Simple Loops

## Theme: Weather Reporter

## Objective

Practice writing `if`/`elif`/`else` statements and iterating with simple `for`/`while` loops.

## 📋 Instructions

You are building small helpers for a basic weather app. Complete the functions in `weather.py` using conditionals and simple loops.

Implement these functions:

1. `temperature_feel(temp_c: int | float) -> str`
   - Return a label based on the Celsius temperature:
     - `"freezing"` for `temp_c <= 0`
     - `"cold"` for `1 <= temp_c <= 10`
     - `"mild"` for `11 <= temp_c <= 20`
     - `"warm"` for `21 <= temp_c <= 30`
     - `"hot"` for `temp_c > 30`

2. `count_rainy_days(forecast: list[str]) -> int`
   - Loop through the list and count how many entries equal `"rainy"` (case-insensitive).
   - Ignore other values like `"sunny"`, `"cloudy"`, etc.

3. `first_warm_day(temps: list[int | float]) -> int`
   - Return the index of the first day with a temperature strictly above `20`.
   - If there is no such day, return `-1`.

4. `sum_until_limit(numbers: list[int | float], limit: int | float) -> int | float`
   - Iterate through `numbers` and keep a running total.
   - Stop adding when the next number would push the total above `limit`.
   - Return the total that does not exceed `limit`.

## 💡 Example

- `temperature_feel(5)` -> `"cold"`
- `count_rainy_days(["Sunny", "Rainy", "RAINY"])` -> `2`
- `first_warm_day([10, 20, 22, 19])` -> `2`
- `sum_until_limit([4, 4, 10], 9)` -> `8`

## 📚 Required Knowledge: Functions and Return

A **function** is a reusable block of code that performs a specific task. Functions can accept inputs (called **parameters** or **arguments**) and produce outputs using the `return` statement.

The `return` statement sends a value back to whoever called the function. Once a `return` statement executes, the function stops immediately.

```python
def calculate_discount(price, percent):
    discount = price * (percent / 100)
    return discount

result = calculate_discount(100, 10)  # result = 10.0
```

In this exercise, you'll complete functions that have already been defined. Your job is to add the logic inside each function and use `return` to send back the correct result.

```python
def is_adult(age):
    if age >= 18:
        return True
    else:
        return False

status = is_adult(20)  # status = True
```

## 📚 Required Knowledge: Conditionals

Use `if`/`elif`/`else` to run different code based on conditions. Comparisons: `>`, `>=`, `<`, `<=`, `==`, `!=`. Logical operators: `and`, `or`, `not`.

### Example: using conditionals to assign grades based on score

```python
score = 73
if score >= 85:
   grade = "A"
elif score >= 70:
   grade = "B"
elif score >= 55:
   grade = "C"
else:
   grade = "D"
```

## 📚 Required Knowledge: For Loops

Use `for` loops to iterate over sequences (lists, strings, ranges).

### Example: counting prices over a particular value

```python
prices = [5.0, 12.5, 3.0, 20.0]
count_over_10 = 0
for p in prices:
   if p > 10:
      count_over_10 += 1
```

### Example of iterating with range

```python

for i in range(3):
   print(i)  # 0, 1, 2
```

## 📚 Required Knowledge: While Loops

Use `while` loops when you repeat until a condition changes. Ensure something inside the loop updates the condition to avoid infinite loops.

### Example: saving money until reaching a goal

```python
goal = 100
saved = 0
deposit = 15
while saved + deposit <= goal:
   saved += deposit
```

## 📚 Required Knowledge: Checking for case-insensitive matches

To check for case-insensitive matches in strings, you can convert both strings to the same case (either lower or upper) before comparing them.

### Example: checking for case-insensitive match

Count how many times the name "Roger" appears in a list, regardless of case.

```python
input_strings = ["Roger", "Boris", "rOger", "alice", "ROGER"]
count_roger = 0
for name in input_strings:
    if name.lower() == "roger":
        count_roger += 1
```

## 👋 Handy Knowledge: Type Hints

A type hint is a way to indicate the expected data type of a variable, function parameter, or return value in Python. The type hints in our exercises help show what data types to expect from inputs and outputs, making the code easier to understand and maintain. The type hints also help VS Code and other IDEs give you ideas about methods for things like strings and lists as you type.

```python
def greet(name: str) -> str:
      return f"Hello, {name}!"
   ```

We can see from the type hints that the `greet` function expects a string (`str`) as input and will return a string.

```python

def average(numbers: list[int | float]) -> float:
    return sum(numbers) / len(numbers)
```

Here, we get lots of information from our type hints:

- The `numbers` parameter should be a list containing integers (`int`) or floats (`float`).
- The function will return a float.


## 🧪 Running the Tests

```pwsh
pytest 02_conditionals_and_loops/test_weather.py -v
```

or use the testing extension in VS Code.

## ✅ Success Criteria

- All tests pass for `test_weather.py`.
- Your solutions use conditionals and loops as described.
