Emoji Rock-Paper-Scissors ✊ ✋ ✌️

A visually engaging, console-based Rock-Paper-Scissors game. This version uses Colorama to highlight game outcomes and Emojis to provide a modern user experience.
✨ Key Features

  Visual Feedback: Uses Fore.GREEN for wins, Fore.RED for losses, and Fore.MAGENTA for ties.

  Emoji Interface: Clear visual representation of Rock, Paper, and Scissors.

  Smart Logic: A robust conditional system to determine the winner between the Player and the CPU.

  Error Handling: Includes a "Beyond Limit" check for invalid inputs.

🛠️ How It Works

The script assigns numerical values to each move:

  1 = Rock ✊

  2 = Paper ✋

  3 = Scissors ✌️

The CPU generates a random integer between 1 and 3 using the random module, and the winner is decided based on standard game rules.
🚀 Setup

  Install the required dependency:
    Bash

    pip install colorama

  Run the game:
    Bash

    python3 rock_paper_scissor.py
