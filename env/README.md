# Environment setup 🔧

[![Python 3.10.8](https://img.shields.io/badge/python-%E2%89%A5_3.11.5-blue.svg)](https://www.python.org/downloads/release/python-397/)
[![Conda 22.11.1](https://img.shields.io/badge/miniconda-%E2%89%A5_23.11.0-green.svg)](https://docs.conda.io/en/latest/miniconda.html)

## 🐍📦 Installing conda

First, you need to install conda to use this software. All information to installed conda are listed here: https://docs.anaconda.com/free/miniconda/index.html#quick-command-line-install

**All next commands are to used when you are in the `📁 env/` directory:**

## 📶 Installing the environment with conda

### 🐍⚡️ Installing mamba

Mamba is a fast packages installer. If it is not yet installed, do:

```bash
$ conda activate base
$ conda install conda-forge::mamba
```

### ⛰ Installing the environment

To set the environment, launch in the terminal the following command:

```bash
$ mamba env create --file performance_assessor.yml
$ conda activate performance_assessor
```

## 📶 Installing the environment with pip

To set the environment, launch in the terminal the following command:

```bash
$ python -m pip install -r requirements.txt
```

## Module list 📝

| **Module**                          | **Version** |
| :---------------------------------- | :---------: |
| mamba                               |   `1.5.5`   |
| plotly                              |  `5.19.0`   |
| pylint                              |  `2.16.2`   |
| pytest                              |   `7.4.0`   |
| **pip:** ipython                    |  `8.22.2`   |
| **pip:** markdown                   |   `3.5.2`   |
| **pip:** mkdocs                     |   `1.5.3`   |
| **pip:** mkdocs-autorefs            |   `1.0.1`   |
| **pip:** mkdocs-callouts            |  `1.13.2`   |
| **pip:** mkdocs-material            |  `9.5.14`   |
| **pip:** mkdocs-material-extensions |   `1.3.1`   |
| **pip:** mkdocstrings               |  `0.24.1`   |
| **pip:** mkdocstrings-python        |   `1.9.0`   |

