import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.

build_exe_options = {"packages": ["pyttsx3"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="BASKET_WITH_YAFAI",
    version="0.1",
    description="THIS IS MY FIRST APP. I CREATED IN MY HOLIDAYS AFTER 12TH. DATE: 14-06-2024",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)
