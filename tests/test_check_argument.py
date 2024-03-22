r"""Test if "src/perfassess/parse_argument/check_argument.py" is functional.

Usage
-----
When you are in the main directory ("performance_assessor/"), you can launch:

```sh
    # Execute this command line in a conda environment.
    $ pytest
```
"""

__authors__ = ["Lucas ROUAUD"]
__contact__ = ["lucas.rouaud@gmail.com"]
__copyright__ = "MIT License"

# [D]
from dataclasses import dataclass

# [P]
import pytest

# [S]
from src.perfassess.parse_argument.check_argument import check_argument


@dataclass
class ArgumentParserSimulator:
    """A class to simulate an argument parser.
    """

    def __init__(
        self,
        script: str,
        output: str,
        function: str,
        n_field: int,
        package: str,
        subpackage: str,
        argument: str
    ):
        """Simulate the creation of parsed arguments.

        Parameters
        ----------
        script : `str`
            The script path.

        output : `str`
            The directory to output results.

        function : `str`
            The function to assess.

        n_field : `int`
            The number of field to keep.

        package : `str`
            A package path.

        subpackage : `str`
            A subpackage path.

        argument : `str`
            A YAML file path.
        """
        self.script: str = script
        self.output: str = output
        self.function: str = function
        self.n_field: int = n_field
        self.package: str = package
        self.subpackage: str = subpackage
        self.argument: str = argument

    def redefine_parameter(self, **kwargs):
        """Give multiple parameters to redefine them.

        Raises
        ------
        `KeyError`
            If the given parameter does not exists.
        """
        for key, value in kwargs.items():
            if key == "script":
                self.script = value
            elif key == "output":
                self.output = value
            elif key == "function":
                self.function = value
            elif key == "n_field":
                self.n_field = value
            elif key == "package":
                self.package = value
            elif key == "subpackage":
                self.subpackage = value
            elif key == "argument":
                self.argument = value
            else:
                raise KeyError("[Err##] Wrong key given.")


@pytest.fixture
def __argument() -> dataclass:
    """Return a instantiated object of `PerformanceAssessor` to test it. Use a
    pytest magic method to only do it once.

    Returns
    -------
    `PerformanceAssessor`
        The class to test.
    """
    return ArgumentParserSimulator(
        script="src/perfassess/main.py",
        output="data/",
        function="main",
        n_field=0,
        package="src/perfassess/__init__.py",
        subpackage="src/perfassess/__init__.py",
        argument="data/argument.yml"
    )


@pytest.mark.parametrize(
    "parameter",
    [
        {"script": "//None//none.py"},
        {"output": "//None"},
        {"package": "//None//none__init__.py"},
        {"subpackage": "//None//none__init__.py"},
        {"argument": "//None//None.yml"}
    ]
)
def test_file_not_found(__argument: dataclass, parameter: dict):
    """Test if the file are not found.

    Parameters
    ----------
    __argument : `dataclass`
        The class that simulates input argument.

    parameter : `dict`
        The tested wrong file path.
    """
    # Satanic notation, please forgive me lord~.
    old_parameter = __argument.__dict__[list(parameter.keys())[0]]

    # Add wrong parameter.
    __argument.redefine_parameter(**parameter)

    # Test the error.
    with pytest.raises(FileNotFoundError):
        check_argument(__argument)

    for key in parameter.keys():
        parameter[key] = old_parameter

    # Give back good parameter.
    __argument.redefine_parameter(**parameter)


@pytest.mark.parametrize(
    "parameter",
    [
        {"script": "data/argument.yml"},
        {"output": "data/argument.yml"},
        {"n_field": -1},
        {"package": "data/argument.yml"},
        {"subpackage": "data/argument.yml"},
        {"argument": "src/perfassess/main.py"}
    ]
)
def test_value_error(__argument: dataclass, parameter: dict):
    """Test if error are well thrown when bad values are given.

    Parameters
    ----------
    __argument : `dataclass`
        The class that simulates input argument.

    parameter : `dict`
        The tested wrong values.
    """
    # Satanic notation, please forgive me lord~.
    old_parameter = __argument.__dict__[list(parameter.keys())[0]]

    __argument.redefine_parameter(**parameter)

    # Test the error.
    with pytest.raises(ValueError):
        check_argument(__argument)

    for key in parameter.keys():
        parameter[key] = old_parameter

    # Give back good parameter.
    __argument.redefine_parameter(**parameter)


@pytest.mark.parametrize(
    "parameter",
    [
        {"function": "none"}
    ]
)
def test_module_error(__argument: dataclass, parameter: dict):
    """Test if an error is thrown when a non-existing function is given.

    Parameters
    ----------
    __argument : `dataclass`
        The class that simulates input argument.

    parameter : `dict`
        The tested wrong function name.
    """
    __argument.redefine_parameter(**parameter)

    # Test the error.
    with pytest.raises(ValueError):
        check_argument(__argument)
