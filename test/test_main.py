r"""Test if "main.py" is functional.

Linting
-------
```sh
    $ pylint test/
```

Usage
-----
```sh
    # Execute this command line in a conda environment.
    $ pytest test/functional_assessor.py
```
"""

__authors__ = ["Lucas ROUAUD"]
__contact__ = ["lucas.rouaud@gmail.com"]
__copyright__ = "MIT License"

# [S]
from subprocess import run
from sys import version

# [P]
import pytest

# [P]
from src.main import PerformanceAssessor


# =========================================
#
#   Testing the PerformanceAssessor class.
#
# =========================================


@pytest.fixture
def __assessor() -> PerformanceAssessor:
    """Return a instantiated object of `PerformanceAssessor` to test it. Use a
    pytest magic method to only do it once.

    Returns
    -------
    `PerformanceAssessor`
        The class to test.
    """
    return PerformanceAssessor(main=lambda: 10, n_field=1, value=[0] * 1000)


def test_plot_path_exists(__assessor: PerformanceAssessor):
    """Test if an error is thrown when a path that does not exist is given.

    Parameters
    ----------
    __assessor : `PerformanceAssessor`
        The class to test.
    """
    with pytest.raises(FileNotFoundError):
        __assessor.plot("//not_a_directory")


def test_plot_is_directory(__assessor: PerformanceAssessor):
    """Test if an error is thrown when a path pointing to something else than a
    file is given.

    Parameters
    ----------
    __assessor : `PerformanceAssessor`
        The class to test.
    """
    with pytest.raises(ValueError):
        __assessor.plot("data/existing_file.txt")

