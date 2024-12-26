# Dice Game: Craps Simulation

## Description

This is a simple implementation of the **Craps** dice game in Python. The game simulates rolling two six-sided dice and follows the basic rules of Craps. The player wins or loses based on the outcome of the rolls.

### Rules:
1. **Initial Roll (Come-out Roll):**
   - If the sum of the dice is **7 or 11**, you win immediately.
   - If the sum of the dice is **2, 3, or 12**, you lose immediately.
   - If the sum is **4, 5, 6, 8, 9, or 10**, this becomes your **goal** number.

2. **Subsequent Rolls (After Setting a Goal):**
   - You continue rolling the dice until you either roll the **goal number** again (win) or roll a **7** (lose).

### Game Flow:
1. The game starts by rolling two dice.
2. If the sum of the dice is 7 or 11, you win and the game ends.
3. If the sum of the dice is 2, 3, or 12, you lose and the game ends.
4. If the sum is 4, 5, 6, 8, 9, or 10, that becomes the goal number.
5. You continue rolling the dice until:
   - You roll the goal number again (win).
   - You roll a 7 (lose).

## Features

- Random dice rolls between 1 and 6 (inclusive).
- Win condition on the initial roll if the sum is 7 or 11.
- Lose condition on the initial roll if the sum is 2, 3, or 12.
- Goal-setting if the sum is 4, 5, 6, 8, 9, or 10, and the player must continue rolling until they either match the goal or roll a 7.
- The game ends when a win or loss is determined.

## Requirements

- **Python 3.x**: This game uses the built-in `random` module, so no external dependencies are required.

## How to Run

1. Clone or download the repository to your local machine.
2. Navigate to the folder where the script is saved.
3. Run the script using Python:

   ```bash
   python dice_game.py
