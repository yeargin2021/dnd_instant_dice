# D&D Instant Dice

## Description

D&D Instant Dice is a simple, interactive Python application designed to simulate dice rolls for tabletop games like Dungeons & Dragons. It allows users to input the maximum value of a dice roll (e.g., 20 for a D20 roll) and generates a random number within that range. The app is a lightweight and easy-to-use tool for players who need quick, fair, and randomized results during their game sessions.

## Features

- Allows the user to specify the maximum roll value (between 1 and 100).
- Generates a random number within the user-defined range.
- Offers an option to continue rolling or exit the app after each roll.
- Provides an engaging and user-friendly text-based interface.

## How to Use

1. Run the script using your Python interpreter:
   ```bash
   python dnd_instant_dice.py
   ```

2. Enter the maximum value for your dice roll (e.g., `20` for a D20).

3. Press `Enter` to roll the dice.

4. View the randomly generated result.

5. Choose whether to roll again (`y`) or exit the app (`n`).

## Example Usage

```plaintext
D&D INSTANT DICE
----------------
For maximum roll enter a number between 1 and 100: 20

Press Enter to generate a random number between 1 and 20:

*User Presses Enter*

18

Continue? y/n: y

*User enters a new max roll or continues exiting when ready*
```

## Requirements

- Python 3.x (tested on the latest Python versions)

No additional libraries or dependencies are required.

## Customization

You can modify the script to:
- Set a default maximum roll value if the user doesn’t input one.
- Add other options for predefined dice types (e.g., D4, D6, D10, D12, etc.).
- Handle invalid inputs gracefully (e.g., non-numeric values or out-of-range numbers).

## Benefits

- Lightweight and cross-platform.
- No third-party libraries or administrator-level permissions required.
- Useful for casual D&D players who don’t have physical dice at hand.

## License

This project is licensed under the MIT License.

---
Enjoy using D&D Instant Dice for your adventures!