from setuptools import find_packages, setup

if __name__ == "__main__":
    long_description: str = ""

    with open("README.md", "r", encoding="utf-8") as file:
        long_description = file.read()

    setup(
        name="performance_assessor",
        version="0.0.1",
        description=("Access the performance of a given function and create"
                     "plot."),
        package_dir={"": "src"},
        packages=find_packages(where="src"),
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/FilouPlains/performance_assessor",
        author="FilouPlains",
        author_email="lucas.rouaud@gmail.com",
        license="MIT",
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Natural Language :: English",
            "Programming Language :: Python :: 3.10"
        ],
        install_requires=[
            "plotly >= 5.19.0"
        ],
        extras_require={
            "dev": [
                "ipython >= 8.22.2",
                "markdown >= 3.5.2",
                "mkdocs >= 1.5.3",
                "mkdocs-autorefs >= 1.0.1",
                "mkdocs-callouts >= 1.13.2",
                "mkdocs-material >= 9.5.14",
                "mkdocs-material-extensions >= 1.3.1",
                "mkdocstrings >= 0.24.1",
                "mkdocstrings-python >= 1.9.0",
                "pylint >= 2.16.2",
                "pytest>=7.0"
            ],
        },
        python_requires=">=3.10",
    )
