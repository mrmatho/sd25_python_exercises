# Exercise 01: Variables and Data Types

## Theme: Coffee Shop Order

### Objective

Practice storing data in variables and working with different Python data types including strings, integers, floats, and booleans.

## Instructions

You are building a simple coffee shop order system. Your task is to create variables that store information about a customer's order.

Complete the `order.py` file by:

1. Create a variable `customer_name` that stores the customer's name as a string
2. Create a variable `drink_size` that stores the size as a string (small, medium, or large)
3. Create a variable `quantity` that stores the number of drinks as an integer
4. Create a variable `price_per_drink` that stores the price as a float
5. Create a variable `total_price` that calculates the total cost (quantity × price_per_drink)
6. Create a variable `is_loyalty_member` that stores whether the customer is a loyalty member as a boolean
7. Create a variable `discount_amount` that stores 0.0 if not a loyalty member, or 10% of total_price if they are a member
8. Create a variable `final_price` that calculates the total after discount (total_price - discount_amount)

## Example

If the customer is "Alice", orders 2 medium drinks at $4.50 each, and is a loyalty member:
- `customer_name` = "Alice"
- `drink_size` = "medium"
- ...etc.

NOTE: For items like `total_price`, `discount_amount`, and `final_price`, ensure you perform the  calculations in the code - not in your brain! The values must be computed using the variables you have already created. 

## Required Knowledge: Data types

Python uses a data type system called "duck typing" or "dynamic typing," which means that the *type of a variable is based on the value assigned to it*. The main data types you will work with in this exercise include:
- **String**: Used for text. Example: `street_address = "Waters Grove, Heathmont"`
- **Integer**: Used for whole numbers. Example: `count = 1`
- **Float**: Used for decimal numbers. Example: `percentage_tax = 28.5`
- **Boolean**: Used for true/false values. Example: `is_a_good_guy = True`

This exercise tests that the variables you create are of the correct data type and that calculations are performed correctly.

## Required Knowledge: Basic arithmetic

You will need to use basic arithmetic operations to calculate the total price, discount amount, and final price. The operations you could need include:

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Floor Division (`//`)
    - Floor division performs division and **rounds down** to the nearest whole number.
- Modulus (`%`)
    - The modulus operator returns the **remainder** of a division operation.
    - Modulus and floor division often get used together.

Note that we use `*` rather than `x` for multiplication in Python.

## Required Knowledge: Conditional statements

You will need to use an `if` statement to determine the discount amount based on whether the customer is a loyalty member.

In an `if` statement, if the condition evaluates to `True`, the block of code under the `if` statement will execute. If it evaluates to `False`, the block will be skipped.

### Example of an if statement

```python

if is_nice_guy:
    discount = 0.10  # 10% discount for nice guys
else:
    discount = 0.0   # No discount for not nice guys
```

## Running the Tests

Run the tests to check your solution:

```bash
pytest 01_variables_and_types/test_order.py -v
```

or using the Testing panel in VS Code.

## Success Criteria

All tests should pass when you run the test file. Note that for this task, the tests will error until you have entered values for each variable as specified
