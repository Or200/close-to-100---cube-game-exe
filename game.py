
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
        



