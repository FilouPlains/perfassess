# class_performance_assessor.py

## Details about cProfile output

|     Value     | Description                                                                                                             |
| :-----------: | :---------------------------------------------------------------------------------------------------------------------- |
| **`ncalls`**  | Shows the number of calls made.                                                                                         |
| **`tottime`** | Total time taken by the given function. The time made in calls to sub-functions are excluded.                           |
| **`percall`** | Total time per numbers of calls.                                                                                        |
| **`cumtime`** | Like `tottime`, but includes time spent in all called subfunctions.                                                     |
| **`percall`** | Quotient of `cumtime` divided by primitive calls. The primitive calls include all calls not included through recursion. |

Information was collected here: [https://www.machinelearningplus.com/python/cprofile-how-
to-profile-your-python-code/](https://www.machinelearningplus.com/python/cprofile-how-
to-profile-your-python-code/)

::: src.perfassess.class_performance_assessor
