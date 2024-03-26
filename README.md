<div align="center">

# ⌛️ PERFASSESS 💾

[![Python 3.10.8](https://img.shields.io/badge/python-%E2%89%A5_3.11.5-blue.svg)](https://www.python.org/downloads/release/python-397/)
[![Conda 22.11.1](https://img.shields.io/badge/miniconda-%E2%89%A5_23.11.0-green.svg)](https://docs.conda.io/en/latest/miniconda.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


✍ Contributor: **Lucas ROUAUD**

</div align="center">

## 📒 Description

**This module permit to evaluate the performance of a given function and create Plotly bar plot.**

## 🗄 Dependencies

To run this software, you will need `python ≥ 3.10` and this next module:

- `numpy ≥ 1.26.0`
- `plotly ≥ 5.19.0`
- `pyyaml ≥ 6.0.1`

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
$ perfassess --help
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

You can actually directly test the program in the repository root (`📁 perfassess/`) using:

```sh
$ perfassess -s src/perfassess/testor.py \\
             -f testor \\
             -a data/argument.yml \\
             -o data/
```

### 📁 Package use

Let us say that you want to test a package, which should have this kind of tree structure:

```sh
package/
└── src/
    ├── __init__.py
    └── script.py
```

In package, you can use relative paths. But with these, the “normal use” method do not work. Instead, use the next command, if you are in `📁 package/`, in order to evaluate `script.py`:

```sh
$ perfassess -s src/script.py \\
             -f function_name \\
             -o output_directory/ \\
             --package src/__init__.py \\
             -a argument.yml
```

In addition of the previous "normal use" method, you have to indicate a `__init__.py` file.

> **Note 📝**
> 
> Packages are identify with `__init__.py` files and allow relatives import.

### 🗂 Subpackage use

Let us say that you want to test a subpackage, which should have this kind of tree structure:

```sh
./package/
└── src/
    ├── __init__.py
    └── subpackage/
        ├── __init__.py
        └── script.py
```

In subpackage, you can use relative paths. But with these, the “normal use” method do not work. But the “package use” also do not work. Instead, use the next command, if you are in `📁 package/`, in order to evaluate `script.py`:

```sh
$ perfassess -s src/subpackage/script.py \\
             -f function_name \\
             -o output_directory/ \\
             --package src/__init__.py \\
             --subpackage src/subpackage/__init__.py \\
             -a argument.yml
```

In addition of the previous “normal use” and “package use” method, you have to indicate two `__init__.py` files. The first one is the top package `__init__.py` file. The second one is the `__init__.py` file of the subpackage to test.

> **Note 📝**
> 
> Packages are identify with `__init__.py` files and allow relatives import.

### 🔍 Describing possible parameters

| **Argument**             | **Mandatory?** | **Type and usage**                  | **Description**                                    |
| :----------------------- | :------------: | :---------------------------------- | :------------------------------------------------- |
| **`-s` or `--script`**   |      Yes       | `-s script.py`                      | The script that contain the function to test.      |
| **`-o` or `--output`**   |      Yes       | `-o output_directory/`              | The directory where the plot have to be produced.  |
| **`-f` or `--function`** |       No       | `-f main`                           | The function to test.                              |
| **`-a` or `--argument`** |       No       | `-a argument.yml`                   | The argument to passe to the function to test*.    |
| **`--n_field`**          |       No       | `-n_field 2`                        | The number of field to keep**.                     |
| **`--package`**          |       No       | `--package package/__init__.py`     | The `__init__.py` file of the top package to test. |
| **`--subpackage`**       |       No       | `-o package/subpackage/__init__.py` | The `__init__.py` file of the subpackage to test.  |
| **`-h` or `--help`**     |       No       | Flag                                | Display the help and exit the program.             |
| **`-v` or `--version`**  |       No       | Flag                                | Display the version and exit the program.          |

- **\* =** If you want to test a function that requires arguments, you can give to the command line interface a `argument.yml` file that contains all required arguments. If the tested function requires an argument like `toto`, you can put in the YAML file:

```yml
toto: 10
```

- **\*\* =** In memory usage, tested functions are going to be named something like `/home/user/Documents/program/package/script.py`. To shorten the name, use the `--n_field` tag. For instance, giving 2 will let know to the program that you want to only keep the last to field, which in the end will look something like: `package/script.py`.

## 🙇‍♂️ Aknowledgement

🔍 Code reviewing: **Hubert Santuz**

_This work is licensed under a [MIT License](https://opensource.org/licenses/MIT)._


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
