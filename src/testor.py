"""A simple function to test the module.
"""

__authors__ = ["Lucas ROUAUD"]
__contact__ = ["lucas.rouaud@gmail.com"]
__copyright__ = "MIT License"


def testor(value: list, to_add: int = 1):
    """A function to launch the program in order to test it.

    Parameters
    ----------
    value : `list`
        A list of values.
    to_add : `int`, optional
        An optional argument to test them. By default 1.
    """
    for value_i in value:
        to_add += value_i
