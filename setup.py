import sys
from cx_Freeze import setup, Executable

# Remplacez "main.py" par le nom de votre script principal
target = Executable(script="main.py", base="Win32GUI")

# Options supplémentaires si nécessaire
# build_exe_options = {}

setup(
    name="TNS",
    version="1.0",
    description="Calcul de la transformée de Fourier discrète",
    executables=[target],
    options={
        "build_exe": {
            "includes": ["TNS2"],  # Ajoutez d'autres modules requis ici
            # "options": build_exe_options
        }
    }
)
