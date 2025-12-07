def multiplicity_n(arg: int) -> bool:
    if not isinstance(arg, int):
        raise TypeError("[mathhunt] : [logic] : Input error! Arguments must be an integer")
    
    else:
        return arg >= 0


def multiplicity_z(arg: int) -> bool:
    if not isinstance(arg, int):
        raise TypeError("[mathhunt] : [logic] : Input error! Arguments must be an integer")
    
    return True


def multiplicity_q(arg: float) -> bool:
    if not isinstance(arg, float):
        raise TypeError("[mathhunt] : [logic] : Input error! Arguments must be a float")
    
    return True


def multiplicity_e(arg: float) -> bool:
    if not isinstance(arg, float):
        raise TypeError("[mathhunt] : [logic] : Input error! Arguments must be a float")
    
    return (arg % 2) == 0


def multiplicity_o(arg: float) -> bool:
    if not isinstance(arg, float):
        raise TypeError("[mathhunt] : [logic] : Input error! Arguments must be a float")
    
    return (arg % 2) != 0


def conjunction(arg: bool, kwarg: bool) -> bool:
    if not isinstance(arg, bool) or not isinstance(kwarg, bool):
        raise TypeError("[mathhunt] : [logic] : Input error! Arguments must be boolean")
    
    return arg and kwarg


def disjunction(arg: bool, kwarg: bool) -> bool:
    if not isinstance(arg, bool) or not isinstance(kwarg, bool):
        raise TypeError("[mathhunt] : [logic] : Input error! Arguments must be boolean")
    
    return arg or kwarg


def negation(arg: bool) -> bool:
    if not isinstance(arg, bool):
        raise TypeError("[mathhunt] : [logic] : Input error! Argument must be boolean")
    
    return not arg


def implication(arg: bool, kwarg: bool) -> bool:
    if not isinstance(arg, bool) or not isinstance(kwarg, bool):
        raise TypeError("[mathhunt] : [logic] : Input error! Arguments must be boolean")
    
    return not arg or kwarg


def equivalence(arg: bool, kwarg: bool) -> bool:
    if not isinstance(arg, bool) or not isinstance(kwarg, bool):
        raise TypeError("[mathhunt] : [logic] : Input error! Arguments must be boolean")
    
    return arg == kwarg