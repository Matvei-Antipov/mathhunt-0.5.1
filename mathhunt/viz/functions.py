import numpy as np
from typing import Tuple
from core import get_ax, get_next_color, get_next_hatch, get_next_edge
import matplotlib.pyplot as plt

def create_quadrate(*args: float, dimension: str):
    """
    Draw a quadrate (square).
    Arguments:
        args: One argument - side length.
        dimension: "2d" or "3d".
    """
    if not all(isinstance(arg, (int, float)) for arg in args):
        raise TypeError("[mathhunt] : [vizuals] : Input error! All metrics must be numbers!")
    
    if not isinstance(dimension, str):
        raise TypeError("[mathhunt] : [vizuals] : Input error! Type must be a string!")
    color = get_next_color()
    hatch = get_next_hatch()
    edge = get_next_edge()
    if dimension == "2d":
        ax = get_ax()
        half = args[0] / 2
        offset_text = args[0] * 0.1

        x = [-half, half, half, -half]
        y = [-half, -half, half, half]

        ax.fill(x + [x[0]], y + [y[0]], facecolor=color, edgecolor=edge, linewidth=2, hatch=hatch, label=f"Quadrate {args[0]}")

        for xi, yi in zip(x, y):
            if yi > 0:
                if xi < 0:
                    ax.text(xi - offset_text, yi + 0.5, f"({xi},{yi})", fontsize=10, ha='right', va='bottom')
                else:
                    ax.text(xi + offset_text, yi + 0.5, f"({xi},{yi})", fontsize=10, ha='left', va='bottom')
            else:
                if xi < 0:
                    ax.text(xi - offset_text, yi - 0.5, f"({xi},{yi})", fontsize=10, ha='right', va='top')
                else:
                    ax.text(xi + offset_text, yi - 0.5, f"({xi},{yi})", fontsize=10, ha='left', va='top')

        ax.set_xlim(-args[0], args[0])
        ax.set_ylim(-args[0], args[0])

    elif dimension == "3d":
        print("[mathhunt] : [vizuals] : 3D quadrates are not implemented yet.")
    else:
        raise ValueError("[mathhunt] : [vizuals] : Dimension must be '2d' or '3d'")


def create_rectangle(*args: float, dimension: str):
    """
    Draw a rectangle.
    Arguments:
        args: Two arguments - side lengths.
        dimension: "2d" or "3d".
    """
    if not all(isinstance(arg, (int, float)) for arg in args):
        raise TypeError("[mathhunt] : [vizuals] : Input error! All metrics must be numbers!")
    
    if not isinstance(dimension, str):
        raise TypeError("[mathhunt] : [vizuals] : Input error! Type must be a string!")
    color = get_next_color()
    hatch = get_next_hatch()
    edge = get_next_edge()
    if len(args) == 1:
        print("[mathhunt] : [vizuals] : Input hint! There must be 2 arguments! Your shape will be executed as quadrate!")
        create_quadrate(args[0], dimension=dimension)
        return

    if dimension == "2d":
        ax = get_ax()
        half_a = args[0] / 2
        half_b = args[1] / 2
        offset_text = args[1] * 0.1

        x = [-half_a, half_a, half_a, -half_a]
        y = [-half_b, -half_b, half_b, half_b]

        ax.fill(x + [x[0]], y + [y[0]], facecolor=color, edgecolor=edge, linewidth=2, hatch=hatch, label=f"Rectangle {args[0]}x{args[1]}")

        for xi, yi in zip(x, y):
            if yi > 0:
                if xi < 0:
                    ax.text(xi - offset_text, yi + 0.5, f"({xi},{yi})", fontsize=10, ha='right', va='bottom')
                else:
                    ax.text(xi + offset_text, yi + 0.5, f"({xi},{yi})", fontsize=10, ha='left', va='bottom')
            else:
                if xi < 0:
                    ax.text(xi - offset_text, yi - 0.5, f"({xi},{yi})", fontsize=10, ha='right', va='top')
                else:
                    ax.text(xi + offset_text, yi - 0.5, f"({xi},{yi})", fontsize=10, ha='left', va='top')

        ax.set_xlim(-args[0], args[0])
        ax.set_ylim(-args[1], args[1])

    elif dimension == "3d":
        print("[mathhunt] : [vizuals] : 3D rectangles are not implemented yet.")
    else:
        raise ValueError("[mathhunt] : [vizuals] : Dimension must be '2d' or '3d'")


def create_circle(*args: float, dimension: str):
    """
    Draw a circle.
    Arguments:
        args: One argument - radius.
        dimension: "2d" or "3d".
    """
    if not all(isinstance(arg, (int, float)) for arg in args):
        raise TypeError("[mathhunt] : [vizuals] : Input error! All metrics must be numbers!")
    
    if not isinstance(dimension, str):
        raise TypeError("[mathhunt] : [vizuals] : Input error! Type must be a string!")
    color = get_next_color()
    hatch = get_next_hatch()
    edge = get_next_edge()
    center = (0, 0)
    if dimension == "2d":
        ax = get_ax()
        radius = args[0]
        offset_text = radius * 0.1

        circle = plt.Circle((0, 0), radius, facecolor=color, edgecolor=edge, linewidth=2, hatch=hatch, label=f"Circle r={radius}")
        center = plt.Circle((0, 0), 0.1, color='black')
        radius_line = plt.Line2D((0, radius), (0, 0), color='red', linestyle='--')
        ax.add_artist(circle)
        ax.add_artist(radius_line)
        ax.add_artist(center)

        ax.text(0 + offset_text, 0 + offset_text, f"(0,0)", fontsize=10, ha='left', va='bottom')

        ax.set_xlim(-radius * 1.5, radius * 1.5)
        ax.set_ylim(-radius * 1.5, radius * 1.5)

    elif dimension == "3d":
        print("[mathhunt] : [vizuals] : 3D circles are not implemented yet.")
    else:
        raise ValueError("[mathhunt] : [vizuals] : Dimension must be '2d' or '3d'")
    
def create_triangle(*args: float, dimension: str):
    """
    Draw a triangle.
    Arguments:
        args: Three arguments - side lengths.
        dimension: "2d" or "3d".
    """
    if not all(isinstance(arg, (int, float)) for arg in args):
        raise TypeError("[mathhunt] : [vizuals] : Input error! All metrics must be numbers!")
    
    if not isinstance(dimension, str):
        raise TypeError("[mathhunt] : [vizuals] : Input error! Type must be a string!")
    
    if len(args) != 3:
        raise ValueError("[mathhunt] : [vizuals] : Input error! There must be exactly 3 side lengths for a triangle!")
    
    color = get_next_color()
    hatch = get_next_hatch()
    edge = get_next_edge()
    if dimension == "2d":
        ax = get_ax()
        a, b, c = args
        s = (a + b + c) / 2
        area = np.sqrt(s * (s - a) * (s - b) * (s - c))

        A = (0, 0)
        B = (c, 0)

        x_C = (a**2 - b**2 + c**2) / (2 * c)
        y_C = np.sqrt(a**2 - x_C**2)
        C = (x_C, y_C)

        x = [A[0], B[0], C[0]]
        y = [A[1], B[1], C[1]]

        ax.fill(x + [x[0]], y + [y[0]], facecolor=color, edgecolor=edge, linewidth=2, hatch=hatch, label=f"Triangle {a}x{b}x{c}")

        offset_text = max(a, b, c) * 0.1
        for xi, yi in zip(x, y):
            if yi > 0:
                if xi < x_C:
                    ax.text(xi - offset_text, yi + 0.5, f"({xi:.2f},{yi:.2f})", fontsize=10, ha='right', va='bottom')
                else:
                    ax.text(xi + offset_text, yi + 0.5, f"({xi:.2f},{yi:.2f})", fontsize=10, ha='left', va='bottom')
            else:
                if xi == 0:
                    ax.text(xi - offset_text, yi - 0.5, f"({xi},{yi})", fontsize=10, ha='right', va='top')
                else:
                    ax.text(xi + offset_text, yi - 0.5, f"({xi},{yi})", fontsize=10, ha='left', va='top')

        ax.set_xlim(-max(a, b, c), max(a, b, c))
        ax.set_ylim(-max(a, b, c), max(a, b, c))
    elif dimension == "3d":
        print("[mathhunt] : [vizuals] : 3D triangles are not implemented yet.")
    else:
        raise ValueError("[mathhunt] : [vizuals] : Dimension must be '2d' or '3d'")

def create_trapezoid(*args: float, dimension: str):
    """
    Draw a trapezoid.
    Arguments:
        args: Four arguments - side lengths.
        dimension: "2d" or "3d".
    """
    if not all(isinstance(arg, (int, float)) for arg in args):
        raise TypeError("[mathhunt] : [vizuals] : Input error! All metrics must be numbers!")
    
    if not isinstance(dimension, str):
        raise TypeError("[mathhunt] : [vizuals] : Input error! Type must be a string!")
    
    if len(args) != 4:
        raise ValueError("[mathhunt] : [vizuals] : Input error! There must be exactly 4 side lengths for a trapezoid!")

    AD, BC, AB, CD = args

    if dimension != "2d":
        raise ValueError("[mathhunt] : [vizuals] : 3D trapezoid cannot be drawn!")

    A = (0.0, 0.0)
    B = (AB, 0.0)

    xD = (AD**2 - BC**2 + AB**2) / (2 * AB)

    h_sq = AD**2 - xD**2
    if h_sq < 0:
        raise ValueError("[mathhunt] : [vizuals] : Such a trapezoid cannot exist with given sides!")

    yD = h_sq**0.5

    D = (xD, yD)

    C = (D[0] + CD, yD)

    ax = get_ax()

    color = get_next_color()
    ax.plot([A[0], B[0]], [A[1], B[1]], color=color)
    ax.plot([B[0], C[0]], [B[1], C[1]], color=color)
    ax.plot([C[0], D[0]], [C[1], D[1]], color=color)
    ax.plot([D[0], A[0]], [D[1], A[1]], color=color)

    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(min(A[0], D[0]) - 1, max(B[0], C[0]) + 1)
    ax.set_ylim(-1, yD + 1)   

    ax.fill([A[0], B[0], C[0], D[0], A[0]], [A[1], B[1], C[1], D[1], A[1]], facecolor=color, edgecolor='black', linewidth=2, hatch=get_next_hatch(), label=f"Trapezoid {AD}x{BC}x{AB}x{CD}") 
