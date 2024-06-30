import random

def roll():
    max_number=6
    min_number=1    
    return random.randint(1,6)


while True:
    players = input("The number players(2,4) : ")
    if players.isdigit():
        players=int(players)
        if 2 <= players <=4:
            break
        else:
            print("Please Enter a value between 2 and 4")
    else:
        print("You are enterd a invalid input! Enter a valid input.")

max_score=50
scores =[0 for _ in range(players)]

for player_index in range(players):
    print("/nPlayer number "+ (player_index+1) + "turn has started!")
    print("Your total score is:",scores[player_index],"/n")
    current_score=0

    

