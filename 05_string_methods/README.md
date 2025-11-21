# Exercise 05: String Methods

## 🎯 Theme: Text Message Processor

## 📝 Objective

Practice using Python string methods to manipulate, transform, and analyze text data.

## 📋 Instructions

You are building a text message processing system. Complete the functions in `text_processor.py` to perform various string operations.

Implement these functions:

1. `normalize_text(text: str) -> str`
   - Remove leading and trailing whitespace.
   - Convert the entire string to lowercase.
   - Return the normalized text.

2. `count_words(text: str) -> int`
   - Count the number of words in the text.
   - Words are separated by spaces.
   - Return the word count.

3. `is_shouting(text: str) -> bool`
   - Determine if the text is "shouting" (all uppercase letters).
   - Ignore non-letter characters.
   - Return `True` if shouting, `False` otherwise.
   - Empty strings or strings with no letters should return `False`.

4. `censor_word(text: str, word: str) -> str`
   - Replace all occurrences of `word` in `text` with asterisks of the same length.
   - Replacement should be case-insensitive.
   - Return the censored text.

5. `create_acronym(phrase: str) -> str`
   - Create an acronym from the phrase by taking the first letter of each word.
   - Convert to uppercase.
   - Return the acronym.

6. `reverse_words(text: str) -> str`
   - Reverse the order of words in the text.
   - Return the text with words in reverse order.

7. `is_valid_email(email: str) -> bool`
   - Check if the email contains exactly one `@` symbol.
   - Check if there's at least one character before and after the `@`.
   - Check if there's at least one `.` after the `@`.
   - Return `True` if valid, `False` otherwise.

8. `extract_numbers(text: str) -> list[int]`
   - Extract all numeric "words" from the text.
   - Convert them to integers and return as a list.
   - Non-numeric words should be ignored.

## 💡 Example

```python
normalize_text("  Hello WORLD  ")  # "hello world"
count_words("Hello world from Python")  # 4
is_shouting("HELLO!")  # True
censor_word("Hello world, hello!", "hello")  # "***** world, *****!"
create_acronym("as soon as possible")  # "ASAP"
reverse_words("Hello world")  # "world Hello"
is_valid_email("test@example.com")  # True
extract_numbers("I have 2 cats and 3 dogs")  # [2, 3]
```

## 📚 Required Knowledge: Strings are immutable

In Python, strings are **immutable**, meaning they cannot be changed after they are created. Any operation that modifies a string will actually create a new string.

This also means you can't do:

```python
my_string = "Hello"
my_string[0] = "Y"  # This will raise an error
```

Instead, you would create a new string:

```python
my_string = "Hello"
my_string = "Y" + my_string[1:]  # Now my_string is "Yello"
```

This takes a bit of getting used to, but is important to understand when working with strings and string methods.

## 📚 Required Knowledge: Basic String Methods

Python strings have built-in methods for common operations:

```python
text = "  Hello World  "
cleaned = text.strip()  # "Hello World" - removes leading/trailing whitespace
lower = text.lower()  # "  hello world  "
upper = text.upper()  # "  HELLO WORLD  "
```

## 📚 Required Knowledge: String Splitting and Joining

Use `.split()` to break strings into lists and `.join()` to combine lists into strings:

```python
sentence = "Hello world from Python"
words = sentence.split()  # ["Hello", "world", "from", "Python"]
word_count = len(words)  # 4

# Join list into string
words = ["Hello", "world"]
result = " ".join(words)  # "Hello world"
```

## 📚 Required Knowledge: String Searching and Replacement

Find and replace text within strings:

```python
text = "Hello world"
position = text.find("world")  # 6 (returns -1 if not found)
has_hello = "Hello" in text  # True

# Replace text
new_text = text.replace("world", "Python")  # "Hello Python"
# Case-insensitive replace requires .lower() or .upper() first
```

## 📚 Required Knowledge: String Checking Methods

Check string properties:

```python
text1 = "HELLO"
text1.isupper()  # True
text1.islower()  # False

text2 = "hello"
text2.islower()  # True

num_str = "123"
num_str.isdigit()  # True

alpha_str = "abc"
alpha_str.isalpha()  # True
```

## 📚 Required Knowledge: Counting Occurrences

Count how many times a substring appears:

```python
text = "hello world, hello Python"
count = text.count("hello")  # 2

# Count specific characters
at_count = "test@example.com".count("@")  # 1
```

## 📚 Required Knowledge: String Formatting

Create formatted strings using f-strings:

```python
name = "Alice"
age = 25
message = f"Hello, {name}! You are {age} years old."
# "Hello, Alice! You are 25 years old."

# Can include expressions
result = f"2 + 2 = {2 + 2}"  # "2 + 2 = 4"
```

## 🧪 Running the Tests

```pwsh
pytest 05_string_methods/test_text_processor.py -v
```

## ✅ Success Criteria

- All tests pass for `test_text_processor.py`.
- Your solutions use appropriate string methods.
