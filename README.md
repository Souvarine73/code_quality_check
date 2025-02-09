# Code Quality Checker 🚀

## 📋 Descripción

**Code Quality Checker** es un script en Python que automatiza el análisis de calidad del código utilizando las herramientas más populares:

- **Black**: Para el formateo automático del código.
- **Pylint**: Para evaluar la calidad del código y detectar errores.
- **Flake8**: Para comprobar el estilo del código según PEP8.
- **Vulture**: Para identificar código no utilizado.
- **Radon**: Para medir la complejidad ciclomática del código.

Este script facilita la revisión del código de manera rápida y efectiva, mostrando mensajes claros sobre el estado del análisis. ✅❌⚠️

---

## 🚀 ¿Cómo usarlo?

### 1️⃣ **Requisitos Previos**
Asegúrate de tener instaladas las siguientes herramientas:

```bash
pip install black pylint flake8 vulture radon
```

### 2️⃣ **Ejecutar el Script**

```bash
python code_quality_check_class.py
```

El script analizará automáticamente el archivo especificado en su configuración.

### 3️⃣ **Personalización**
Si deseas analizar otro archivo o directorio, modifica la siguiente línea al final del script:

```python
checker = CodeQualityChecker(r"./ruta_al_archivo_o_directorio")
```

---

## 📊 Ejemplo de Salida

```bash
🚀 Ejecutando comando: black ./code_quality_check_class.py
All done! 
1 file left unchanged.

🔙 Código de retorno: 0
🔲 ✅ Código ya formateado correctamente.

🚀 Ejecutando comando: pylint ./code_quality_check_class.py
************* Module code_quality_check_class
code_quality_check_class.py:57:15: W0718: Catching too general exception Exception (broad-exception-caught)

------------------------------------------------------------------
Your code has been rated at 9.82/10 (previous run: 9.82/10, +0.00)


🔙 Código de retorno: 4
🚩 Pylint encontró advertencias o problemas de estilo

🚀 Ejecutando comando: flake8 ./code_quality_check_class.py
./code_quality_check_class.py:42:80: E501 line too long (80 > 79 characters)
./code_quality_check_class.py:105:80: E501 line too long (88 > 79 characters)
./code_quality_check_class.py:125:80: E501 line too long (88 > 79 characters)
./code_quality_check_class.py:151:80: E501 line too long (88 > 79 characters)
./code_quality_check_class.py:173:80: E501 line too long (88 > 79 characters)
./code_quality_check_class.py:196:80: E501 line too long (88 > 79 characters)

🔙 Código de retorno: 1
🔲 ⚠️ Se encontraron errores o advertencias.

🚀 Ejecutando comando: vulture ./code_quality_check_class.py
🔙 Código de retorno: 0
🔲 ✅ No se encontraron código no utilizado.

🚀 Ejecutando comando: radon cc ./code_quality_check_class.py -a
./code_quality_check_class.py
    M 60:4 CodeQualityChecker.error_handler - A
    M 40:4 CodeQualityChecker.run_command - A
    C 14:0 CodeQualityChecker - A
    M 98:4 CodeQualityChecker.handle_pylint_error - A
    M 30:4 CodeQualityChecker.run - A
    M 20:4 CodeQualityChecker.__init__ - A
    M 118:4 CodeQualityChecker.handle_black_error - A
    M 144:4 CodeQualityChecker.handle_flake8_error - A
    M 166:4 CodeQualityChecker.handle_vulture_error - A
    M 189:4 CodeQualityChecker.handle_radon_error - A

10 blocks (classes, functions, methods) analyzed.
Average complexity: A (2.2)

🔙 Código de retorno: 0
🔲 ✅ Ejecución exitosa.
```

Cada herramienta muestra resultados claros, utilizando iconos para una mejor visualización:
- ✅ Sin errores
- ⚠️ Advertencias o código no utilizado
- ❌ Errores críticos

---

## 🤝 Contribuciones

Si deseas mejorar este script:

1. Haz un fork del repositorio 📂
2. Crea una rama para tu feature `git checkout -b mi-feature` 🚀
3. Realiza un commit de tus cambios `git commit -m "Mejora: nueva funcionalidad"` ✍️
4. Haz push a la rama `git push origin mi-feature` ⬆️
5. Abre un Pull Request 📝

---

## ⚡ Licencia

Este proyecto está bajo la [MIT License].

---

¡Gracias por usar **Code Quality Checker**! 🚀🎯

