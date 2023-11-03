from pprint import pprint
from typing import List, Callable

from sympy import Symbol, factorial, limit, log, oo, sqrt


def check_limit_tendency(func1: Callable, func2: Callable, arg: float) -> bool:
    """
    Check if the limit of func1 divided by func2, with the argument arg, tends to a finite value.

    Args:
        func1: A function representing the numerator of the division.
        func2: A function representing the denominator of the division.
        arg: The argument to be passed to the limit function.

    Returns:
        A boolean value indicating whether the limit tends to a finite value.
    """
    return str(limit(func1 / func2, arg, oo)) == "oo"


def main(funcs: List[Callable], arg) -> List[Callable]:
    """
    Sorts the given list of functions based on their tendency to exceed a limit.

    Args:
    - funcs (List[Callable]): A list of functions to be sorted.
    - arg: The argument to be passed to the check_limit_tendency function.

    Returns:
    - List[Callable]: The sorted list of functions.
    """
    n = len(funcs)
    for j in range(n - 1):
        for i in range(n - j - 1):
            if check_limit_tendency(funcs[i], funcs[i + 1], arg):
                funcs[i], funcs[i + 1] = funcs[i + 1], funcs[i]
    return funcs


if __name__ == "__main__":
    n = Symbol("n")
    funcs = [
        sqrt(log(n, 4)),
        log(log(n, 2), 2),
        log(n, 3),
        sqrt(n),
        n / log(n, 5),
        log(n, 2) ** 2,
        log(factorial(n), 2),
        3 ** log(n, 2),
        n**2,
        4**n,
        2 ** (3 * n),
        factorial(n),
        2 ** (2**n),
        log(n, 2) ** log(n, 2),
        7 ** log(n, 2),
        n ** log(n, 2),
        n ** sqrt(n),
        2**n,
    ]
    pprint(main(funcs, n))
