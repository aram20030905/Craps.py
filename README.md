# Craps.py
# Dice Game: Craps Simulation

## Description

This is a simple implementation of the **Craps** dice game in Python. The game simulates rolling two six-sided dice and follows the basic rules of Craps. The player wins or loses based on the outcome of the rolls.

### Rules:
- **Initial Roll (Come-out Roll):**
  - If the sum of the dice is **7 or 11**, you win immediately.
  - If the sum of the dice is **2, 3, or 12**, you lose immediately.
  - If the sum is **4, 5, 6, 8, 9, or 10**, this becomes your **goal** number.

- **Subsequent Rolls (After Setting a Goal):**
  - You continue rolling the dice until you either roll the **goal number** again (win) or roll a **7** (lose).

### Flow:
1. The game starts with rolling two dice.
2. The sum of the dice is checked:
   - If the sum is 7 or 11, the player wins.
   - If the sum is 2, 3, or 12, the player loses.
   - If the sum is 4, 5, 6, 8, 9, or 10, it sets the "goal" for the next rolls.
3. The player continues rolling the dice until they either roll the goal number again (win) or roll a 7 (lose).

## Features

- Random dice rolls between 1 and 6 (inclusive).
- Check for immediate win or loss on the first roll (come-out roll).
- Set a goal if the sum is between 4 and 10 (inclusive), and roll until the goal number or a 7 is rolled.
- The game ends when the player wins or loses.

## Requirements

This game requires Python 3.x. No additional dependencies are required since it only uses the built-in `random` library.

## How to Run

1. Clone or download the repository to your local machine.
2. Navigate to the folder where the script is saved.
3. Run the script using Python:

   ```bash
   python dice_game.py
