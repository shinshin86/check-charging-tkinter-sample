import sys
from cx_Freeze import setup, Executable
from setuptools import find_packages

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("main.py", base=base)]

setup(
    name="check-charging-tkinter-sample",
    version="0.0.1",
    description="Check charging app",
    executables=executables,
    packages=find_packages(
        include=[],
        exclude=[]
    )
)
