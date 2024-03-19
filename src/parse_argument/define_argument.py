"""Contains a function to parse given arguments.
"""


__authors__ = ["Lucas ROUAUD"]
__contact__ = ["lucas.rouaud@gmail.com"]
__copyright__ = "MIT License"


# [T]
from textwrap import dedent

# [A]
from argparse import ArgumentParser, RawTextHelpFormatter


def define_argument(version: str = None) -> ArgumentParser:
    """Parse user given arguments.

    Parameters
    ----------
    version : `str`, optional
        The script version. By default None.

    Returns
    -------
    `ArgumentParser`
        The object with unchecked parsed arguments.
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

    \033[7m [[NORMAL USE]] \033[0m\n
    $ python -m src.main \\
             -s script.py \\
             -f function_name \\
             -o output_directory/ \\
             -a argument.yml

    Legend:
        - int: Integer.
        - [type|value]: Type of the input required, follow by the default
                        value. So if this optional arguments is not used,
                        "value" will be chosen.

    If you use this module to test another or, in another words, a package, the
    usage is a bit different. Let us says that you have a package following
    next schema:
    
    \033[7m [[SUBPACKAGE USE]] \033[0m\n
    ./package/
    └── src/
        ├── __init__.py
        └── subpackage/
            ├── __init__.py
            └── script.py
    
    Note that packages are identify with "__init__.py" files and allow
    relatives import. To launch the function assessor on "script.py" do, if you
    are in ./package:
    
    $ python -m src.main \\
             -s src/subpackage/script.py \\
             -f function_name \\
             -o output_directory/ \\
             --package src/__init__.py \\
             --subpackage src/subpackage/__init__.py \\
             -a argument.yml
    
    \033[7m [[PACKAGE USE]] \033[0m\n
    
    If you have no "subpackage", you do not need to provide anything for this
    parameter:
    
    ./package/
    └── src/
        ├── __init__.py
        └── script.py
    
    $ python -m src.main \\
             -s src/script.py \\
             -f function_name \\
             -o output_directory/ \\
             --package src/__init__.py \\
             -a argument.yml
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
        default=0,
        type=int,
        metavar="[int|0]",
        help=("    > The number of field to keep in function name. By default "
              "0.")
    )

    parser.add_argument(
        "--package",
        dest="package",
        required=False,
        default=None,
        type=str,
        metavar="[FILE][\".py\"]",
        help="    > The path to an \"__init__.py\" package. By default None."
    )

    parser.add_argument(
        "--subpackage",
        dest="subpackage",
        required=False,
        default=None,
        type=str,
        metavar="[FILE][\".py\"]",
        help="    > The path to an \"__init__.py\" subpackage. By default None."
    )

    parser.add_argument(
        "-a",
        "--argument",
        dest="argument",
        required=False,
        default=None,
        type=None,
        metavar="[FILE][\".yml\"]",
        help=("    > A YAML file containing all argument for the function to "
              "test. By default None.")
    )

    argument: ArgumentParser = parser.parse_args()

    return argument
