"""Contains a function to parse given arguments.
"""


__authors__ = ["Lucas ROUAUD"]
__contact__ = ["lucas.rouaud@gmail.com"]
__copyright__ = "MIT License"

# [I]
from importlib.util import module_from_spec, spec_from_file_location
# [O]
from os.path import exists, isdir
# [S]
from sys import modules
# [T]
from textwrap import dedent

# [A]
from argparse import ArgumentParser, RawTextHelpFormatter
# [Y]
from yaml import safe_load

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
    
    \033[7m [[subpackage USE]] \033[0m\n
    ./package/
    └── src/
        ├── __init__.py
        └── subpackage/
            ├── __init__.py
            └── script.py
    
    Note that packages are identify with "__init__.py" files and allow
    relatives import. To launch the function assessor on "script.py" do, if you
    are in ./package:
    
    \033[7m [[PACKAGE USE]] \033[0m\n
    $ python -m src.main \\
             -s src/subpackage/script.py \\
             -f function_name \\
             -o output_directory/ \\
             --package src/__init__.py \\
             --subpackage src/subpackage/__init__.py \\
             -a argument.yml
    
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
        metavar="[int|9]",
        help=("    > The number of field to keep in function name. By default "
              "9.")
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
        type=str,
        metavar="[FILE][\".yml\"]",
        help=("    > A YAML file containing all argument for the function to "
              "test. By default None.")
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
                         "not the extension \".py\".")

    # Input package errors.
    if argument.package is not None:
        if not exists(argument.package):
            raise FileNotFoundError("[Err##] In script, file "
                                    f"\"{argument.package}\" does not exist.")
        if not argument.package.endswith("__init__.py"):
            raise ValueError(f"[Err##] In script, file \"{argument.package}\" "
                             "have to be a \"__init__.py\" file.")

    # Input subpackage errors.
    if argument.subpackage is not None:
        if not exists(argument.subpackage):
            raise FileNotFoundError("[Err##] In script, file "
                                    f"\"{argument.subpackage}\" does not "
                                    "exist.")
        if not argument.subpackage.endswith("__script__.py"):
            raise ValueError("[Err##] In script, file "
                             f"\"{argument.subpackage}\" have to be a "
                             "\"__init__.py\" file.")

    # Input YAML errors.
    if argument.argument is not None:
        if not exists(argument.argument):
            raise FileNotFoundError("[Err##] In script, file "
                                    f"\"{argument.argument}\" does not "
                                    "exist.")
        if not argument.argument.endswith(".yml"):
            raise ValueError("[Err##] In script, file "
                             f"\"{argument.argument}\" have to be a "
                             "\".yml\" file.")

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

    if argument.n_field < 0:
        raise ValueError("[Err##] In n_filed, the value "
                         f"\"{argument.n_field}\" should be greater strictly "
                         "to 0.")

    # =============
    #
    # SIMPLE SCRIPT
    #
    # =============
    if argument.package is None and argument.subpackage is None:
        # Load the function inside the module.
        module_spec = spec_from_file_location(
            name=argument.function,
            location=argument.script
        )

        # "Prepare" the module.
        module = module_from_spec(spec=module_spec)

        # "Launch" the module inside the python environment.
        module_spec.loader.exec_module(module=module)
    # =======
    #
    # PACKAGE
    #
    # =======
    elif argument.package is not None and argument.subpackage is None:
        # Get the package name.
        package_name: str = argument.package.split("/")[-2]
        # Load the package.
        package_spec = spec_from_file_location(package_name, argument.package)

        # "Prepare" the package.
        package = module_from_spec(package_spec)
        # Add the package to the modules dict.
        modules[package_name] = package

        # "Launch" the package.
        package_spec.loader.exec_module(package)

        # Set the module name.
        module_name: list = []

        for item in argument.script[:-3].split("/")[::-1]:
            module_name += [item]

            if item == package_name:
                break

        module_name: str = ".".join(module_name[::-1])

        # Load the script inside the module.
        module_spec = spec_from_file_location(module_name, argument.script)

        # "Prepare" the script.
        module = module_from_spec(module_spec)
        # Add the script to the modules dict.
        modules[package_name + ".None"] = module

        # "Launch" the script.
        module_spec.loader.exec_module(module)
    # ==========
    #
    # SUBPACKAGE
    #
    # ==========
    elif argument.package is not None and argument.subpackage is not None:
        # Get the package name.
        package_name: str = argument.package.split("/")[-2]
        # Load the package.
        package_spec = spec_from_file_location(package_name, argument.package)

        # "Prepare" the package.
        package = module_from_spec(package_spec)
        # Add the package to the modules dict.
        modules[package_name] = package

        # "Launch" the package.
        package_spec.loader.exec_module(package)

        # Set the module name.
        module_name: list = []

        for item in argument.script[:-3].split("/")[::-1]:
            module_name += [item]

            if item == package_name:
                break

        module_name: str = ".".join(module_name[::-1])

        # Set the subpackage name.
        subpackage_name: list = []

        for item in argument.subpackage[:-3].split("/")[::-1]:
            subpackage_name += [item]

            if item == package_name:
                break

        subpackage_name: str = ".".join(subpackage_name[::-1])

        # Load the script inside the module.
        module_spec = spec_from_file_location(module_name, argument.script)

        # "Prepare" the script.
        module = module_from_spec(module_spec)
        # Add the script to the modules dict.
        modules[subpackage_name] = module

        # "Launch" the script.
        module_spec.loader.exec_module(module)
    else:
        raise ValueError("[Err##] If --subpackage is specified, --package "
                         "must be specified too.")

    # Check if the function exists inside the module/package/subpackage.
    try:
        argument.function = module.__dict__[argument.function]
    except KeyError as error:
        raise ValueError(f"[Err##] \"{argument.function}\" is not present "
                         "inside the given script "
                         "\"{argument.script}\".") from error

    # ====================
    #
    # PARSING THE YML FILE
    #
    # ====================
    if argument.argument is not None:
        # Parsing user file.
        with open(argument.argument, "r", encoding="utf-8") as file:
            argument.argument: dict = safe_load(file)

    return argument


if __name__ == "__main__":
    __argument: ArgumentParser = parse_argument()

    print(f"{__argument.function=}")
    print(f"{__argument.script=}")
    print(f"{__argument.output=}")
    print(f"{__argument.argument=}")
    print(f"{__argument.package=}")
    print(f"{__argument.subpackage=}")
