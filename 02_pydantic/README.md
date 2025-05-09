
# 🍎 Fruit Model with Pydantic & Type Annotations

This small script demonstrates the use of **Pydantic** models with advanced type hints using **Python's typing system**, `Annotated`, and `Literal`. It includes **runtime validation** for structured data representing a fruit object.

## 📦 Features

- `BaseModel` from Pydantic to define and validate data models.
- Use of:
  - `str`, `float`, `dict`, `list`, `tuple` from `typing`
  - `Literal` to enforce fixed string choices
  - `Annotated` with `Gt(0)` to enforce a constraint that `weight > 0`

## 🧪 Example

```python
from typing import Annotated, Literal
from annotated_types import Gt
from pydantic import BaseModel

class Fruit(BaseModel):
    name: str
    color: Literal['red', 'green']
    weight: Annotated[float, Gt(0)]
    bazam: dict[str, list[tuple[int, bool, float]]]

# ✅ Valid
print(
    Fruit(
        name="Muskan",
        color="red",
        weight=4.2,
        bazam={"basketball": [(1, True, 0.1)]}
    )
)

# ❌ Invalid: `name` expects a string but receives an integer
print(
    Fruit(
        name=7,
        color="red",
        weight=4.2,
        bazam={"football": [(1, True, 0.1)]}
    )
)
````

## 🚫 Error Handling

The second `Fruit` object will raise a **validation error** because the `name` field expects a `str`, but an `int` (`7`) is given.

### ❗ Output:

```
pydantic_core._pydantic_core.ValidationError: 1 validation error for Fruit
name
  Input should be a valid string [type=string_type, input_value=7, input_type=int]
```

---

## 🧠 Difference Between `pydantic` and `mypy`

| Feature        | `pydantic`                               | `mypy`                                     |
| -------------- | ---------------------------------------- | ------------------------------------------ |
| Type checking  | **Runtime**                              | **Static (Compile-time)**                  |
| Purpose        | Validate and parse data in real time     | Detect type errors before execution        |
| Use case       | API input validation, data integrity     | IDE/static code analysis, linting          |
| Error example  | Catches invalid types **when code runs** | Catches invalid types **before code runs** |
| Based on       | Pydantic’s own parser and validator      | Python's `typing` module                   |
| Extra features | Custom validators, field constraints     | N/A (only checks types, not logic)         |

### 👇 Summary:

* Use **`pydantic`** when you want to **enforce and validate data at runtime** (e.g., API inputs).
* Use **`mypy`** to **catch bugs early** by checking type correctness during development (before the program runs).

---


