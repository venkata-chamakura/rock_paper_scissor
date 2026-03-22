from colorama import Fore
import random #using for random generation for CPU

print("===================\nRock Paper Scissors\n===================")

print("1) ✊ (Rock)\n2) ✋ (Paper)\n3) ✌️ (Scissors)") #showing the menu

player = int(input("\nPick a Number: "))  #player selects the number
cpu = random.randint(1,3)  #cpu random generation

print("") 
#shows_what_player_has_selected
if player == 1:
    print("You choose: ✊")
elif player == 2:
    print('You choose: ✋')
elif player == 3:
    print('You choose: ✌️')
else:
    print('You choose: Beyond Limit')

#shows_what_cpu_has_generated
if cpu == 1:
    print('CPU choose: ✊')
elif cpu == 2:
    print('CPU choose: ✋')
elif cpu == 3:
    print('CPU choose: ✌️')
print("")

#---------------
#game_logic
#---------------
if player == 1 and cpu == 1 or player == 2 and cpu == 2 or player == 3 and cpu == 3: #tie_logic
    print(Fore.MAGENTA,"Its a Tie!")
elif player == 1 and cpu == 3 or player == 2 and cpu == 1 or player == 3 and cpu == 2: #player_wins_logic
    print(Fore.GREEN,"The Player Won!")
elif player == 1 and cpu == 2 or player == 2 and cpu == 3 or player == 3 and cpu == 1: #cpu_wins_logic
    print(Fore.RED,'The CPU Won!')
else:
    print(Fore.YELLOW,"It's Beyond Limit")
