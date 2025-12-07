from typing import Tuple


def volume(*args: float, type: str) -> float:
    """
    Calculate the volume of various 3D shapes.

    Parameters:
        *args (float): Metrics for the shape (e.g., radius, height).
        type (str): Type of the shape (e.g., 'cube', 'sphere').

    Returns:
        float: Volume of the shape.

    Raises:
        TypeError: If the inputs are of incorrect types.
        ValueError: If the shape type is invalid, arguments are incorrect, or metrics are non-positive.
    """
    if not all(isinstance(arg, (int, float)) for arg in args):
        raise TypeError("[mathhunt] : [shapes] : Input error! All metrics must be numbers!")
    
    if not isinstance(type, str):
        raise TypeError("[mathhunt] : [shapes] : Input error! Type must be a string!")

    expected_args: dict[str, Tuple[int, str]] = {
        "parallelepiped": (3, "length, width, height"),
        "cube": (1, "side"),
        "cylinder": (2, "radius, height"),
        "sphere": (1, "radius"),
        "cone": (2, "radius, height"),
        "pyramid": (2, "base area, height"),
        "tetrahedron": (1, "edge length"),
        "octahedron": (1, "edge length"),
        "icosahedron": (1, "edge length")
    }

    if type not in expected_args:
        raise ValueError(f"[mathhunt] : [shapes] : Invalid type! Must be one of: {', '.join(expected_args)}")
    
    expected_arg_count, arg_names = expected_args[type]

    if len(args) != expected_arg_count:
        raise ValueError(f"[mathhunt] : [shapes] : {type.capitalize()} requires {expected_arg_count} argument(s): {arg_names}")

    if any(arg <= 0 for arg in args):
        raise ValueError("[mathhunt] : [shapes] : Metrics must be > 0!")

    if type == "parallelepiped":
        return args[0] * args[1] * args[2]
    if type == "cube":
        return args[0] ** 3
    if type == "cylinder":
        return 3.14 * (args[0] ** 2) * args[1]
    if type == "sphere":
        return (4.0 / 3.0) * 3.14 * (args[0] ** 3)
    if type == "cone":
        return (1.0 / 3.0) * 3.14 * (args[0] ** 2) * args[1]
    if type == "pyramid":
        return (1.0 / 3.0) * args[0] * args[1]
    if type == "tetrahedron":
        return (args[0] ** 3) / (6 * (2 ** 0.5))
    if type == "octahedron":
        return ((2 ** 0.5) / 3.0) * (args[0] ** 3)
    if type == "icosahedron":
        return ((5 * (3 + (5 ** 0.5))) / 12.0) * (args[0] ** 3)


def square(*args: float, type: str) -> float:
    """
    Calculate the area of various 2D shapes.

    Parameters:
        *args (float): Metrics for the shape (e.g., side lengths, radius).
        type (str): Type of the shape (e.g., 'quadrate', 'rectangle').

    Returns:
        float: Area of the shape.

    Raises:
        TypeError: If the inputs are of incorrect types.
        ValueError: If the shape type is invalid, arguments are incorrect, or metrics are non-positive.
    """
    if not all(isinstance(arg, (int, float)) for arg in args):
        raise TypeError("[mathhunt] : [shapes] : Input error! All metrics must be numbers!")
    
    if not isinstance(type, str):
        raise TypeError("[mathhunt] : [shapes] : Input error! Type must be a string!")
    
    expected_args: dict[str, Tuple[int, str]] = {
        "quadrate": (1, "side"),
        "rectangle": (2, "width, height"),
        "triangle_h": (2, "base, height"),
        "triangle_s": (3, "side a, side b, side c"),
        "circle": (1, "radius"),
        "trapezoid": (3, "base a, base b, height"),
        "rhombus": (2, "diagonal d1, diagonal d2"),
        "parallelogram": (2, "base, height"),
        "sector": (2, "angle deg, radius"),
        "ellipse": (2, "half-axis a, half-axis b"),
        "polygon": (3, "n - quantity of sides, radius of inscribed circle, length of side"),
        "sphere": (1, "radius")
    }

    if type not in expected_args:
        raise ValueError(f"[mathhunt] : [shapes] : Invalid type! Must be one of: {', '.join(expected_args)}")
    
    expected_arg_count, arg_names = expected_args[type]

    if len(args) != expected_arg_count:
        raise ValueError(f"[mathhunt] : [shapes] : {type.capitalize()} requires {expected_arg_count} argument(s): {arg_names}")

    if any(arg <= 0 for arg in args):
        raise ValueError("[mathhunt] : [shapes] : Metrics must be > 0!")
    
    if type == "quadrate":
        return args[0] ** 2
    if type == "rectangle":
        return args[0] * args[1]
    if type == "triangle_h":
        return args[0] * args[1] * 0.5
    if type == "triangle_s":
        s = (args[0] + args[1] + args[2]) / 2.0
        return (s * (s - args[0]) * (s - args[1]) * (s - args[2])) ** 0.5  # Using Heron's formula
    if type == "circle":
        return 3.14 * (args[0] ** 2)
    if type == "trapezoid":
        return 0.5 * (args[0] + args[1]) * args[2]
    if type == "rhombus":
        return (args[0] * args[1]) / 2.0
    if type == "parallelogram":
        return args[0] * args[1]
    if type == "sector":
        return (args[0] / 360.0) * (3.14 * (args[1] ** 2))
    if type == "ellipse":
        return 3.14 * args[0] * args[1]
    if type == "polygon":
        return 0.5 * args[0] * args[1] * args[2]
    if type == "sphere":
        return 4.0 * 3.14 * (args[0] ** 2)