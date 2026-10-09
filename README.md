# 🏝️ Treasure Island Adventure — Python CLI Game

**Choose your path. Avoid the dangers. Find the treasure!**

Treasure Island Adventure is an interactive, text-based game built with **Python 3**. Players explore a series of choices at a crossroad, a river, and three mysterious doors. Each decision changes the outcome: **find the treasure or face game over**.

This beginner-friendly project demonstrates practical Python skills, from conditional statements and functions to input validation and automated testing.

> **Project scope:** This is a terminal-based learning project, not a graphical video game. No external packages are required.

## ✨ Features

- 🧭 **Choose your own path** through a branching storyline.
- 🚪 **Three doors, three outcomes**: treasure, fire, or a beast.
- ✅ **Input validation**: unsupported answers trigger a helpful message and a retry.
- 🔡 **Case-insensitive input**: `LEFT`, `left`, and ` left ` are accepted.
- 🔁 **Replay option**: start another round without restarting the program.
- 🧩 **Reusable functions** for checking answers and running the game.
- 🧪 **Automated unit tests** covering game paths, invalid inputs, and replay.
- 💻 **No third-party dependencies**: runs with the Python standard library.

## 🛠️ Technologies and concepts

| Technology / concept | How it is used |
| --- | --- |
| Python 3 | Game implementation |
| `if`, `elif`, `else` | Story branching and game outcomes |
| Functions | Organizing game and input logic |
| `while` loop | Input retries and replay |
| `input()` and `print()` | Terminal interaction |
| `.strip()` and `.lower()` | Flexible, normalized input |
| `return` | Reporting whether the treasure was found |
| `unittest` and `unittest.mock` | Automated testing |

## 📁 Project structure

```text
treasure-island-adventure/
├── treasure_island.py       # Main interactive game
├── test_treasure_island.py  # Automated unit tests
├── README.md                # Documentation
└── .gitignore               # Files Git should exclude
```

## 🚀 Getting started

### Requirements

Install **Python 3**. Check your installation:

```bash
python --version
```

On some systems use `python3 --version`, or `py --version` on Windows.

### Clone the repository

```bash
git clone https://github.com/Fafali1234557/treasure-island-adventure.git
cd treasure-island-adventure
```

Replace `Fafali1234557` with your own GitHub username. If you haven't uploaded the project yet, simply extract the downloaded ZIP file and open the folder in your terminal.

### Start the adventure

```bash
python treasure_island.py
```

If needed, use `python3 treasure_island.py` on macOS/Linux or `py treasure_island.py` on Windows.

## 🎮 Example gameplay

```text
=======================================
       WELCOME TO TREASURE ISLAND
=======================================
Your mission is to find the treasure.

You are at a crossroad. Do you go left or right? LEFT
You reached a river. Do you swim or wait? wait
You see 3 doors: red, blue, yellow. Choose one: yellow

Congratulations! You found the treasure! YOU WIN!

Would you like to play again? (yes/no): no
Thanks for playing Treasure Island! Goodbye!
```

The game accepts answers regardless of capitalization and asks again if you type an unsupported choice.

## 🗺️ Adventure decision map

```text
START
  |
  +-- Right --------------------> Trap! Game Over
  |
  +-- Left
        |
        +-- Swim --------------> Shark! Game Over
        |
        +-- Wait
              |
              +-- Red ---------> Fire room! Game Over
              +-- Blue --------> Beast room! Game Over
              +-- Yellow ------> TREASURE! You win!
```

**Hint:** Explore the routes and see if you can discover the winning combination yourself.

## 🧠 How the code works

**1. `get_choice(prompt, valid_options)`** repeatedly asks the player for an answer. It strips extra spaces, converts text to lowercase, and only returns an allowed option.

**2. `treasure_game()`** runs one adventure and uses conditional statements to determine the result of each decision. It returns `True` for a win and `False` for a loss.

**3. `main()`** handles replay. The player can enter `yes`, `y`, `no`, or `n` after a round.

**4. `if __name__ == "__main__":`** launches the game when the file is run directly, while allowing its functions to be imported for tests. The entry point also closes gracefully on Ctrl+C or end-of-input.

## 🧪 Run automated tests

From the project folder, run:

```bash
python -m unittest -v
```

The included test suite checks winning and losing paths, different capitalization, retrying invalid choices, and replaying the adventure.

## 📚 What I learned

By developing and improving this project, I practised:

- Breaking a problem into small, reusable functions
- Designing decision-based programs with nested conditions
- Using loops to improve user experience
- Validating and normalizing terminal input
- Keeping game logic separate from the replay flow
- Writing tests to verify expected outcomes
- Organizing and documenting a Python project for GitHub

## 🔮 Future improvements

- [ ] Add more scenes, clues, and alternate endings
- [ ] Track wins and losses across rounds
- [ ] Add a score or health system
- [ ] Introduce random events and hidden items
- [ ] Save and load progress
- [ ] Build a graphical version of the game

## 🤝 Contributions and feedback

Suggestions and improvements are welcome. You can fork the project, experiment with new story paths, or open an issue with ideas.

## ⭐ Support

If you enjoyed exploring this beginner Python project, consider starring the repository!

**Made while learning Python, one decision at a time.** 🐍🏴‍☠️
