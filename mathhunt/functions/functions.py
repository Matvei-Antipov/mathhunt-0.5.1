import json
import os


def _load_bradys_table(filename='__data\\bradis_table.json'):

    if __name__ != 'mathhunt.functions.functions':
        raise ImportError("This function cannot be imported outside this module")

    filepath = os.path.join(os.path.dirname(__file__), '../', filename)
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data


def linear_function(a: float, x: float, b: float) -> float:
    """
    Calculate the value of a linear function.

    Args:
        a (float): The coefficient of x.
        x (float): The variable input.
        b (float): The constant term.

    Raises:
        TypeError: If any of the arguments are not numbers (int or float).

    Returns:
        float: The result of the linear function ax + b.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(x, (int, float)):
        raise TypeError("[mathhunt] : [functions] : Input error! Arguments must be numbers (int or float)")
    
    return (a * x) + b


def quadratic_function(a: float, x: float, b: float, c: float) -> float:
    """
    Calculate the value of a quadratic function.

    Args:
        a (float): The coefficient of x^2.
        x (float): The variable input.
        b (float): The coefficient of x.
        c (float): The constant term.

    Raises:
        TypeError: If any of the arguments are not numbers (int or float).
        ValueError: If the coefficient 'a' is 0, as this would make it a linear function.

    Returns:
        float: The result of the quadratic function ax^2 + bx + c.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)) or not isinstance(x, (int, float)):
        raise TypeError("[mathhunt] : [functions] : Input error! Arguments must be numbers (int or float)")
    
    if a == 0:
        raise ValueError("[mathhunt] : [functions] : If A is 0 that's a linear function")
    
    return (a * (x ** 2)) + (b * x) + c


def power_function(x: float, n: float) -> float:
    """
    Calculate the power of a number.

    Args:
        x (float): The base number.
        n (float): The exponent.

    Raises:
        TypeError: If any of the arguments are not numbers (int or float).

    Returns:
        float: The result of x raised to the power of n (x^n).
    """
    if not isinstance(x, (int, float)) or not isinstance(n, (int, float)):
        raise TypeError("[mathhunt] : [functions] : Input error! Arguments must be numbers (int or float)")
    
    return x ** n


def root_function(x: float, n: float) -> float:
    """
    Calculate the nth root of a number.

    Args:
        x (float): The number to find the root of.
        n (float): The degree of the root.

    Raises:
        TypeError: If any of the arguments are not numbers (int or float).
        ValueError: If x is negative, as the result would be NaN.

    Returns:
        float: The nth root of x (x^(1/n)).
    """
    if not isinstance(x, (int, float)) or not isinstance(n, (int, float)):
        raise TypeError("[mathhunt] : [functions] : Input error! Arguments must be numbers (int or float)")
    
    if x < 0:
        raise ValueError("[mathhunt] : [functions] : Input error! Result is NaN")

    return x ** (1 / n)

   
def pointer_function(x: float, a: float) -> float:
    """
    Calculate a raised to the power of x.

    Args:
        x (float): The exponent.
        a (float): The base number.

    Raises:
        TypeError: If any of the arguments are not numbers (int or float).
        ValueError: If a is equal to 0, as the function is unstable.

    Returns:
        float: The result of a raised to the power of x (a^x).
    """
    if not isinstance(x, (int, float)) or not isinstance(a, (int, float)):
        raise TypeError("[mathhunt] : [functions] : Input error! Arguments must be numbers (int or float)")
    
    if a == 0:
        raise ValueError("[mathhunt] : [functions] : Input error! Function is unstable, a must not be equal to 0")
    
    return a ** x

   
def logarithm_function(a: float, x: float) -> float:
    """
    Calculate the logarithm of x with base a.

    Args:
        a (float): The base of the logarithm.
        x (float): The argument of the logarithm.

    Raises:
        TypeError: If any of the arguments are not numbers (int or float).
        ValueError: If a is less than or equal to 0, a is equal to 1, or x is less than or equal to 0.

    Returns:
        float: The logarithm of x to the base a.
    """
    if not isinstance(x, (int, float)) or not isinstance(a, (int, float)):
        raise TypeError("[mathhunt] : [functions] : Input error! Arguments must be numbers (int or float)")
    
    if a <= 0 or a == 1:
        raise ValueError("[mathhunt] : [functions] : Base 'a' must be greater than 0 and not equal to 1")
    
    if x <= 0:
        raise ValueError("[mathhunt] : [functions] : Argument 'x' must be greater than 0")
    
    if x == 1:
        return 0.0
    
    if x == a:
        return 1.0

    log_value = 0.0
    current_value = 1.0

    while current_value < x:
        current_value *= a
        log_value += 1

    if current_value > x:
        while current_value > x:
            current_value /= a
            log_value -= 1

    return log_value


def absolut_function(x: float) -> float:
    """
    Calculate the absolute value of x.

    Args:
        x (float): The input number.

    Raises:
        TypeError: If the argument is not a number (int or float).

    Returns:
        float: The absolute value of x.
    """
    if not isinstance(x, float):
        raise TypeError("[mathhunt] : [functions] : Input error! Arguments must be numbers (int or float)")

    if x < 0:
        return -x
    return x


def sinus(x: float, type: str) -> float:
    """
    Calculate the sine of an angle given in degrees or radians using Bradis table.

    Args:
        x (float): The angle to calculate the sine for.
        type (str): The type of the angle, either "deg" for degrees or "rad" for radians.

    Raises:
        TypeError: If x is not a number or type is not a string.
        ValueError: If x is outside the valid range for the specified type or not found in the Bradis table.

    Returns:
        float: The sine of the angle.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("[mathhunt] : [functions] : Input error! Arguments must be an integer or float")
    if not isinstance(type, str):
        raise TypeError("[mathhunt] : [functions] : Input error! Type must be a string")

    if type == "deg" and not (-360 <= x <= 360):
        raise ValueError("[mathhunt] : [functions] : Angle in degrees must be in the range [-360, 360]")
    if type == "rad" and not (-6.2832 <= x <= 6.2832):
        raise ValueError("[mathhunt] : [functions] : Angle in radians must be in the range [-2π, 2π]")

    table = _load_bradys_table()
    angles = table.get("angles", {})

    if type == "rad":
        for value in angles.values():
            if abs(value['radian'] - x) < 1e-4:
                return value['sin']
    elif type == "deg":
        key = str(int(x))
        if key in angles:
            return angles[key]['sin']
    raise ValueError(f"[mathhunt] : [functions] : Angle {x} not found in Bradis table")


def cosinus(x: float, type: str) -> float:
    """
    Calculate the cosine of an angle given in degrees or radians using Bradis table.

    Args:
        x (float): The angle to calculate the cosine for.
        type (str): The type of the angle, either "deg" for degrees or "rad" for radians.

    Raises:
        TypeError: If x is not a number or type is not a string.
        ValueError: If x is outside the valid range for the specified type or not found in the Bradis table.

    Returns:
        float: The cosine of the angle.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("[mathhunt] : [functions] : Input error! Arguments must be an integer or float")
    if not isinstance(type, str):
        raise TypeError("[mathhunt] : [functions] : Input error! Type must be a string")

    if type == "deg" and not (-360 <= x <= 360):
        raise ValueError("[mathhunt] : [functions] : Angle in degrees must be in the range [-360, 360]")
    if type == "rad" and not (-6.2832 <= x <= 6.2832):
        raise ValueError("[mathhunt] : [functions] : Angle in radians must be in the range [-2π, 2π]")

    table = _load_bradys_table()
    angles = table.get("angles", {})

    if type == "rad":
        for value in angles.values():
            if abs(value['radian'] - x) < 1e-4:
                return value['cos']
    elif type == "deg":
        key = str(int(x))
        if key in angles:
            return angles[key]['cos']
    raise ValueError(f"[mathhunt] : [functions] : Angle {x} not found in Bradis table")


def tangens(x: float, type: str) -> float:
    """
    Calculate the tangent of an angle given in degrees or radians using Bradis table.

    Args:
        x (float): The angle to calculate the tangent for.
        type (str): The type of the angle, either "deg" for degrees or "rad" for radians.

    Raises:
        TypeError: If x is not a number or type is not a string.
        ValueError: If x is outside the valid range for the specified type or not found in the Bradis table.

    Returns:
        float: The tangent of the angle.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("[mathhunt] : [functions] : Input error! Arguments must be an integer or float")
    if not isinstance(type, str):
        raise TypeError("[mathhunt] : [functions] : Input error! Type must be a string")

    if type == "deg" and not (-360 <= x <= 360):
        raise ValueError("[mathhunt] : [functions] : Angle in degrees must be in the range [-360, 360]")
    if type == "rad" and not (-6.2832 <= x <= 6.2832):
        raise ValueError("[mathhunt] : [functions] : Angle in radians must be in the range [-2π, 2π]")

    table = _load_bradys_table()
    angles = table.get("angles", {})

    if type == "rad":
        for value in angles.values():
            if abs(value['radian'] - x) < 1e-4:
                return value['tan']
    elif type == "deg":
        key = str(int(x))
        if key in angles:
            return angles[key]['tan']
    raise ValueError(f"[mathhunt] : [functions] : Angle {x} not found in Bradis table")


def cotangens(x: float, type: str) -> float:
    """
    Calculate the cotangent of an angle given in degrees or radians using Bradis table.

    Args:
        x (float): The angle to calculate the cotangent for.
        type (str): The type of the angle, either "deg" for degrees or "rad" for radians.

    Raises:
        TypeError: If x is not a number or type is not a string.
        ValueError: If x is outside the valid range for the specified type or not found in the Bradis table.

    Returns:
        float: The cotangent of the angle.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("[mathhunt] : [functions] : Input error! Arguments must be an integer or float")
    if not isinstance(type, str):
        raise TypeError("[mathhunt] : [functions] : Input error! Type must be a string")

    if type == "deg" and not (-360 <= x <= 360):
        raise ValueError("[mathhunt] : [functions] : Angle in degrees must be in the range [-360, 360]")
    if type == "rad" and not (-6.2832 <= x <= 6.2832):
        raise ValueError("[mathhunt] : [functions] : Angle in radians must be in the range [-2π, 2π]")

    table = _load_bradys_table()
    angles = table.get("angles", {})

    if type == "rad":
        for value in angles.values():
            if abs(value['radian'] - x) < 1e-4:
                return 1 / value['tan']
    elif type == "deg":
        key = str(int(x))
        if key in angles:
            return 1 / angles[key]['tan']
    raise ValueError(f"[mathhunt] : [functions] : Angle {x} not found in Bradis table")


def arcsin(x: float) -> float:
    if not isinstance(x, (int, float)):
        raise TypeError("[mathhunt] : [functions] : Input error! Arguments must be an integer or float")

    table = _load_bradys_table()
    angles = table.get("angles", {})
    for key, value in angles.items():
        if value.get("sin") == x:
            return float(key)
    raise ValueError(f"[mathhunt] : [functions] : arcsin({x}) not found in Bradis table")


def arccos(x: float) -> float:
    if not isinstance(x, (int, float)):
        raise TypeError("[mathhunt] : [functions] : Input error! Arguments must be an integer or float")

    table = _load_bradys_table()
    angles = table.get("angles", {})
    for key, value in angles.items():
        if value.get("cos") == x:
            return float(key)
    raise ValueError(f"[mathhunt] : [functions] : arccos({x}) not found in Bradis table")


def arctan(x: float) -> float:
    if not isinstance(x, (int, float)):
        raise TypeError("[mathhunt] : [functions] : Input error! Arguments must be an integer or float")

    table = _load_bradys_table()
    angles = table.get("angles", {})
    for key, value in angles.items():
        if value.get("tan") == x:
            return float(key)
    raise ValueError(f"[mathhunt] : [functions] : arctan({x}) not found in Bradis table")


def arccot(x: float) -> float:
    if not isinstance(x, (int, float)):
        raise TypeError("[mathhunt] : [functions] : Input error! Arguments must be an integer or float")

    table = _load_bradys_table()
    angles = table.get("angles", {})
    for key, value in angles.items():
        if value.get("tan") == 1 / x:
            return float(key)
    raise ValueError(f"[mathhunt] : [functions] : arccot({x}) not found in Bradis table")


def exponential_function(x: float) -> float:
    if not isinstance(x, float):
        raise TypeError("[mathhunt] : [functions] : Input error! Arguments must be a number")
    return 2.71828 ** x


def sinh(x: float) -> float:
    if not isinstance(x, (int, float)):
        raise TypeError("[mathhunt] : [functions] : Input error! Arguments must be a number")
    return ((2.71828 ** x) - (2.71828 ** -(x))) / 2


def cosh(x: float) -> float:
    if not isinstance(x, (int, float)):
        raise TypeError("[mathhunt] : [functions] : Input error! Arguments must be a number")
    return ((2.71828 ** x) + (2.71828 ** -(x))) / 2


def tanh(x: float) -> float:
    if not isinstance(x, (int, float)):
        raise TypeError("[mathhunt] : [functions] : Input error! Arguments must be a number")
    return ((2.71828 ** x) - (2.71828 ** -(x))) / ((2.71828 ** x) + (2.71828 ** -(x)))


def coth(x: float) -> float:
    if not isinstance(x, (int, float)):
        raise TypeError("[mathhunt] : [functions] : Input error! Arguments must be a number")
    return ((2.71828 ** x) + (2.71828 ** -(x))) / ((2.71828 ** x) - (2.71828 ** -(x)))


def sigma(i: int, n: int, equation: float = 0.0) -> float:
    """
    Calculate the sum of integers from i to n, starting with an initial equation value.

    Parameters:
    i (int): Starting index.
    n (int): Ending index (inclusive).
    equation (float): Initial value to start the sum. Default is 0.0.

    Returns:
    float: The total sum.
    """
    if not all(isinstance(arg, int) for arg in (i, n)) or not isinstance(equation, (int, float)):
        raise TypeError("[mathhunt] : [functions] : Input error! Arguments must be numbers.")
    
    if n < i:
        raise ValueError("[mathhunt] : [functions] : Ending index (n) must be greater than or equal to starting index (i).")

    total_sum = equation

    for j in range(i, n + 1):
        total_sum += j

    return total_sum


def sigma_p(i: int, n: int, equation: float = 1.0) -> float:
    """
    Calculate the product of integers from i to n, starting with an initial equation value.

    Parameters:
    i (int): Starting index.
    n (int): Ending index (inclusive).
    equation (float): Initial value to start the product. Default is 1.0.

    Returns:
    float: The total product.
    """
    if not all(isinstance(arg, int) for arg in (i, n)) or not isinstance(equation, (int, float)):
        raise TypeError("[mathhunt] : [functions] : Input error! Arguments must be numbers.")
    
    if n < i:
        raise ValueError("[mathhunt] : [functions] : Ending index (n) must be greater than or equal to starting index (i).")

    total_product = equation

    for j in range(i, n + 1):
        total_product *= j

    return total_product