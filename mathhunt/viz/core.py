import matplotlib.pyplot as plt

_ax = None

_color_index = 0

_hatches_index = 0

_edges_index = 0

_colors = [
    "lightblue",
    "lightgreen",
    "lightsalmon",
    "plum",
    "khaki",
    "orange",
    "lightcoral",
    "turquoise",
    "violet",
    "gold"
]

_hatches = [
    "//",
    "\\\\",
    "xx",
    "..",
    "oo",
    "--",
    "++",
    "**",
    "||",
    "///"
]

_edges = [
    "lightblue",
    "lightgreen",
    "lightsalmon",
    "plum",
    "khaki",
    "orange",
    "lightcoral",
    "turquoise",
    "violet",
    "gold"
]

def get_ax():
    """Return current axis or make new if it is needed."""
    global _ax
    if _ax is None:
        _, _ax = plt.subplots()
    return _ax

def get_next_color():
    """Return next color."""
    global _color_index
    color = _colors[_color_index % len(_colors)]
    _color_index += 1
    return color

def get_next_hatch():
    """Return next color."""
    global _hatches_index
    hatch = _hatches[_hatches_index % len(_hatches)]
    _hatches_index += 1
    return hatch

def get_next_edge():
    """Return next color."""
    global _edges_index
    edge = _edges[_edges_index % len(_edges)]
    _edges_index += 1
    return edge

def show():
    """Show all figures in a one coordinate system"""
    ax = get_ax()
    ax.set_aspect('equal', 'box')
    ax.legend()
    ax.grid(True, which='both')
    plt.show()
