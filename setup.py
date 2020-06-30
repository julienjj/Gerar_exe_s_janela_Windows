from cx_Freeze import setup, Executable

setup(name = "reandurllib" ,
      version = "0.1" ,
      description = "" ,
      executables = [Executable("Seu_Código.py",base = "Win32GUI")])
