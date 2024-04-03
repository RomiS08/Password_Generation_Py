import sys

from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Password Generator",
    version="1.0",
    description="Simple Python application for generating the password",
    executables=[Executable("version2main.py", base=base, icon="app_icon.ico")],
    options={
        "build_exe": {
            "packages": ["secrets", "string", "tkinter", "tkinter.ttk"],
            "include_files": ["requirements.txt", "app_icon.ico"]
        }
    }
)
