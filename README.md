# Python Number Guessing Game

A classic, terminal-based number guessing game built using Python. The game randomly selects a number between **1 and 100**, and challenges the player to guess it within **7 attempts**.

---

## 🚀 Features

* **Live Feedback:** Tells you whether your guess is too high or too low after every attempt.
* **Smart Input Validation:** Safely handles non-numeric inputs or out-of-range numbers without penalizing your guess count.
* **Performance Timer:** Tracks exactly how many seconds it takes you to guess the correct number.
* **Session Statistics:** Keeps track of your total **Wins** and **Losses** across multiple rounds.
* **Play Again Option:** Allows you to seamlessly restart a new round without exiting the script.

---

## 🛠️ Prerequisites

To run this game, you only need **Python 3.x** installed on your system. It relies entirely on standard built-in libraries (`random` and `time`), so **no external packages or installations are required**.

---

## 🎮 How to Run and Play

1. **Clone the Repository:**
```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git
cd YOUR-REPOSITORY-NAME

```


2. **Run the Game:**
```bash
python Number-guessing_game.py

```


3. **Gameplay Rules:**
* Look at the range provided (Default: 1 to 100).
* Type your number and press `Enter`.
* Follow the hints (`Too high!` or `Too low!`) to narrow down your next choice.
* Win by guessing the correct number before running out of your **7 guesses**.



---

## 📑 Code Overview

The script is structured into two primary loops:

* **The Outer Loop (`is_playing`):** Manages the overall game session, allowing you to play multiple rounds and displaying final win/loss stats when you choose to quit.
* **The Inner Loop (`is_running`):** Manages the active game round, processing individual inputs, counting down attempts, and tracking elapsed time using Python's `time` module.
