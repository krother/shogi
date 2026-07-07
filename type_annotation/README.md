
# Type Checking Python Code

practical hints for getting started

**by Dr. Kristian Rother**

[www.academis.eu](https://www.academis.eu)

---

## Goals of this workshop

In this tutorial you type annotate a small Python program.
It is an opportunity to try out different aspects of type annotation:

- run a type checker
- annotate variables
- define types
- nested types
- annotate functions
- ignore annotations

---

## How to get started

Download or clone the repository. 
Install and start the code in `debugging/` with ``uv`` from a terminal:

    pip install uv
    uv sync
    uv run fastapi run --reload app.py

then visit localhost:8000 in your browser.

---

## Run a type checker

**ty** is a fast type checker written in Rust.

```
uv add ty
uv run ty check .
```

or

```
pip install ty
ty check .
```

---

## Annotate variables

Here are some examples:

```python
running: bool = True

piece: str = "lion"

player: int|None = 1
```

---

## Nested types

Specify what tuples, lists and dictionaries should contain:

```python
position: tuple[int, int]

names: list[str]

field: list[list[tuple[str, int|None]]]
```

Annotate some of the variables in `shogi.py`. Then run `ty` again.

---

## Literals

Literals protect you from typos!

```python
from typing import Literal

Player = Literal[1, -1]

Piece = Literal["lion", "giraffe", "elephant", "chick"]
```

Use Literals for the player and pieces. Then run `ty` again.

---

## Define types

Enhance readability with more precise types:

```python
Position = tuple[int, int]
position: Position = (1, 2)

Field = list[list[tuple[Piece, Player|None]]]
```

Use the above definition to make the type annotation of the `field` variable more convenient to read.

---

## Annotate functions

Annotating function **parameters** and **return types** is a great starting point to type annotate a larger program.
Here is a minimalistic example:

```python
def add(a: int, b: int) -> int:
```

Apply type annotations to `execute_move()`:

```python
def execute_move(field: Field,
                 player: Player,
                 move: tuple[Position, Position]
                 ) -> tuple[Field, Player, str]:
```

---

## Special types

Some types need to be imported from the **typing** module:

```python
from typing import (
  Any,         # placeholder that matches everything
  Callable,    # function
  Sequence,    # lists, generators, files etc.
  cast         # function to convert type annotations (ugly)
)
```

In the shogi game, we don't need these for now.

---

## Ignoring types

Sometimes types are ugly to resolve and you may not want to check them:

```python
fruit: str = "apple"
fruit = 42  # type: ignore
```

---

## Links

- [mypy](https://www.mypy-lang.org/) - a slower type checker that works with most libraries
- [pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) - VS Code plugin that checks types as you write code
