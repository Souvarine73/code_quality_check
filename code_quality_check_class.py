"""
Script para análisis de calidad de código en Python usando
black, pylint, flake8, vulture y radon.

Este script automatiza la ejecución de herramientas de
análisis de código para verificar formato, calidad, estilo
y detectar código no utilizado.
"""

import subprocess
import sys


class CodeQualityChecker:
    """
    Clase para análisis de calidad de código en Python usando
    black, pylint, flake8, vulture y radon.
    """

    def __init__(self, project_dir: str):
        self.project_dir = project_dir
        self.commands = [
            [sys.executable, "-m", "black", self.project_dir],
            [sys.executable, "-m", "pylint", self.project_dir],
            [sys.executable, "-m", "flake8", self.project_dir],
            [sys.executable, "-m", "vulture", self.project_dir],
            [sys.executable, "-m", "radon", "cc", self.project_dir, "-a"],
        ]

    def run(self):
        """
        Ejecuta los comandos de análisis de calidad de código.

        Returns:
            None
        """
        for command in self.commands:
            self.run_command(command)

    def run_command(self, command: list[str]) -> None:
        """
        Ejecuta un comando y maneja los errores específicos de cada herramienta.

        Args:
            command (list[str]): Comando a ejecutar.

        Returns:
            None
        """
        print(f"🚀 Ejecutando comando: {' '.join(command)}")
        try:
            self.error_handler(command)
        except FileNotFoundError as e:
            print(f"❌ Error: Herramienta no encontrada - {e}")
        except subprocess.SubprocessError as e:
            print(f"⚠️ Error en la ejecución del comando: {e}")
        except Exception as ex:
            print(f"🚨 Error inesperado: {ex}")

    def error_handler(self, command: list[str]) -> None:
        """
        Maneja los errores en la ejecución de los comandos.

        Args:
            command (list[str]): Comando a ejecutar

        Returns:
            None
        """
        error_handlers = {
            "pylint": self.handle_pylint_error,
            "black": self.handle_black_error,
            "flake8": self.handle_flake8_error,
            "vulture": self.handle_vulture_error,
            "radon": self.handle_radon_error,
        }

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )

        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)

        print(f"🔙 Código de retorno: {result.returncode}")

        for tool, handler in error_handlers.items():
            if tool in command:
                handler(result, command)
                break

    def handle_pylint_error(
        self, result: subprocess.CompletedProcess, command: list[str]
    ) -> None:
        """
        Maneja los errores de Pylint.

        Args:
            result (subprocess.CompletedProcess): Resultado de la ejecución del comando.
            command (list[str]): Comando a ejecutar.

        Returns:
            None
        """
        if result.returncode >= 32:
            print(f"❗ Error crítico en {' '.join(command)}\n")
        elif result.returncode > 0:
            print("🚩 Pylint encontró advertencias o problemas de estilo\n")
        else:
            print("✅ Pylint: No se encontraron errores\n")

    def handle_black_error(
        self, result: subprocess.CompletedProcess, command: list[str]
    ) -> None:
        """
        Maneja los errores de Black.

        Args:
            result (subprocess.CompletedProcess): Resultado de la ejecución del comando.
            command (list[str]): Comando a ejecutar.

        Returns:
            None
        """
        messages = {
            0: "✅ Código ya formateado correctamente.\n",
            1: "✍️ Se realizaron cambios en el formato del código.\n",
            2: "❌ Error de sintaxis en el archivo.\n",
            123: "🚨 Error interno de black.\n",
            124: "⏱️ Timeout: El análisis superó el tiempo de espera.\n",
            125: "🚫 Error al acceder al archivo o directorio.\n",
        }
        message = messages.get(
            result.returncode, f"🚩 Error inesperado en {' '.join(command)}\n"
        )
        print(f"🔲 {message}")

    def handle_flake8_error(
        self, result: subprocess.CompletedProcess, command: list[str]
    ) -> None:
        """
        maneja los errores de Flake8.

        Args:
            result (subprocess.CompletedProcess): Resultado de la ejecución del comando.
            command (list[str]): Comando a ejecutar.

        Returns:
            None
        """
        messages = {
            0: "✅ El código está limpio: sin errores de estilo.\n",
            1: "⚠️ Se encontraron errores o advertencias.\n",
        }
        message = messages.get(
            result.returncode, f"🚩 Error de ejecucion en {' '.join(command)}\n"
        )
        print(f"🔲 {message}")

    def handle_vulture_error(
        self, result: subprocess.CompletedProcess, command: list[str]
    ) -> None:
        """
        Maneja los errores de Vulture.

        Args:
            result (subprocess.CompletedProcess): Resultado de la ejecución del comando.
            command (list[str]): Comando a ejecutar.

        Returns:
            None
        """
        messages = {
            0: "✅ No se encontraron código no utilizado.\n",
            1: "⚠️ Se encontró código no utilizado.\n",
            2: "❌ Error en la ejecución de Vulture.\n",
        }
        message = messages.get(
            result.returncode, f"🚩 Error de ejecucion en {' '.join(command)}\n"
        )
        print(f"🔲 {message}")

    def handle_radon_error(
        self, result: subprocess.CompletedProcess, command: list[str]
    ) -> None:
        """
        Maneja los errores de Radon.

        Args:
            result (subprocess.CompletedProcess): Resultado de la ejecución del comando.
            command (list[str]): Comando a ejecutar.

        Returns:
            None
        """
        messages = {
            0: "✅ Ejecución exitosa.\n",
            1: "⚠️ Error en la ejecución.\n",
            2: "❌ Error crítico.\n",
        }
        message = messages.get(
            result.returncode, f"🚩 Error de ejecucion en {' '.join(command)}\n"
        )
        print(f"🔲 {message}")


if __name__ == "__main__":
    checker = CodeQualityChecker(r"./code_quality_check_class.py")
    checker.run()
