import math

def fact(n: float, type: str) -> float:
    """
    Calculate the factorial of a non-negative integer n.
    Arguments:
        n: A non-negative integer.
    """
    if not isinstance(n, float):
        raise TypeError("[mathhunt] : [probability] : Input error! Argument must be an integer!")
    if n < 0:
        raise ValueError("[mathhunt] : [probability] : Input error! Argument must be a non-negative integer!")
    if not type:
        raise ValueError("[mathhunt] : [probability] : Input error! Type is not recieved for this function!")
    if not isinstance(type, str):
        raise TypeError("[mathhunt] : [probability] : Input error! Type must be a string!")
    
    if isinstance(n, float) and not n.is_integer():
        return math.gamma(n + 1)

    if n == 0 or n == 1:
        return 1.0
    
    if type == "recursive":
        return n * fact(n - 1, type="recursive")
    else:
        result = 1.0

        for i in range(2, int(n) + 1):
            result *= i
    
    return float(result)

def P_n(n: float) -> int:
    """
    Calculate the number of permutations of n elements.
    Arguments:
        n: A non-negative float.
    """
    if not isinstance(n, float):
        raise TypeError("[mathhunt] : [probability] : Input error! Argument must be an integer!")
    if n < 0:
        raise ValueError("[mathhunt] : [probability] : Input error! Argument must be a non-negative integer!")
    
    return int(fact(n, type="iterative"))

def A_n_k(n: float, k: float) -> int:
    """
    Calculate the number of arrangements of n elements taken k at a time.
    Arguments:
        n: A non-negative float.
        k: A non-negative float less than or equal to n.
    """
    if not isinstance(n, float) or not isinstance(k, float):
        raise TypeError("[mathhunt] : [probability] : Input error! Arguments must be integers!")
    if n < 0 or k < 0:
        raise ValueError("[mathhunt] : [probability] : Input error! Arguments must be non-negative integers!")
    if k > n:
        raise ValueError("[mathhunt] : [probability] : Input error! k must be less than or equal to n!")
    
    return int(fact(n, type="iterative") / fact(n - k, type="iterative"))

def C_n_k(n: float, k: float) -> int:
    """
    Calculate the number of combinations of n elements taken k at a time.
    Arguments:
        n: A non-negative float.
        k: A non-negative float less than or equal to n.
    """
    if not isinstance(n, float) or not isinstance(k, float):
        raise TypeError("[mathhunt] : [probability] : Input error! Arguments must be integers!")
    if n < 0 or k < 0:
        raise ValueError("[mathhunt] : [probability] : Input error! Arguments must be non-negative integers!")
    if k > n:
        raise ValueError("[mathhunt] : [probability] : Input error! k must be less than or equal to n!")
    
    return int(fact(n, type="iterative") / (fact(k, type="iterative") * fact(n - k, type="iterative")))

def P(event_outcomes: float, total_outcomes: float) -> float:
    """
    Calculate the probability of an event.
    Arguments:
        event_outcomes: Number of favorable outcomes for the event.
        total_outcomes: Total number of possible outcomes.
    """
    if not isinstance(event_outcomes, float) or not isinstance(total_outcomes, float):
        raise TypeError("[mathhunt] : [probability] : Input error! Arguments must be floats!")
    if event_outcomes < 0 or total_outcomes <= 0:
        raise ValueError("[mathhunt] : [probability] : Input error! Outcomes must be non-negative and total outcomes must be positive!")
    if event_outcomes > total_outcomes:
        raise ValueError("[mathhunt] : [probability] : Input error! Event outcomes cannot exceed total outcomes!")
    
    return event_outcomes / total_outcomes