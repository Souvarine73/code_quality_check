"""
Script para análisis de calidad de código en Python usando
black, pylint, flake8, vulture y radon.

Este script automatiza la ejecución de herramientas de
análisis de código para verificar formato, calidad, estilo
y detectar código no utilizado.
"""

import subprocess
import sys

# Directorio a analizar
PROJECT_DIR = r".\code_quality_check.py"

# Comandos de análisis
COMMANDS = [
    [sys.executable, "-m", "black", PROJECT_DIR],  # Formateo de código
    [sys.executable, "-m", "pylint", PROJECT_DIR],  # Calidad de código
    [sys.executable, "-m", "flake8", PROJECT_DIR],  # Estilo de código
    [sys.executable, "-m", "vulture", PROJECT_DIR],  # Código no utilizado
    [sys.executable, "-m", "radon", "cc", PROJECT_DIR, "-a"],  # Complejidad ciclomática
]


def error_pylint(result: subprocess.CompletedProcess, command: list[str]) -> None:
    """
    Maneja los errores específicos de Pylint.

    Args:
        result (subprocess.CompletedProcess): Resultado de la ejecución del comando.
    Returns:
        None
    """
    if result.returncode >= 32:
        print(f"❗ Error crítico en {' '.join(command)}\n")
    elif result.returncode > 0:
        print("🚩 Pylint encontró advertencias o problemas de estilo\n")
    else:
        print("✅ Pylint: No se encontraron errores\n")


def error_black(result: subprocess.CompletedProcess, command: list[str]) -> None:
    """
    Maneja los errores específicos de Black.

    Args:
        result (subprocess.CompletedProcess): Resultado de la ejecución del comando.
        command (list[str]): Comando ejecutado.
    Returns:
        None
    """
    black_return_codes = {
        0: "✅ Código ya formateado correctamente.\n",
        1: "✍️ Se realizaron cambios en el formato del código.\n",
        2: "❌ Error de sintaxis en el archivo.\n",
        123: "🚨 Error interno de black.\n",
        124: "⏱️ Timeout: El análisis superó el tiempo de espera.\n",
        125: "🚫 Error al acceder al archivo o directorio.\n",
    }

    if result.returncode in black_return_codes:
        print(f"🔲 {black_return_codes[result.returncode]}")
    else:
        print(f"🚩 Error inesperado en {' '.join(command)}\n")


def error_flake8(result: subprocess.CompletedProcess, command: list[str]) -> None:
    """
    Maneja los errores específicos de Flake8.

    Args:
        result (subprocess.CompletedProcess): Resultado de la ejecución del comando.
        command (list[str]): Comando ejecutado.
    Returns:
        None
    """
    flake8_return_codes = {
        0: "✅ El código está limpio: sin errores de estilo.\n",
        1: "⚠️ Se encontraron errores o advertencias.\n",
    }
    if result.returncode in flake8_return_codes:
        print(f"🔲 {flake8_return_codes[result.returncode]}")
    else:
        print(f"🚩 Error de ejecucion en {' '.join(command)}\n")


def error_vulture(result: subprocess.CompletedProcess, command: list[str]) -> None:
    """
    Maneja los errores específicos de Vulture.

    Args:
        result (subprocess.CompletedProcess): Resultado de la ejecución del comando.
        command (list[str]): Comando ejecutado.
    Returns:
        None
    """
    vulture_return_codes = {
        0: "✅ No se encontraron código no utilizado.\n",
        1: "⚠️ Se encontró código no utilizado.\n",
        2: "❌ Error en la ejecución de Vulture.\n",
    }
    if result.returncode in vulture_return_codes:
        print(f"🔲 {vulture_return_codes[result.returncode]}")
    else:
        print(f"🚩 Error de ejecucion en {' '.join(command)}\n")


def error_radon(result: subprocess.CompletedProcess, command: list[str]) -> None:
    """
    Maneja los errores específicos de Radon.

    Args:
        result (subprocess.CompletedProcess): Resultado de la ejecución del comando.
        command (list[str]): Comando ejecutado.
    Returns:
        None
    """
    radon_return_codes = {
        0: "✅ Ejecución exitosa.\n",
        1: "⚠️ Error en la ejecución.\n",
        2: "❌ Error crítico.\n",
    }
    if result.returncode in radon_return_codes:
        print(f"🔲 {radon_return_codes[result.returncode]}")
    else:
        print(f"🚩 Error de ejecucion en {' '.join(command)}\n")


def error_handler(command: list[str]) -> None:
    """
    Maneja los errores en la ejecución de los comandos.

    Args:
        result (subprocess.CompletedProcess): Resultado de la ejecución del comando.
        command (list[str]): Comando a ejecutar para análisis.
    Returns:
        None
    """

    error_handlers_dict = {
        "pylint": error_pylint,
        "black": error_black,
        "flake8": error_flake8,
        "vulture": error_vulture,
        "radon": error_radon,
    }

    result = subprocess.run(
        command, capture_output=True, text=True, encoding="utf-8", check=False
    )

    # Mostrar salida estándar y de errores
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)

    print(f"🔙 Código de retorno: {result.returncode}")

    for tool, handler in error_handlers_dict.items():
        if tool in command:
            handler(result, command)
            break

def run_commands(command: list[str]) -> None:
    """
    Ejecuta un comando de análisis de código y muestra el resultado.

    Args:
        command (list[str]): Comando a ejecutar.

    Returns:
        None
    """
    print(f"🚀 Ejecutando comando: {' '.join(command)}")

    try:
        error_handler(command)
    except FileNotFoundError as e:
        print(f"❌ Error: Herramienta no encontrada - {e}")
    except subprocess.SubprocessError as e:
        print(f"⚠️ Error en la ejecución del comando: {e}")
    except Exception as ex:
        print(f"🚨 Error inesperado: {ex}")


if __name__ == "__main__":
    for cmd in COMMANDS:
        run_commands(cmd)
