# PERFASSESS

## Description

This module/software permits to easily compute the time and memory usage of a python function. It is possible to import the module or use it with a command line interface.

## Results example

Next are Plotly interactive results.

### Time evaluation

<iframe src="plot/time_evaluation.html">
</iframe>

### Memory evaluation

<iframe src="plot/memory_evaluation.html">
</iframe>

## Program help

### General note

By doing:

```sh
$ python -m src.main --help
```

You will get the help to use the command line interface. Here are the used legends:

- **`int`:** Integer.
- **`str`:** String.
- **`[type|value]`:** Type of the input required, follow by the default value. So if this optional arguments is not used, “value” will be chosen.


### Normal use

Assess. is a program to assess the time execution of a given script in python. To use it, launch:

```sh
$ python -m src.main \\
            -s script.py \\
            -f function_name \\
            -o output_directory/ \\
            -a argument.yml
```

### Package use


If you use this module to test another or, in another words, a package, the usage is a bit different. If you have no “subpackage”, you have to launch, for this kind of tree structure:

```sh
./package/
└── src/
    ├── __init__.py
    └── script.py
```

The next command, if you are in `./package`, in order to evaluate `script.py`:

```sh
$ python -m src.main \\
         -s src/script.py \\
         -f function_name \\
         -o output_directory/ \\
         --package src/__init__.py \\
         -a argument.yml
```

!!! note
    Packages are identify with `__init__.py` files and allow relatives import.

### Subpackage use

If you use this module to test another or, in another words, a package, the usage is a bit different. If you have to test a “subpackage”, you have to launch, for this kind of tree structure:

```sh
./package/
└── src/
    ├── __init__.py
    └── subpackage/
        ├── __init__.py
        └── script.py
```

The next command, if you are in `./package`, in order to evaluate `script.py`:


```sh
$ python -m src.main \\
         -s src/subpackage/script.py \\
         -f function_name \\
         -o output_directory/ \\
         --package src/__init__.py \\
         --subpackage src/subpackage/__init__.py \\
         -a argument.yml
```

!!! note
    Packages are identify with `__init__.py` files and allow relatives import.
