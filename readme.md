# Peek-A-Boo Game

## Introduction
Welcome to Peek-A-Boo! This is a simple console-based game where you try to uncover pairs of elements on a grid. The goal is to match pairs and reveal the entire grid.

## Instructions
To play the game, follow these steps:

1. Run the game by providing the grid size as a command-line argument. For example:
    ```bash
    python my_game_script.py 4
    ```

2. You will be presented with a grid of hidden elements.

3. Use the menu options to interact with the game:
    - **1. Let me select two elements**: Manually choose two elements to uncover and match.
    - **2. Uncover one element for me**: Let the game randomly uncover one element for you.
    - **3. I give up - reveal the grid**: Give up and reveal all the elements on the grid.
    - **4. New game**: Start a new game with a new grid.
    - **5. Exit**: Exit the game.

4. The game will display the updated grid, your score, and any relevant messages based on your choices.

5. The game continues until you choose to exit or start a new game.

## Classes

### MyGame Class
- The main class responsible for the game's logic and user interaction.

### MyGrid Class
- Handles the grid, element visibility, and scoring.

## Dependencies
- The game utilizes basic Python libraries and assumes a UNIX-like environment for clearing the console screen (`os.system("clear")`).

## Usage
1. Clone the repository.
2. Run the game script with the desired grid size as a command-line argument.

## Example
```bash
python my_game_script.py 6
```

## Notes
- Ensure that the grid size provided as an argument is a positive integer.

Enjoy playing Peek-A-Boo! 🎮