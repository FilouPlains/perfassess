r"""Test if "src/main.py" is functional.

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
    performance_assessor: PerformanceAssessor = PerformanceAssessor(
        main=lambda: 10,
        n_field=1
    )

    performance_assessor.launch_profiling()

    return performance_assessor


def test_plot_path_not_exists(__assessor: PerformanceAssessor):
    """Test if an error is thrown when a path that does not exist is given.

    Parameters
    ----------
    __assessor : `PerformanceAssessor`
        The class to test.
    """
    with pytest.raises(FileNotFoundError):
        __assessor.plot("//not_a_directory")


def test_plot_is_not_directory(__assessor: PerformanceAssessor):
    """Test if an error is thrown when a path pointing to something else than a
    file is given.

    Parameters
    ----------
    __assessor : `PerformanceAssessor`
        The class to test.
    """
    with pytest.raises(ValueError):
        __assessor.plot("data/existing_file.txt")


def test_launch_no_profiling(__assessor: PerformanceAssessor):
    """Test if an error is thrown when either `do_memory` and `do_time` are set
    to `False`.

    Parameters
    ----------
    __assessor : `PerformanceAssessor`
        The class to test.
    """
    with pytest.raises(ValueError):
        __assessor.launch_profiling(do_memory=False, do_time=False)
