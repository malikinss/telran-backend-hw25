# HW25: Stack with Max and NumberBox Implementation

## Task Definition

This homework contains two main tasks:

1. Implement a stack with O(1) max operation (`MyStackInt`).
2. Implement a number container with efficient addition, removal, filtering, and deduplication (`NumberBox`).

---

### Task 1: `MyStackInt`

#### Description

Implement a class `MyStackInt` — a stack for integers that supports:

-   **Push** a number (`push`)
-   **Pop** a number (`pop`)
-   **Retrieve the maximum** number (`max`)

All operations must run in **O(1)** time.

#### Method Requirements

-   `push(num: int) -> None`
-   `pop() -> int` — raises `IndexError` if empty
-   `max() -> int` — raises `IndexError` if empty

#### Example usage

```python
s = MyStackInt()
s.push(3)
s.push(5)
assert s.max() == 5
assert s.pop() == 5
assert s.max() == 3
```

---

### Task 2: `NumberBox`

#### Description

Implement a class `NumberBox` for storing integers with efficient operations:

-   Adding a number
-   Removing a number
-   Removing numbers by predicate
-   Removing numbers in a range
-   Removing duplicates
-   Iteration

All operations should be efficient and suitable for large datasets.

#### Method Requirements

-   `add_number(num: int) -> None`
-   `remove_number(num: int) -> int | None`
-   `remove_numbers_predicate(pred: Callable[[int], bool]) -> int`
-   `remove_numbers_range(min: int, max: int) -> int`
-   `distinct() -> int`
-   `__iter__() -> Iterator[int]`

---

## 📝 Description

-   `MyStackInt` uses two internal stacks to maintain O(1) push, pop, and max operations.
-   `NumberBox` uses `SortedList` for efficient addition, removal, and range operations.

## 🎯 Purpose

-   Practice implementing optimized data structures.
-   Handle edge cases with proper error handling.
-   Test data structure functionality with unit tests.

## 🔍 How It Works

-   `MyStackInt` maintains a separate `_max_stack` for tracking current maximum.
-   `NumberBox` maintains a sorted list internally, supporting efficient queries and removals.

## 📜 Output Example

```python
# MyStackInt
s = MyStackInt()
s.push(3)
s.push(5)
print(s.max())  # 5

# NumberBox
nb = NumberBox()
nb.add_number(3)
nb.add_number(1)
print(list(nb))  # [1, 3]
```

## 📦 Usage

1. Clone the repository.
2. Implement missing methods if any.
3. Run tests to verify correctness.

## 🧪 Running Tests

```bash
python -m unittest discover -s tests -v
```

## ✅ Dependencies

-   Python 3.10+
-   `sortedcontainers` package

## 🗂 Project Structure

```
.
├── main.py
├── .gitignore
├── /.vscode
│   ├── launch.json
│   ├── settings.json
│   └── tasks.json
├── src
│   ├── __init__.py
│   ├── my_stack_int.py
│   └── number_box.py
└── tests
    ├── __init__.py
    ├── test_my_stack_int.py
    └── test_number_box.py
```

## 📊 Project Status

✅ Implemented `MyStackInt`
✅ Implemented `NumberBox`
✅ All unit tests passing

## 📄 License

MIT License

---

## 🧮 Conclusion

This homework demonstrates efficient stack and container implementations in Python, along with comprehensive unit testing.

---

Made with ❤️ and `Python` by **Sam-Shepsl Malikin** 🎓
© 2025 All rights reserved.
