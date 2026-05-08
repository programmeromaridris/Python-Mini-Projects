# Python Mini Projects

Small projects made while getting comfortable with Python syntax. Coming from gamedev, so the logic itself is not new. The point was learning syntax.

---

## Projects

### Dijkstra's Algorithm

Implements Dijkstra's shortest path algorithm on a weighted graph using a priority queue.

A `Graph` class holds an adjacency list and exposes a `shortest_distances(source)` method. It initializes all node distances to infinity, then greedily processes the nearest unvisited node using `heapq`. Neighbors are relaxed if a shorter path is found.

**Run it:**
```bash
python dijkstra-algo.py
```

**What this required:**
- Understanding priority queues and how `heapq` works in Python
- Why a visited set is needed to avoid reprocessing nodes
- Translating the algorithm's logic into a class with clean state management

---

Sudoku Solver

Solves a Sudoku grid using recursive backtracking.

The solver scans for empty cells (marked `0`), tries digits 1–9, validates against the current row, column, and 3x3 box, and recurses. If it hits a dead end, it resets the cell and backtracks. Prints all valid solutions.

**Run it:**
```bash
python sudoku-solver-algo.py
```

**What this required:**
- Implementing backtracking cleanly with a global grid
- Indexing 3x3 subgrids using integer division
- Understanding when and why to reset a cell after a failed branch
---

###  Quiz Game

A short trivia game with four questions and a scoring system.
---

###  Number Guesser

You pick the upper bound, the program picks a random number, and you keep guessing until you get it. Type `q` to quit and reveal the answer.

- Validates input and rejects non-numbers
- Rejects ranges of 0 or below
- Loops until you guess correctly or quit

**Run it:**
```bash
python guesser.py
```

---

###  Rock Paper Scissors

RPS against the CPU. Tracks wins on both sides across as many rounds as you want. Type `Q` to quit.

---

###  Weather App

Takes a city name, hits the OpenWeatherMap API, and returns the current weather and temperature.

This one went a step above syntax practice. Had to read API documentation, understand how HTTP requests work, and handle cases where the city is not found.

**Run it:**
```bash
python weather.py
```

**What I learned here specifically:**
- How to use `requests` to make HTTP GET requests
- Reading API documentation and constructing a URL with query parameters
- Parsing a JSON response with `.json()` and navigating nested keys
- Basic error handling based on response codes

---

###  Password Manager

A simple in-memory account system. You can create an account and log back in. Passwords are never stored as plain text.

This one introduced hashing. The point was understanding why you do not store raw passwords.

**Run it:**
```bash
python password_manager.py
```

**What I learned here specifically:**
- What hashing is and why it is used for passwords instead of encryption
- Using `hashlib.sha256` to hash a string
- Using `getpass` so the password does not echo in the terminal
- Storing and comparing hashed values instead of the original input

---

## General Python Syntax Things Picked Up

The logic here is nothing new, these are absolute beginner friendly projects. The point was getting used to how Python syntax looks and feels

- How Python uses indentation instead of curly braces to define blocks
- Using `input()` to get user input and how it always returns a string
- Type conversion: `int()`, `str()`, and checking first with `.isdigit()`
- `if / elif / else` chaining and how Python reads top to bottom
- The `not in` and `and` / `or` operators for readable conditionals
- `quit()` as a way to exit mid-script
- `import random`: `random.randint()` and `random.choice()`
- `import time`: using `time.sleep()` for small pacing delays
- `.lower()` for case-insensitive input handling

---

Will add more projects
