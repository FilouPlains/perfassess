
# ⌨️ Using command line

## ✏️ General note

By doing:

```sh
$ perfassess --help
```

You will get the help to use the command line interface. Here are the used legends:

- **`int`:** Integer.
- **`str`:** String.
- **`[type|value]`:** Type of the input required, follow by the default value. So if this optional arguments is not used, “value” will be chosen.

> ⚠️ If you use `pickle`, the command line interface will not work!

## 📄 Normal use

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
             -f testor
             -a data/argument.yml \\
             -o data/
```

## 📁 Package use

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

!!!note
    Packages are identify with `__init__.py` files and allow relatives import.

## 🗂 Subpackage use

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

!!!note
    Packages are identify with `__init__.py` files and allow relatives import.

## 🔍 Describing possible parameters

| **Argument**             | **Mandatory?** | **Type and usage**                  | **Description**                                    |
| :----------------------- | :------------: | :---------------------------------- | :------------------------------------------------- |
| **`-s`<br>`--script`**   |      Yes       | `-s script.py`                      | The script that contain the function to test.      |
| **`-o`<br>`--output`**   |      Yes       | `-o output_directory/`              | The directory where the plot have to be produced.  |
| **`-f`<br>`--function`** |       No       | `-f main`                           | The function to test.                              |
| **`-a`<br>`--argument`** |       No       | `-a argument.yml`                   | The argument to passe to the function to test*.    |
| **`--n_field`**          |       No       | `-n_field 2`                        | The number of field to keep**.                     |
| **`--package`**          |       No       | `--package package/__init__.py`     | The `__init__.py` file of the top package to test. |
| **`--subpackage`**       |       No       | `-o package/subpackage/__init__.py` | The `__init__.py` file of the subpackage to test.  |
| **`-h`<br>`--help`**     |       No       | Flag                                | Display the help and exit the program.             |
| **`-v`<br>`--version`**  |       No       | Flag                                | Display the version and exit the program.          |

- **\* =** If you want to test a function that requires arguments, you can give to the command line interface a `argument.yml` file that contains all required arguments. If the tested function requires an argument like `toto`, you can put in the YAML file:

```yml
toto: 10
```

- **\*\* =** In memory usage, tested functions are going to be named something like `/home/user/Documents/program/package/script.py`. To shorten the name, use the `--n_field` tag. For instance, giving 2 will let know to the program that you want to only keep the last to field, which in the end will look something like: `package/script.py`.

## 🗒 YAML file example

For the next python function, [describe here](../../code_documentation/testor/):

```py
def testor(value: list, to_add: int = 1):
    """A function to launch the program in order to test it.

    Parameters
    ----------
    value : `list`
        A list of values.

    to_add : `int`, optional
        An optional argument to test them. By default 1.
    """
    for value_i in value:
        to_add += value_i
```

You can see that the function have:

- **An mandatory argument `value`:** it is a list of value.
- **An optional argument `to_add`:** it is an integer with the default value of 1.

That means that you need a way to provide the arguments to the function when you are going to use the command line interface. The chosen method is a YAML file. An example of a file, [available here in the GitHub repository](https://github.com/FilouPlains/perfassess/blob/main/data/argument.yml), is the following:

```yaml
value: [1, 2, 3]
```

That means that, when launching the command line, you are going to give to value a list that look like this: `[1, 2, 3]`. Translate in python code, it would be something like:

```py
testor(value = [1, 2, 3])
```

As you can see, only the mandatory argument is given. You do not need to specify anything for the optional ones. If you want to, an other example of YAML file could look to something like this:

```yaml
value: [1, 2, 3]
to_add: 100
```

To finish, you can actually directly test the program in the repository root (`📁 perfassess/`) using:

```sh
$ perfassess -s src/perfassess/testor.py \\
             -f testor \\
             -a data/argument.yml \\
             -o data/
```

Which is an example of launching the command giving arguments to the function `testor()` with a YAML file. If you function do not need any arguments, then the command could look to something like this:

```sh
$ perfassess -s src/perfassess/testor.py \\
             -f testor \\
             -o data/
```

!!!note
    In the background, `pyyaml` is used to parse the file and translate it into a dictionary. Then, we can pass it to the wanted function using `**kwargs` python unpacking “method”.
