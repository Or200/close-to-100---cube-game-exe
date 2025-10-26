import random

def roll_two_d6() -> tuple[int, int]:
    cube_1 = random.randint(1,6)
    cube_2 = random.randint(1,6)
    return cube_1, cube_2

def is_bust(score: int) -> bool:
    return score > 100

def is_exact_100(score: int) -> bool:
    return score == 100

def turn_decision(input_fn) -> str:
    while True:
        inn = input_fn()
        if inn == "r" or inn == "p":
            return inn
        print("Error")

def game_choice() -> str:
    my_input = input("pls input: ")
    return my_input
