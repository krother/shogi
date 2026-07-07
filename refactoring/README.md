
# Refactoring

A practical exercise in refactoring.

**by Dr. Kristian Rother**

[www.academis.eu](https://www.academis.eu)

---

## Goals of this workshop

In this tutorial, you start with a working, type-annotated version of the code. 
You will practise refactoring by:

- identify code smells
- apply 2-3 small refactorings
- apply 1 mid-size refactoring

---

## How to get started

Download or clone the repository. 
Install and start the code in `debugging/` with ``uv`` from a terminal:

    pip install uv
    uv sync
    uv run fastapi run --reload app.py

then visit localhost:8000 in your browser.

---

## Inspect code

Take a look at **shogi.py**

What do you not like about it?

---

## Running the tests

Run the tests with

```
uv run pytest
```

or

```
pip install pytest

pytest
```

---

## Small Refactorings

The general procedure for small refactorings is:

1. run tests
2. modify code
3. run tests again

Small refactorings should be done within a few minutes

---

## Examples of small refactorings

Small refactorings should be doable within a few minutes.
Examples of such refactorings are:

- rename a variable
- extract a function
- re-organize a loop

Find a place where you can apply a small refactoring in the code.

---

## Medium refactorings

- may take up to 1 hour
- may change the interface
- might require editing tests
- programmers can do these on their own

Replace the multiple if block in **execute_move()** by a more data structure that contains moves for each piece.

---

## Large Refactorings

- change the interface or architecture
- break the tests
- may take days or weeks
- stakeholders need to be involved

---

## Links

- [refactoring.guru/refactoring](https://refactoring.guru/refactoring) - a list of refactoring techniques and code smells
- [The Mikado Method](https://www.heise.de/ratgeber/Komplexe-Refactorings-mit-der-Mikado-Methode-durchfuehren-3347338.html) – a workflow for complex refactorings (in German)
