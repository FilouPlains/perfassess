# 📦 Module

## 🪜 Step by step script

To use the script as a module, you only need to import the class `PerformanceAssessor()` as so:

```py
from perfassess.class_performance_assessor import PerformanceAssessor

...
```

You can also, for testing, import `testor()` as so:

```py
...

from perfassess.testor import testor

...
```

You can now launch the class on `testor()` for instance:

```py
...


assessor: PerformanceAssessor = PerformanceAssessor(
    main=testor,
    n_field=1,
    value=[0] * 1000
)

assessor.launch_profiling()
assessor.plot(path="output_directory/")

```

Do not forget to change `📁 output_directory/` as your wish!

## 🧪 Full test script

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
