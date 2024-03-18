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

# [Y]
from yaml import safe_load


def check_argument(argument: object) -> object:
    """Check if the different given arguments are good or not.

    Parameters
    ----------
    argument : `ArgumentParser`
        The parsed arguments to checked.

    Returns
    -------
    `ArgumentParser`
        The modified and corrected parsed arguments.
    """
    # Check errors linked to given files.
    __file_errors(argument=argument)
    # Check errors linked to module importations.
    argument = __module_importation_error(argument=argument)

    # Parse the ".yml" file.
    if argument.argument is not None:
        # Parsing user file.
        with open(argument.argument, "r", encoding="utf-8") as file:
            argument.argument = safe_load(file)
    else:
        argument.argument = {}

    return argument

# pylint: disable=too-many-branches
# We have to check if different parameters are good or not. Implying a lot of
# branches.
def __file_errors(argument: object):
    """Check errors linked to given files.

    Parameters
    ----------
    argument : `ArgumentParser`
        The parsed argument to check.

    Raises
    ------
    `FileNotFoundError`
        If the script file is not found.
    `ValueError`
        If the script file have not a ".py" extension.
    `FileNotFoundError`
        If the package file is not found.
    `ValueError`
        If the package file is not a "__init__.py" one.
    `FileNotFoundError`
        If the subpackage file is not found.
    `ValueError`
        If the package file is not a "__init__.py" one.
    `ValueError`
        If the package file is not a "__init__.py" one.
    `FileNotFoundError`
        If the YAML file is not found.
    `ValueError`
        If the YAML file have not a ".yml" extension.
    `FileNotFoundError`
        If the directory is not found.
    `ValueError`
        If the path given is not a directory.
    `ValueError`
        If a number of negative file is given.
    """
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

# pylint: enable=too-many-branches


def __module_importation_error(argument: object) -> object:
    """Try to import the given file in a module and do some modifications.

    Parameters
    ----------
    argument : `ArgumentParser`
        The parsed argument to check.

    Returns
    -------
    `ArgumentParser`
        The modified and corrected parsed arguments.

    Raises
    ------
    `ValueError`
        If subpackage is filled, package must be given too.
    `ValueError`
        The given function name is not found in the given module.
    """
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
                         f"\"{argument.script}\".") from error

    return argument
