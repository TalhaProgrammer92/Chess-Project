# ♟️ Console Chess Game

A fully-featured, console-based 2D Chess game built in Python — no GUI, just pure logic and terminal graphics. Designed as a challenge to push coding boundaries and create an engaging multiplayer chess experience using object-oriented programming and file handling.

## 🚀 Features

- 2D chess board rendered in the terminal
- Support for all standard chess rules:
  - Piece movement and capturing
  - Check, checkmate, and stalemate detection
  - Castling, en passant, and pawn promotion
- Two-player (local) mode
- Player names and turn tracking
- Game history (win/loss record)
- Scoreboard with highest scores
- Save and load games using files
- Clean, modular OOP design

## 🛠️ Technologies

- Language: Python 3
- Concepts Used:
  - Object-Oriented Programming (OOP)
  - File handling
  - Modular code architecture
  - Console I/O

## 🎮 How to Play

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/console-chess-python.git
   cd console-chess-python
   ```

2. Run the game:

   ```bash
   python main.py
   ```

3. Follow the on-screen prompts to start a new game or load a saved one.

## 🧠 Architecture Overview

* `main.py` – Entry point of the game
* `board.py` – Handles board rendering and piece placement
* `pieces/` – Folder containing each piece class (Pawn, Rook, Knight, etc.)
* `game.py` – Core game logic and turn mechanics
* `utils.py` – Utility functions like validation, saving/loading, etc.
* `players.py` – Manages player information and score tracking

## 🏗️ Planned Features

* AI opponent (basic to intermediate difficulty)
* Undo/redo moves
* Chess timer per player
* Replay previous games
* Highlight legal moves in the console

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---
