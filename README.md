# Number Guessing Game

This Python project is a number guessing game where the player attempts to guess a randomly chosen number between 1 and 50. The game includes two difficulty levels: **easy** and **hard**, each giving the player a different number of attempts to guess the correct number.

## Features

- **Easy Mode**: Player gets 10 attempts to guess the number.
- **Hard Mode**: Player gets 5 attempts to guess the number.
- Provides feedback on whether the guess is too high or too low.
- Announces the winner if the correct number is guessed or the player runs out of attempts.

## How It Works

1. At the start of the game, a random number between 1 and 50 is generated.
2. The player chooses the difficulty level:
    - **easy** (10 attempts)
    - **hard** (5 attempts)
3. The player then guesses the number, and the game provides hints such as "too high" or "too low" based on the guess.
4. The game continues until the player guesses the correct number or runs out of attempts.

## Example

```bash
Enter the level of difficulty...Type 'easy' or 'hard': easy
You have 10 attempts to guess the number!
Make a guess: 25
Your guess is too high!
Make a guess: 10
Your guess is too low!
Make a guess: 18
Your guess is correct...You won!
```

## How to Run

1. Ensure Python is installed on your system.
2. Clone or download the project files from this repository.
3. Create a Python file `Guesslogo.py` and add a `logo` variable to store the game's logo.
    Example `Guesslogo.py`:

    ```python
    logo = """
    ########################
    #  Number Guessing Game #
    ########################
    """
    ```

4. Run the game using:

    ```bash
    python guess_game.py
    ```

5. Follow the on-screen instructions to play.

## Customization

- You can modify the number range (1 to 50) by editing the `random.randint(1, 50)` function.
- Adjust the number of attempts for each difficulty by modifying the `attempts` values for both "easy" and "hard" modes.

## Dependencies

- This project uses Python's built-in `random` module, so no external dependencies are required.
