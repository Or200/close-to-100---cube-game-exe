from game import *
from utils import *

def play_game():
    player1_score = 0
    player2_score = 0
    d_pass = 0
    while True:
        p1 = turn_decision(game_choice)
        if p1 == "r":
            d_pass = 0
            player1_round = sum(roll_two_d6())
            player1_score +=  player1_round
            print(f"Player 1: this roune cubes {player1_round} player 1 score is: {player1_score}")
            if is_exact_100(player1_score):
                print("player 1 Win !")
                break
            if is_bust(player1_score):
                print("player 2 Win !")
                break
            print(f"player {closer_to_target(player1_score, player2_score)} closer to target")
        elif p1 == "p":
            d_pass += 1
            if d_pass == 2:
                if player1_score == player2_score:
                    x = tie_breaker(roll_two_d6)
                    print(f"Player {x} Win !")
                    break
                else:
                    print(f"Player {closer_to_target()} Win !")
                



        p2 = turn_decision(game_choice)
        if p2 == "r":
            d_pass = 0
            player2_round = sum(roll_two_d6())
            player2_score +=  player2_round
            print(f"Player 2: this roune cubes {player2_round} player 2 score is: {player2_score}")
            if is_exact_100(player2_score):
                print("player 2 Win !")
                break
            if is_bust(player1_score):
                print("player 1 Win !")
                break
            print(f"player {closer_to_target(player1_score, player2_score)} closer to target")
        elif p2 == "p":
            d_pass += 1
            if d_pass == 2:
                if player1_score == player2_score:
                    x = tie_breaker(roll_two_d6)
                    print(f"Player {x} Win !")
                    break
                else:
                    print(f"Player {closer_to_target()} Win !")

                

                
        

play_game()