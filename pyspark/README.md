# PySpark practice

This folder is isolated from the rest of the Python scripts. Its virtual environment lives in `.venv/` and is intentionally ignored by Git.

## One-time setup (PowerShell)

From the repository root:

```powershell
cd .\pyspark
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If PowerShell blocks activation, run this once in the current terminal:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Java is required by Spark. This machine currently has Java 18 available. If Spark reports a Java compatibility error, use a supported JDK such as Java 17 and set `JAVA_HOME` before running.

## Run the starter example

```powershell
python .\examples\hello_spark.py
```

The example starts Spark locally, creates a small DataFrame, displays it, and stops the Spark session.

## VS Code setup

Select the interpreter at `pyspark/.venv/Scripts/python.exe` with **Python: Select Interpreter**. New practice files can go in `examples/`, or you can add topic folders such as `dataframes/`, `sql/`, and `rdd/`.

Deactivate the environment when finished:

```powershell
deactivate
```
