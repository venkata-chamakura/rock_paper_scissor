Rock Paper Scissors Lizard Spock ✊ ✋ ✌️ 🦎 🖖

A Python-based expansion of the classic Rock Paper Scissors game. This version adds two new variables—Lizard and Spock—increasing the number of possible outcomes and making the strategy more interesting.
📜 The Rules

The game follows the expanded ruleset to ensure every choice has two strengths and two weaknesses:

Winner	Action	Loser
Scissors	✌️ cuts	✋ Paper
Paper	✋ covers	✊ Rock
Rock	✊ crushes	🦎 Lizard
Lizard	🦎 poisons	🖖 Spock
Spock	🖖 smashes	✌️ Scissors
Scissors	✌️ decapitates	🦎 Lizard
Lizard	🦎 eats	✋ Paper
Paper	✋ disproves	🖖 Spock
Spock	🖖 vaporizes	✊ Rock
Rock	✊ crushes	✌️ Scissors

✨ Features

    Extended Logic: A more complex conditional system to handle 25 different outcome combinations.

    Terminal Colors: Powered by colorama for clear visual win/loss/tie feedback.

    Emoji Integration: Uses ✊, ✋, ✌️, 🦎, and 🖖 for a better UI experience.

    Randomized AI: A computer opponent that selects moves unpredictably.

🛠️ Installation & Usage

    Clone the repo:
    Bash

    git clone https://github.com/your-username/your-repo-name.git

    Install dependencies:
    Bash

    pip install colorama

    Run the game:
    Bash

    python main.py

💻 Technologies Used

    Python 3.x

    Colorama Library (for terminal styling)

    Random Module (for CPU move generation)