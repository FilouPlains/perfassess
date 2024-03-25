
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

## 📁 Package use


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

!!!note
    Packages are identify with `__init__.py` files and allow relatives import.

## 🗂 Subpackage use

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

!!!note
    Packages are identify with `__init__.py` files and allow relatives import.

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

An example of file, [available here in the GitHub repository](https://github.com/FilouPlains/perfassess/blob/main/data/argument.yml), is the following:

```yaml
value: [1, 2, 3]
```

As you can see, only the mandatory argument is given. You do not need to specify anything for the optional ones. If you want to, it could look to something like this:

```yaml
value: [1, 2, 3]
to_add: 100
```

In the background, `pyyaml` is used to parse the file and translate it into a dictionary. Then, we can pass it to the wanted function using `**kwargs` python unpacking “method”.
