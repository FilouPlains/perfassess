"""Contains a function to parse given arguments.
"""


__authors__ = ["Lucas ROUAUD"]
__contact__ = ["lucas.rouaud@gmail.com"]
__copyright__ = "MIT License"

# [I]
from importlib.util import module_from_spec, spec_from_file_location
# [O]
from os.path import exists, isdir
# [T]
from textwrap import dedent

# [A]
from argparse import ArgumentParser, RawTextHelpFormatter


def parse_argument(version: str = None) -> ArgumentParser:
    """Parse given arguments and tests them.

    Parameters
    ----------
    version : `str`, optional
        The script version. By default None.

    Returns
    -------
    `ArgumentParser`
        The object with parsed arguments.

    Raises
    ------
    FileNotFoundError
        When a file or a directory given in argument does not exist, throw an
        error.
    ValueError
        When a file have a wrong extension or is a not directory, throw an
        error.
    """
    logo: str = """
                ▄▀▀█▄   ▄▀▀▀▀▄  ▄▀▀▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▀▀▄  ▄▀▀▀▀▄
               ▐ ▄▀ ▀▄ █ █   ▐ █ █   ▐ ▐  ▄▀   ▐ █ █   ▐ █ █   ▐
                 █▄▄▄█    ▀▄      ▀▄     █▄▄▄▄▄     ▀▄      ▀▄  
                ▄▀   █ ▀▄   █  ▀▄   █    █    ▌  ▀▄   █  ▀▄   █ 
               █   ▄▀   █▀▀▀    █▀▀▀    ▄▀▄▄▄▄    █▀▀▀    █▀▀▀ ▄
               ▐   ▐    ▐       ▐       █    ▐    ▐       ▐     
                                        ▐                        
                     _____________________________________
                    |""|""|""|""|""|""|""|""|""|""|""|""|"|
                    |  1  2  3  4  5  6  7  8  9 10 11 12 |
                    '-------------------------------------'
    """

    print(logo[1:])

    # Description of the program given when the help is cast.
    description: str = """
    Assess. is a program to assess the time execution of a given script in
    python. To use it, launch:

    $ python -m src.main -s script.py -f function_name -o output_directory/

    Legend:
        - int: Integer.
        - [type|value]: Type of the input required, follow by the default
                        value. So if this optional arguments is not used,
                        "value" will be chosen.

    If you use this module to test another or, in another words, a package, the
    usage is a bit different. Let us says that you have a package following
    next schema:
    
    ./package/
    └── src/
        ├── __init__.py
        └── sub_package/
            ├── __init__.py
            └── script.py
    
    Note that packages are identify with "__init__.py" files and allow
    relatives import. To launch the function assessor on "script.py" do, if you
    are in ./package:
    
    $ python -m src.main \\
             -s src/sub_package/script.py \\
             -f function_name \\
             -o output_directory/ \\
             --package src/__init__.py \\
             --sub_package src/sub_package/__init__.py
    
    If you have no "sub_package", you do not need to provide anything for this
    parameter:
    
    ./package/
    └── src/
        ├── __init__.py
        └── script.py
    
    $ python -m src.main \\
             -s src/script.py \\
             -f function_name \\
             -o output_directory/ \\
             --package src/__init__.py
    """

    # ===================
    #
    # ADD ARGUMENT PARSER
    #
    # ===================

    # Setup the arguments parser object.
    parser: object = ArgumentParser(
        description=dedent(description)[1:-1],
        formatter_class=RawTextHelpFormatter,
        add_help=False
    )

    # == REQUIRED.
    parser.add_argument(
        "-s",
        "--script",
        dest="script",
        required=True,
        type=str,
        metavar="[FILE][\".py\"]",
        help=("\033[7m [[MANDATORY]] \033[0m\n    > The \"scrit.py\" file to "
              "assess.")
    )

    parser.add_argument(
        "-o",
        "--output",
        dest="output",
        required=True,
        type=str,
        metavar="[DIRECTORY]",
        help=("\033[7m [[MANDATORY]] \033[0m\n    > A folder where the "
              "plots will be stored.")
    )

    # == OPTIONAL.
    parser.add_argument(
        "-h",
        "--help",
        action="help",
        help="    > Display this help message, then exit the program."
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"Program version is {version}",
        help="    > Display the program's version, then exit the program."
    )

    parser.add_argument(
        "-f",
        "--function",
        dest="function",
        required=False,
        default="main",
        type=str,
        metavar="[str|main]",
        help=("    > The entry point to assess a script. It have to be the "
              "name of a function. By default, \"main\"")
    )

    parser.add_argument(
        "--n_field",
        dest="n_field",
        required=False,
        default=9,
        type=int,
        metavar="[int|9]",
        help=("    > The number of field to keep in function name. By default "
              "9.")
    )

    parser.add_argument(
        "--package",
        dest="package",
        required=False,
        default=None,
        type=int,
        metavar="[FILE][\".py\"]",
        help="    > The path to an \"__init__.py\" package. By default None."
    )

    parser.add_argument(
        "--sub_package",
        dest="sub_package",
        required=False,
        default=None,
        type=int,
        metavar="[FILE][\".py\"]",
        help="    > The path to an \"__init__.py\" subpackage. By default None."
    )

    argument: ArgumentParser = parser.parse_args()

    # ============
    #
    # CHECK ERRORS
    #
    # ============

    # Input script errors.
    if not exists(argument.script):
        raise FileNotFoundError(f"[Err##] In script, file \"{argument.script}\" "
                                "does not exist.")
    if not argument.script.endswith(".py"):
        raise ValueError(f"[Err##] In script, file \"{argument.script}\" have "
                         "not the extension \".pdb\".")

    # Deleting potential "/" at directory end.
    if argument.output[-1] == "/":
        argument.output = argument.output[:-1]

    # Output errors.
    if not exists(argument.output):
        raise FileNotFoundError("[Err##] In output, directory "
                                f"\"{argument.output}\" does not exist.")
    if not isdir(argument.output):
        raise ValueError("[Err##] In output, the given path is not a "
                         "directory.")

    if argument.n_field < 1:
        raise ValueError("[Err##] In n_filed, the value "
                         f"\"{argument.n_field}\" should be greater or equal "
                         "to 0.")

    if argument.package is None and argument.sub_package is None:

    # import sys
    # import os
    # # Get the current script's directory
    # current_dir = os.path.dirname(os.path.abspath(argument.script))# Get the parent directory by going one level up
    # parent_dir = os.path.dirname(current_dir)# Add the parent directory to sys.path
    # sys.path.append(parent_dir)
    # sys.path.append(os.path.dirname(parent_dir))
    # sys.path.append(current_dir)
    # print(sys.path)

        module_spec = spec_from_file_location(
            name=argument.function,
            location=argument.script
        )

        module = module_from_spec(spec=module_spec)
        module_spec.loader.exec_module(module=module)

    # for i in module.__dict__.keys():
    #     print(i, "\t", module.__dict__[i], "\n\n")

    import importlib.util
    import sys
    spec_1 = importlib.util.spec_from_file_location(
        "phi_khi_propride", "/home/rouaud/Documents/performance_assessor/../phi_khi_propride/phi_khi_propride/__init__.py")
    foo_1 = importlib.util.module_from_spec(spec_1)
    sys.modules["phi_khi_propride"] = foo_1
    print(foo_1.__dict__)
    spec_1.loader.exec_module(foo_1)

    # ../phi_khi_propride/phi_khi_propride/grid/property_strategy/class_pi_stacking.py
    spec = importlib.util.spec_from_file_location(
        "phi_khi_propride.grid.property_strategy.class_pi_stacking", argument.script)
    foo = importlib.util.module_from_spec(spec)
    sys.modules["phi_khi_propride.grid.toto"] = foo
    print(foo.__dict__)
    spec.loader.exec_module(foo)
    foo.StrategyPiStacking()

    exit()

    try:
        argument.function = module.__dict__[argument.function]
    except KeyError as error:
        raise ValueError(f"[Err##] \"{argument.function}\" is not present "
                         "inside the given script "
                         "\"{argument.script}\".") from error

    return argument


if __name__ == "__main__":

    __argument: ArgumentParser = parse_argument()

    print(f"{__argument.function=}")
    print(f"{__argument.script=}")
    print(f"{__argument.output=}")
