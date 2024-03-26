<div id="to-center">

<h1>⌛️ PERFASSESS 💾</h1>

<p>
    <a href="https://www.python.org/downloads/release/python-397/"><img src="https://img.shields.io/badge/python-%E2%89%A5_3.11.5-blue.svg"/></a>
    <a href="https://docs.conda.io/en/latest/miniconda.html"><img src="https://img.shields.io/badge/miniconda-%E2%89%A5_23.11.0-green.svg"/></a>
    <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg"/></a>
</p>

<p>✍ Contributor: <strong>Lucas ROUAUD</strong></p>

<p><strong>🐱 GitHub repository:</strong> <a href="https://github.com/FilouPlains/perfassess">https://github.com/FilouPlains/perfassess</a></p>

</div>

## 📒 Description

**This module permit to evaluate the performance of a given function and create Plotly bar plot.**

## 📊 Results example

Next are Plotly interactive results. These are obtained using next command, in `📁 perfassess/` directory from the GitHub repository:

```bash
$ perfassess -s perfassess/testor.py \\
             -f testor \\
             -o data/ \\
             -a data/argument.yml
```



### ⏳ Time evaluation

<iframe src="plot/time_evaluation.html">
</iframe>

### 🧠 Memory evaluation

<iframe src="plot/memory_evaluation.html">
</iframe>


## 🙇‍♂️ Aknowledgement

🔍 Code reviewing: **Hubert Santuz**

_This work is licensed under a [MIT License](https://opensource.org/licenses/MIT)._

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
