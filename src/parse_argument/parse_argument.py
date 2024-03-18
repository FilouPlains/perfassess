"""Contains a function to parse given arguments.
"""


__authors__ = ["Lucas ROUAUD"]
__contact__ = ["lucas.rouaud@gmail.com"]
__copyright__ = "MIT License"


# [C]
from .check_argument import check_argument
# [D]
from .define_argument import define_argument


def parse_argument(version: str = None) -> object:
    """Parse given arguments and tests them.

    Parameters
    ----------
    version : `str`, optional
        The script version. By default None.

    Returns
    -------
    `ArgumentParser`
        The object with checked parsed arguments.
    """
    # Parse the arguments.
    argument = define_argument(version=version)
    # Test the arguments.
    argument = check_argument(argument)

    return argument


if __name__ == "__main__":
    __argument = parse_argument()

    print(f"{__argument.function=}")
    print(f"{__argument.script=}")
    print(f"{__argument.output=}")
    print(f"{__argument.argument=}")
    print(f"{__argument.package=}")
    print(f"{__argument.subpackage=}")
