from utils import *

def closer_to_target(a: int, b: int, target: int = 100) -> int | None:
    if target - a < target - b:
        return 1
    elif target - a > target - b:
        return 2
    else:
        return

def tie_breaker(roller) -> int:
    while True:
        player1 = sum(roller())   
        player2 = sum(roller())

        if player1 > player2:
            return 1
        if player1 < player2:
            return 2
        

def play_round(p1_score: int, p2_score: int):
    d_pass = 0
    while True:
        p1 = turn_decision(game_choice)
        if p1 == "r":
            d_pass = 0
            player1_round = sum(roll_two_d6())
            p1_score +=  player1_round
            print(f"Player 1: this roune cubes {player1_round} player 1 score is: {p1_score}")
            if is_exact_100(p1_score):
                print("player 1 Win !")
                break
            if is_bust(p1_score):
                print("player 2 Win !")
                break
            print(f"player {closer_to_target(p1_score, p2_score)} closer to target")
        elif p1 == "p":
            d_pass += 1
            if d_pass == 2:
                if p1_score == p2_score:
                    x = tie_breaker(roll_two_d6)
                    print(f"Player {x} Win !")
                    break
                else:
                    print(f"Player {closer_to_target()} Win !")
            else:
                pass

        p2 = turn_decision(game_choice)
        if p2 == "r":
            d_pass = 0
            player2_round = sum(roll_two_d6())
            p2_score +=  player2_round
            print(f"Player 2: this roune cubes {player2_round} player 2 score is: {p2_score}")
            if is_exact_100(p2_score):
                print("player 2 Win !")
                break
            if is_bust(p1_score):
                print("player 1 Win !")
                break
            print(f"player {closer_to_target(p1_score, p2_score)} closer to target")
        elif p2 == "p":
            d_pass += 1
            if d_pass == 2:
                if p1_score == p2_score:
                    x = tie_breaker(roll_two_d6)
                    print(f"Player {x} Win !")
                    break
                else:
                    print(f"Player {closer_to_target()} Win !")
            else:
                pass

