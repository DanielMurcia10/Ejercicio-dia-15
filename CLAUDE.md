# CLAUDE.md — Gestión de Empleados

## Descripción del proyecto
Aplicación en Python para gestionar empleados: agregar, listar, buscar, editar y eliminar registros.
Los datos se guardan en un archivo JSON local (`empleados.json`). No usa base de datos ni librerías externas.

## Estructura de archivos
| Archivo | Responsabilidad |
|---|---|
| `main.py` | Punto de entrada. Solo arranca la aplicación; no contiene lógica. |
| `interfaz.py` | Todo lo que ve el usuario: menús, `input()`, `print()` y mensajes. |
| `employee.py` | Clase `Empleado`: atributos, validaciones y conversión a/desde diccionario. |
| `funciones.py` | Lógica del programa: cargar y guardar el JSON, agregar, buscar, editar y eliminar empleados. |
| `empleados.json` | Datos persistentes. Es una lista de objetos, un objeto por empleado. |

## Cómo ejecutar
```bash
python main.py
```

## Reglas de arquitectura (respétalas siempre)
- **Separación de capas:** `interfaz.py` nunca lee ni escribe `empleados.json` directamente; siempre llama a `funciones.py`.
- `funciones.py` no usa `input()` ni `print()`. Devuelve valores o lanza excepciones, y la interfaz decide qué mostrar.
- `employee.py` no importa nada de `interfaz.py` ni de `funciones.py`.
- La estructura de cada empleado en el JSON la define la clase `Empleado`. Si agregas o cambias un campo, actualiza la clase y los métodos de conversión a diccionario al mismo tiempo.
- No cambies los nombres de campos existentes en `empleados.json` sin avisar, porque rompe los datos guardados.

## Estilo de código
- Python 3.10 o superior.
- Nombres de variables, funciones y comentarios en **español** (`agregar_empleado`, `buscar_por_id`).
- Nombres en `snake_case`; clases en `PascalCase`.
- Cada función nueva lleva un docstring corto que diga qué hace, qué recibe y qué devuelve.
- Funciones pequeñas: si una función pasa de ~30 líneas, divídela.

## Manejo del archivo JSON
- Abrir siempre con `encoding="utf-8"` y guardar con `json.dump(..., indent=4, ensure_ascii=False)` para que se vean bien las tildes y la ñ.
- Si `empleados.json` no existe o está vacío, trátalo como una lista vacía `[]`; no dejes que el programa se caiga.
- Captura `json.JSONDecodeError` y muestra un mensaje claro en lugar de un error técnico.

## Validaciones
- No permitir IDs duplicados.
- No aceptar campos obligatorios vacíos.
- Los valores numéricos (por ejemplo, salario) deben ser números positivos; si el usuario escribe texto, pedir el dato de nuevo en vez de cerrar el programa.

## Qué NO hacer
- No instalar librerías externas sin preguntar primero.
- No borrar ni sobrescribir `empleados.json` para hacer pruebas; usa una copia (`empleados_prueba.json`).
- No mezclar lógica y `print()` en el mismo archivo.
- No hacer cambios grandes en varios archivos a la vez sin explicar antes el plan.

## Al terminar cada cambio
1. Ejecutar `python main.py` y probar la opción modificada.
2. Explicar brevemente qué se cambió, en qué archivo y por qué (lo tengo que poder explicar en la revisión).
3. Sugerir un mensaje de commit en español, por ejemplo: `git commit -m "Agrega validación de ID duplicado"`.