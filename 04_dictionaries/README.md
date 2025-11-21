# Exercise 04: Dictionaries

## Theme: Student Gradebook

## Objective

Practice working with dictionaries including creating, accessing, modifying, and iterating through key-value pairs.

## Instructions

You are building a simple student gradebook system. Complete the functions in `gradebook.py` to perform various dictionary operations.

Implement these functions:

1. `create_student(name: str, grade: int) -> dict`
   - Create and return a dictionary with keys `"name"` and `"grade"`.
   - Example: `{"name": "Alice", "grade": 85}`

2. `get_student_grade(student: dict) -> int`
   - Return the grade from the student dictionary.
   - Assume the key `"grade"` exists.

3. `update_grade(student: dict, new_grade: int) -> dict`
   - Update the student's grade to `new_grade`.
   - Return the modified dictionary.

4. `add_subject(student: dict, subject: str, score: int) -> dict`
   - Add a new key-value pair to the student dictionary where the key is `subject` and value is `score`.
   - Return the modified dictionary.

5. `get_all_subjects(student: dict) -> list[str]`
   - Return a list of all keys in the student dictionary.

6. `get_average_score(scores: dict[str, int]) -> float`
   - Calculate and return the average of all values in the `scores` dictionary.
   - Return `0.0` if the dictionary is empty.

7. `student_exists(gradebook: dict[str, int], student_name: str) -> bool`
   - Check if `student_name` exists as a key in the `gradebook` dictionary.
   - Return `True` if it exists, `False` otherwise.

8. `combine_gradebooks(gradebook1: dict, gradebook2: dict) -> dict`
   - Combine two gradebook dictionaries into a new dictionary.
   - If a key exists in both, use the value from `gradebook2`.
   - Return the combined dictionary.

## Example

```python
student = create_student("Bob", 78)  # {"name": "Bob", "grade": 78}
get_student_grade(student)  # 78
update_grade(student, 82)  # {"name": "Bob", "grade": 82}
add_subject(student, "math", 90)  # {"name": "Bob", "grade": 82, "math": 90}
get_all_subjects(student)  # ["name", "grade", "math"]
get_average_score({"math": 90, "science": 85})  # 87.5
student_exists({"Alice": 85, "Bob": 90}, "Alice")  # True
combine_gradebooks({"Alice": 85}, {"Bob": 90, "Alice": 88})  # {"Alice": 88, "Bob": 90}
```

## Required Knowledge: Dictionaries

Dictionaries store data as key-value pairs. Keys must be unique and are typically strings, while values can be any data type.

```python
person = {"name": "John", "age": 30, "city": "Melbourne"}
# Access values using keys
name = person["name"]  # "John"
age = person["age"]  # 30
```

## Required Knowledge: Adding and Modifying Dictionary Items

You can add new key-value pairs or modify existing ones using bracket notation.

```python
car = {"brand": "Toyota", "year": 2020}
car["color"] = "red"  # Add new key-value pair
car["year"] = 2021  # Update existing value
# car is now {"brand": "Toyota", "year": 2021, "color": "red"}
```

## Required Knowledge: Dictionary Methods

Common dictionary operations:

```python
inventory = {"apples": 10, "bananas": 5, "oranges": 8}

# Get all keys
keys = inventory.keys()  # dict_keys(['apples', 'bananas', 'oranges'])
keys_list = list(inventory.keys())  # Convert to list

# Get all values
values = inventory.values()  # dict_values([10, 5, 8])

# Check if key exists
has_apples = "apples" in inventory  # True
has_grapes = "grapes" in inventory  # False

# Get value safely (returns None if key doesn't exist)
apple_count = inventory.get("apples")  # 10
grape_count = inventory.get("grapes")  # None
```

## Required Knowledge: Combining Dictionaries

You can combine dictionaries using the `|` operator (Python 3.9+) or the `update()` method.

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "b": 4}

# Using | operator (creates new dict)
combined = dict1 | dict2  # {"a": 1, "b": 4, "c": 3}

# Using update() method (modifies dict1)
dict1.update(dict2)  # dict1 becomes {"a": 1, "b": 4, "c": 3}
```

## Running the Tests

```pwsh
pytest 04_dictionaries/test_gradebook.py -v
```

## Success Criteria

- All tests pass for `test_gradebook.py`.
- Your solutions use appropriate dictionary methods and operations.
