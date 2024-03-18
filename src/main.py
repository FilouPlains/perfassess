r"""Compute actually time and memory consumption.

Details about cProfile output
-----------------------------

|     Value     | Description                                              |
| :-----------: | :------------------------------------------------------- |
| **`ncalls`**  | Shows the number of calls made.                          |
| **`tottime`** | Total time taken by the given function. The time made in |
|               | calls to sub-functions are excluded.                     |
| **`percall`** | Total time per numbers of calls.                         |
| **`cumtime`** | Like `tottime`, but includes time spent in all called    |
|               | subfunctions.                                            |
| **`percall`** | Quotient of `cumtime` divided by primitive calls. The    |
|               | primitive calls include all calls not included through   |
|               | recursion.                                               |

[Information get here](https://www.machinelearningplus.com/python/cprofile-how-
to-profile-your-python-code/)

Linting
-------
```sh
    $ pylint src/
```

Usage
-----
To evaluate a function performance, import the module object as followed:

```py
from main.performance_assessor import PerformanceAssessor

...
```

If you want to test what the module is doing, launch the following command:

```sh
    # Execute this command line in a conda environment.
    $ python -m main.performance_assessor
```

And check the result in the "data/" subdirectory.
"""

__authors__ = ["Lucas ROUAUD"]
__contact__ = ["lucas.rouaud@gmail.com"]
__version__ = "0.0.1"
__date__ = "18/03/2024"
__copyright__ = "MIT License"

from typing import Callable


# [C]
from .class_performance_assessor import PerformanceAssessor
# [P]
from .parse_argument import parse_argument


def main(
    function: Callable,
    n_field: int,
    output: str,
    argument: dict
):
    assessor: PerformanceAssessor = PerformanceAssessor(
        main=function,
        n_field=n_field,
        **argument
    )

    assessor.launch_profiling()
    assessor.plot(path=output)


if __name__ == "__main__":
    __argument = parse_argument()

    main(
        function=__argument.function,
        n_field=__argument.n_field,
        output=__argument.output,
        argument=__argument.argument
    )
