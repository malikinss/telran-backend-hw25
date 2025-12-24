# HW25:

## Task Definition

### Task 1: Implement a Stack with Max Operation in O(1)

#### Description

Implement a class `MyStackInt` — a stack for integers that supports the following operations:

1. **Push** a number onto the top of the stack (`push`)
2. **Pop** a number from the top of the stack and return it (`pop`)
3. **Retrieve the maximum number** in the stack (`max`)

All methods must run in **O(1)** time complexity.

---

#### Method Requirements

##### `push(num: int) -> None`

-   Adds the number `num` to the top of the stack.

##### `pop() -> int`

-   Removes the number at the top of the stack and returns it.
-   Raises `IndexError` if the stack is empty.

##### `max() -> int`

-   Returns the maximum number in the stack.
-   Raises `IndexError` if the stack is empty.

---

#### Additional Requirements

-   All methods must have **O(1)** time complexity.
-   The stack should only store integer (`int`) values.

---

#### Testing

Write tests to verify:

1. Correct behavior of `push` and `pop`.
2. Correct behavior of `max` after multiple push and pop operations.
3. Proper `IndexError` handling when calling `pop` or `max` on an empty stack.

**Example usage:**

```python
s = MyStackInt()
s.push(3)
s.push(5)
assert s.max() == 5
assert s.pop() == 5
assert s.max() == 3
```

### Task 2: Implementation of `NumberBox` Class

#### Description

You need to implement a class `NumberBox` — a data structure for storing integers with support for efficient addition, removal, and filtering of elements.

The implementation should prioritize **efficiency** of the underlying data structure for all operations.

After implementing the class, you should also write tests to verify that all methods work correctly.

---

#### `NumberBox` Class Requirements

##### Methods

1. **Constructor**

```python
NumberBox()
```

-   Initializes the container.
-   Choose the most **efficient internal data structure** for storing numbers.

---

2. **Add a number**

```python
addNumber(num: int)
```

-   Adds the integer `num` to the `NumberBox`.

---

3. **Remove a number**

```python
removeNumber(num: int) -> int | None
```

-   Removes the **first occurrence** of `num`.
-   Returns the removed number, or `None` if the number is not in the container.

---

4. **Remove numbers by predicate**

```python
removeNumbersPredicate(pred: Callable[[int], bool]) -> int
```

-   Removes all numbers for which `pred(number)` returns `True`.
-   `pred` is a function that takes an integer and returns `True` if it should be removed.
-   Returns the count of numbers removed.

---

5. **Remove numbers in a range**

```python
removeNumbersRange(min: int, max: int) -> int
```

-   Removes all numbers where `min <= number <= max`.
-   Returns the count of numbers removed.

---

6. **Iteration**

```python
__iter__() -> Iterator[int]
```

-   Allows iterating over all numbers in the `NumberBox`.
-   The order can follow the order of insertion or any other order suitable for the chosen efficient data structure.

---

7. **Remove duplicates**

```python
distinct() -> int
```

-   Removes all duplicate numbers, leaving only unique numbers.
-   Returns the count of duplicates removed.

---

#### Testing

-   You must write tests for all methods:

    -   Adding and removing numbers.
    -   Removing numbers by predicate.
    -   Removing numbers by range.
    -   Iteration over elements.
    -   Removing duplicates.

-   Tests should verify correct return values and container state after each operation.

---

#### Notes

-   Consider the choice of data structure carefully: efficient addition, removal, and uniqueness checks are important.
-   All methods should handle large datasets efficiently.

## 📝 Description

## 🎯 Purpose

## 🔍 How It Works

## 📜 Output Example

## 📦 Usage

## 🧪 Running Tests

## ✅ Dependencies

## 🗂 Project Structure

## 📊 Project Status

## 📄 License

MIT License

---

## 🧮 Conclusion

---

Made with ❤️ and `Python` by **Sam-Shepsl Malikin** 🎓
© 2025 All rights reserved.
