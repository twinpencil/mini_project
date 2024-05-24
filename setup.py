import sys
from cx_Freeze import setup, Executable

build_exe_options = {"include_files": ["employee.ico", "database\database.py"]}
setup(
    name="ProManager",
    version="1.0",
    description="this my app ",
    options={"build_exe": build_exe_options},
    executables=[Executable("maintest.py", base=None,icon="employee.ico")],
)