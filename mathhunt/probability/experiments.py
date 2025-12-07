from functions import *
import random as r

def roll(sides: int = 6) -> int:
    """
    Simulate rolling a die with a given number of sides.
    Arguments:
        sides: Number of sides on the die (default is 6).
    Returns:
        An integer representing the result of the die roll.
    """
    if not isinstance(sides, int) or sides < 1:
        raise ValueError("Number of sides must be a positive integer.")
    return r.randint(1, sides)

def flip() -> str:
    """
    Simulate flipping a coin.
    Returns:
        A string representing the result of the coin flip ("Heads" or "Tails").
    """
    return "Heads" if r.randint(0, 1) == 0 else "Tails"