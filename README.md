<div align="center">

# ⌛️ PERFASSESS 💾

[![Python 3.10.8](https://img.shields.io/badge/python-%E2%89%A5_3.11.5-blue.svg)](https://www.python.org/downloads/release/python-397/)
[![Conda 22.11.1](https://img.shields.io/badge/miniconda-%E2%89%A5_23.11.0-green.svg)](https://docs.conda.io/en/latest/miniconda.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


✍ Contributor: **Lucas ROUAUD**

</div align="center">

## 📒 Description

**This module permit to evaluate the performance of a given function and create Plotly bar plot.**



## ⚙️ Installation


### 👬 Cloning the repository

You can clone the repository using `HTTPS`:

```bash
$ git clone https://github.com/FilouPlains/perfassess.git
```

or using `SSH`:

```bash
$ git clone git@github.com:FilouPlains/perfassess.git
```

Then go to the `📁 perfassess/` directory:

```bash
$ cd perfassess
```

**All next commands are assuming that you are in the `📁 perfassess/` directory. This directory will be name as `📁 ./`.**

### 🐍📦 Installing with pip

Simply launch this command in the `📁 ./` directory:

```bash
$ python3 -m pip install .
```

**You are now able to launch the program!**


## ⌨️ Using command line

### ✏️ General note

By doing:

```sh
$ python -m src.main --help
```

You will get the help to use the command line interface. Here are the used legends:

- **`int`:** Integer.
- **`str`:** String.
- **`[type|value]`:** Type of the input required, follow by the default value. So if this optional arguments is not used, “value” will be chosen.

> ⚠️ If you use `pickle`, the command line interface will not work!


### 📄 Normal use

To use th program, launch:

```sh
$ perfassess -s script.py \\
             -f function_name \\
             -o output_directory/ \\
             -a argument.yml
```

### 📁 Package use


If you use this module to test another or, in another words, a package, the usage is a bit different. If you have no “subpackage”, you have to launch, for this kind of tree structure:

```sh
./package/
└── src/
    ├── __init__.py
    └── script.py
```

The next command, if you are in `./package`, in order to evaluate `script.py`:

```sh
$ perfassess -s src/script.py \\
             -f function_name \\
             -o output_directory/ \\
             --package src/__init__.py \\
             -a argument.yml
```

> **Note 📝**
> 
> Packages are identify with `__init__.py` files and allow relatives import.

### 🗂 Subpackage use

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
$ perfassess -s src/subpackage/script.py \\
             -f function_name \\
             -o output_directory/ \\
             --package src/__init__.py \\
             --subpackage src/subpackage/__init__.py \\
             -a argument.yml
```

> **Note 📝**
> 
> Packages are identify with `__init__.py` files and allow relatives import.



_This work is licensed under a [MIT License](https://opensource.org/licenses/MIT)._


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
