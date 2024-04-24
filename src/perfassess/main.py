r"""Compute time and memory consumption.

Linting
-------
```sh
$ pylint src/
```

Usage
-----
You can go on:
https://github.com/FilouPlains/perfassess

To check how to install this module. After, you can launch the module as a
command line. To know what is possible, launch:
```sh
$ perfassess --help
```

Else, you are also able to import the module object as followed:

```py
from perfassess.class_performance_assessor import PerformanceAssessor
from perfassess.testor import testor

assessor: PerformanceAssessor = PerformanceAssessor(
    main=testor,
    n_field=1,
    value=[0] * 1000
)

assessor.launch_profiling()
assessor.plot(path="output_directory/")
```

With "output_directory/" being the output directory of your choice
"""

__authors__ = ["Lucas ROUAUD"]
__contact__ = ["lucas.rouaud@gmail.com"]
__version__ = "0.0.4"
__date__ = "22/03/2024"
__copyright__ = "MIT License"


# [C]
from .class_performance_assessor import PerformanceAssessor
# [P]
from .parse_argument.parse_argument import parse_argument


def main():
    """Main function.
    """
    __argument = parse_argument(version=__version__)

    assessor: PerformanceAssessor = PerformanceAssessor(
        main=__argument.function,
        n_field=__argument.n_field,
        **__argument.argument
    )

    assessor.launch_profiling()
    assessor.plot(path=__argument.output)


if __name__ == "__main__":
    main()
