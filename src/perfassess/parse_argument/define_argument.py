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
    "Assess." is a program to assess the time execution of a given script in
    python. To use it, launch:

    \033[7m [[NORMAL USE]] \033[0m\n

        $ perfassess -s script.py \\
                     -f function_name \\
                     -o output_directory/ \\
                     -a argument.yml

    You can actually directly test the program in the repository root
    (perfassess/) using:

        $ perfassess -s src/perfassess/testor.py \\
                     -f testor \\
                     -a data/argument.yml \\
                     -o data/

    \033[7m [[PACKAGE USE]] \033[0m\n
    Let us say that you want to test a package, which should have this kind of
    tree structure:

        package/
        └── src/
            ├── __init__.py
            └── script.py

    In package, you can use relative paths. But with these, the "normal use"
    method do not work. Instead, use the next command, if you are in package/,
    in order to evaluate script.py:

        $ perfassess -s src/script.py \\
                     -f function_name \\
                     -o output_directory/ \\
                     --package src/__init__.py \\
                     -a argument.yml

    In addition of the previous "normal use" method, you have to indicate a
    __init__.py file.

    \033[7m [[SUBACKAGE USE]] \033[0m\n
    Let us say that you want to test a subpackage, which should have this kind
    of tree structure:

        ./package/
        └── src/
            ├── __init__.py
            └── subpackage/
                ├── __init__.py
                └── script.py

    In subpackage, you can use relative paths. But with these, the "normal use"
    method do not work. But the "package use" also do not work. Instead, use
    the next command, if you are in package/, in order to evaluate script.py:

        $ perfassess -s src/subpackage/script.py \\
                     -f function_name \\
                     -o output_directory/ \\
                     --package src/__init__.py \\
                     --subpackage src/subpackage/__init__.py \\
                     -a argument.yml

    In addition of the previous "normal use" and "package use" method, you have
    to indicate two __init__.py files. The first one is the top package
    __init__.py file. The second one is the __init__.py file of the subpackage
    to test.
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
        help="    > Display the program's version, then exit the\nprogram."
    )

    parser.add_argument(
        "-f",
        "--function",
        dest="function",
        required=False,
        default="main",
        type=str,
        metavar="[str|main]",
        help=("    > The entry point to assess a script. It have to be\nthe "
              "name of a function. By default, \"main\".")
    )

    parser.add_argument(
        "--n_field",
        dest="n_field",
        required=False,
        default=0,
        type=int,
        metavar="[int|0]",
        help=("    > The number of field to keep in function name. "
              "By\ndefault 0.")
    )

    parser.add_argument(
        "--package",
        dest="package",
        required=False,
        default=None,
        type=str,
        metavar="[FILE][\".py\"]",
        help="    > The path to an \"__init__.py\" package. By default\nNone."
    )

    parser.add_argument(
        "--subpackage",
        dest="subpackage",
        required=False,
        default=None,
        type=str,
        metavar="[FILE][\".py\"]",
        help=("    > The path to an \"__init__.py\" subpackage. By\ndefault "
              "None.")
    )

    parser.add_argument(
        "-a",
        "--argument",
        dest="argument",
        required=False,
        default=None,
        type=None,
        metavar="[FILE][\".yml\"]",
        help=("    > A YAML file containing all argument for the\nfunction to "
              "test. By default None.")
    )

    argument: ArgumentParser = parser.parse_args()

    return argument
