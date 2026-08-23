import os
import sys


def configure_spark_env() -> None:
    """Ensure Spark uses the same Python interpreter as the active venv."""
    python_path = sys.executable
    os.environ["PYSPARK_PYTHON"] = python_path
    os.environ["PYSPARK_DRIVER_PYTHON"] = python_path


configure_spark_env()
