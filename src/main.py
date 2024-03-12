r"""Compute actually time and memory consumption.

Details about cProfile output
-----------------------------

|     Value     | Description                                              |
| :-----------: | :------------------------------------------------------- |
| **`ncalls`**  | Shows the number of calls made.                          |
| **`tottime`** | Total time taken by the given function. The time made in |
|               | calls to sub-functions are excluded.                     |
| **`percall`** | Total time per numbers of calls.                         |
| **`cumtime`** | Like `tottime`, but includes time spent in all called    |
|               | subfunctions.                                            |
| **`percall`** | Quotient of `cumtime` divided by primitive calls. The    |
|               | primitive calls include all calls not included through   |
|               | recursion.                                               |

[Information get here](https://www.machinelearningplus.com/python/cprofile-how-
to-profile-your-python-code/)

Linting
-------
```sh
    $ pylint src/
```

Usage
-----
To evaluate a function performance, import the module object as followed:

```py
from main.performance_assessor import PerformanceAssessor

...
```

If you want to test what the module is doing, launch the following command:

```sh
    # Execute this command line in a conda environment.
    $ python -m main.performance_assessor
```

And check the result in the "data/" subdirectory.
"""

__authors__ = ["Lucas ROUAUD"]
__contact__ = ["lucas.rouaud@gmail.com"]
__version__ = "0.0.1"
__date__ = "12/03/2024"
__copyright__ = "MIT License"

# [C]
from cProfile import Profile
# [I]
from io import StringIO
# [P]
from pstats import Stats
import sys
# [T]
import tracemalloc
from typing import Callable
# [O]
from os.path import exists, isdir

# [N]
import numpy as np
# [P]
import plotly.graph_objects as go


class PerformanceAssessor:
    """A class to access the performance of a given function (memory or time).
    """

    def __init__(
        self,
        main: Callable,
        n_field: int = 9,
        **kwargs
    ):
        """Initialize a PerformanceAssessor object.

        Parameters
        ----------
        main : `Callable`
            The function to access.
        n_field : `int`, optional
            The number of field to keep in function name. By default 9.

            Let us say that we have a function named like this:

            >>> /home/user/Document/some_function.py:000(function_name)

            If input 2, we will have something like this:

            >>> Document/some_function.py:000(function_name)

            We split at each "/" and keep the last two field.
        kwargs
            All possible arguments for the function to test.

        Example
        -------
        >>> assessor: PerformanceAssessor = PerformanceAssessor(
        >>>     main=function_to_test,
        >>>     n_field=1,
        >>>     argument_for_function_to_test="some_value"
        >>> )
        """
        self.__assessed_function: Callable = main
        self.__function_argument: dict = dict(kwargs)
        self.__plot: "dict[go.Figure]" = {}
        self.n_field: int = n_field

    def launch_profiling(
        self,
        do_memory: bool = True,
        do_time: bool = True
    ):
        """Launch the evaluation of performance (memory or time).

        Parameters
        ----------
        do_memory : `bool`, optional
            Do the memory evaluation. By default True.
        do_time : `bool`, optional
            Do the time evaluation. By default True.

        Raises
        ------
        ValueError
            When both `do_memory` and `do_time` are set to `False`.
        """
        if not do_memory and not do_time:
            raise ValueError("[Err##] One value between \"do_memory\" or "
                             "\"do_time\" have to set to `True`.")

        if do_memory:
            # Starting to check memory usage.
            tracemalloc.start()

        if do_time:
            profile: Profile = Profile()
            # Starting to check time usage.
            profile.enable()

        # Launch the function to test.
        self.__assessed_function(**self.__function_argument)

        if do_memory:
            # Get a traceback of memory usage.
            snapshot = tracemalloc.take_snapshot()

            # Create the plot for evaluating memory usage.
            self.__memory_evaluation(stat_memory=snapshot.statistics("lineno"))

            # Stop to check memory usage.
            tracemalloc.stop()

        if do_time:
            # Stop to check time usage.
            profile.disable()

            # Create the plot for evaluating memory usage.
            self.__time_evaluation(profile=profile)

    def __memory_evaluation(
        self,
        stat_memory: tracemalloc.Statistic
    ):
        """Parsed memory evaluation output and set a plot.

        Parameters
        ----------
        stat_memory : `tracemalloc.Statistic`
            The "assessor".
        """
        stat_dict = {}

        # Setting the dataset for memory usage.
        for stat in stat_memory:
            key: str = str(stat).split()[0]

            if self.n_field > 0:
                key = key.split(sep="/", maxsplit=self.n_field + 1)[-1]

            if key not in stat_dict:
                stat_dict[key] = 0

            stat_dict[key] += stat.size

        # Draw and save the plot for memory usage.
        self.__plot["memory_evaluation"] = self.__set_plot(
            head=np.array(["size (Mib)", "function"]),
            label=np.array(list(stat_dict.keys())),
            data=np.array([list(stat_dict.values())]).T / 1024
        )

    def __time_evaluation(
        self,
        profile: Profile
    ):
        """Parsed time evaluation output and set a plot.

        Parameters
        ----------
        profile : `Profile`
            The "assessor".
        """
        # Redirect print stdout into a buffer.
        buffer: StringIO = StringIO()
        sys.stdout = buffer

        # Get the traceback of time execution.
        stat_time: Stats = Stats(profile).strip_dirs().print_stats()
        stat_time = buffer.getvalue()

        # Set the print stdout standard behaviour.
        sys.stdout = sys.__stdout__

        skip_line: bool = True
        data_label: np.array = np.array([])
        numeric_data: np.array = np.array([])

        # Setting the dataset for time usage.
        for line in stat_time.strip().split("\n"):
            if "ncalls" in line:
                data_head: np.array = np.array(line.split())
                # Add units (seconds) to each header, but the first one.
                data_head = np.char.add(data_head, ["", *[" (s)"] * 4, ""])

                # pylint: disable=C0103
                # It is not a constant pylint!
                skip_line = False
                # pylint: enable=C0103
                continue

            if skip_line or "/" in line:
                continue

            line: list = line.split(maxsplit=5)

            data_label = np.append(data_label, line[-1])

            if numeric_data.shape[0] == 0:
                numeric_data = np.array(line[:-1])
            else:
                numeric_data = np.vstack((numeric_data, line[:-1]))

        numeric_data = numeric_data.astype(float)

        # Draw and save the plot for time usage.
        self.__plot["time_evaluation"] = self.__set_plot(
            head=data_head,
            label=data_label,
            data=numeric_data
        )

    # pylint: disable=too-many-arguments, too-many-instance-attributes
    # Special class that needs a lot of data to be set up. Using a dataclass
    # would be unnecessary, as far as it would just simply take more memory
    # for nothing.

    def __set_plot(
        self,
        head: np.array,
        label: np.array,
        data: np.array,
        foreground: str = "#2E2E3E",
        background: str = "rgba(0, 0, 0, 0)"
    ) -> go.Figure:
        """Set a Plotly bar plot based on computed evaluation.

        Parameters
        ----------
        head : `np.array`
            The data header (like ncall). Or like one label per column.
        label : `np.array`
            The data label (like functions names). Or like one label per row.
        data : `np.array`
            The numerical data.
        foreground : `str`, optional
            The "foreground" color. By default "#2E2E3E".
        background : `str`, optional
            The "background" color. By default "rgba(0, 0, 0, 0)".

        Returns
        -------
        go.Figure
            The setted Plotly bar plot.
        """
        plot: object = go.Figure()

        sort_i: np.array = np.flip(np.argsort(data.T[0]))

        # Trace the barplot
        plot.add_trace(go.Bar(
            x=label[sort_i],
            y=data.T[0][sort_i],
            marker_line_color=foreground,
            marker_color=foreground
        ))

        # Modify general plot properties.
        plot.update_layout(
            template="plotly_white",
            margin={"r": 5},
            font={"size": 32, "family": "Roboto Light"},
            xaxis={
                "title": f"<b>Tested function ({head[-1]})</b>",
                "showline": True,
                "linewidth": 1,
                "showgrid": False,
                "title_font": {"family": "Roboto Black"},
                "tickfont": {"size": 16}
            },
            yaxis={
                "title": f"<b>{head[0].capitalize()}</b>",
                "showline": True,
                "linewidth": 1,
                "showgrid": False,
                "title_font": {"family": "Roboto Black"},
                "tickfont": {"size": 16}
            },
            title_font={"family": "Roboto Black"},
            plot_bgcolor=background,
            paper_bgcolor=background,
        )

        # Add the rectangle border.
        plot.add_shape(
            type="rect",
            xref="paper",
            yref="paper",
            x0=0,
            y0=0,
            x1=1,
            y1=1,
            line={"width": 2, "color": foreground}
        )

        plot.update_traces()

        # Adding the dropdown menu in the case of multiple datas.
        if data.T.shape[0] != 1:
            # Add the dropdown to the plot.
            plot.update_layout(updatemenus=self.__add_dropdown(
                foreground=foreground,
                head=head,
                label=label,
                data=data
            ))

        return plot

    # pylint: enable=too-many-arguments

    def __add_dropdown(
        self,
        head: np.array,
        label: np.array,
        data: np.array,
        foreground: str
    ) -> list:
        """Add a dropdown to the Plotly plot, in order to select different
        assessed values.

        Parameters
        ----------
        head : `np.array`
            The data header (like ncall). Or like one label per column.
        label : `np.array`
            The data label (like functions names). Or like one label per row.
        data : `np.array`
            The numerical data.
        foreground : `str`
            The "foreground" color.

        Returns
        -------
        `list`
            The dropdown menu, which is a `update_menu`.
        """
        button: list = []

        for i, label_i in enumerate(head[:-1]):
            sort_i: np.array = np.flip(np.argsort(data.T[i]))

            # Add a element in the dropdown. By selecting it, it will modify
            # the plot.
            button += [{
                "method": "update",
                "label": label_i,
                "args": [
                    # Restyling.
                    {"x": [label[sort_i]], "y": [data.T[i][sort_i]]},
                    # Updating.
                    {"yaxis": {
                        "showline": True,
                        "linewidth": 1,
                        "showgrid": False,
                        "title": {
                            "text": f"<b>{label_i.capitalize()}</b>",
                            "font": {"family": "Roboto Black"}
                        },
                        "tickfont": {"size": 16}
                    }}
                ],
            }]

        # Create the dropdown menu.
        update_menu: list = [{
            "buttons": button,
            "type": "dropdown",
            "direction": "down",
            "showactive": True,
            "x": 1,
            "xanchor": "right",
            "y": 1.01,
            "yanchor": "bottom",
            "bgcolor": "#FFF",
            "bordercolor": foreground,
            "borderwidth": 2,
            "font_color": foreground
        }]

        return update_menu

    def plot(
        self,
        path: str = "./"
    ):
        """Save the plot to a `.html` file.

        Parameters
        ----------
        path : `str`, optional
            The path to save the file, which have to be a directory. By default
            "./".

        Raises
        ------
        FileNotFoundError
            If the input path does not exist.
        ValueError
            If the input path is not a directory.
        """
        if path.endswith("/"):
            path = path[:-1]

        if not exists(path):
            raise FileNotFoundError(f"[Err##] Given path \"{path}\" does not "
                                    "exist.")
        if not isdir(path):
            raise ValueError(f"[Err##] Given path  \"{path}\" is not "
                             "directory.")

        for key, plot_i in self.__plot.items():
            # Save the plot.
            plot_i.write_html(
                file=f"{path}/{key}.html",
                include_plotlyjs=True,
                full_html=True
            )

    def get_plot(self) -> dict:
        """Get the setted plot.

        Returns
        -------
        `dict`
            The setted plot.
        """
        return self.__plot


if __name__ == "__main__":
    def __testor(value: list, to_add: int = 1):
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

    assessor: PerformanceAssessor = PerformanceAssessor(
        main=__testor,
        n_field=1,
        value=[0] * 1000
    )

    assessor.launch_profiling()
    assessor.plot(path="data/")
