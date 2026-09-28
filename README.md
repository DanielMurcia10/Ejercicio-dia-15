# Ejercicio-dia-15
1. Separación de capas ❌ No cumple
- main.py debería solo arrancar la aplicación, pero tiene todo el menú (Ejecutar_sistema, unas 90 líneas) con sus print().
- funciones.py usa print() en obtener_empleado_por_id (funciones.py:10) y en buscar_empleado_por_id, que además pide datos con interfaz._pedir_entero. También importa interfaz.
- interfaz.pedir_cambio_empleado cambia los datos del empleado directamente, cuando esa lógica debería estar en funciones.py.
- ✅ interfaz.py no toca el JSON y employee.py no importa nada.

2. La clase Empleado define la estructura ⚠️ Cumple a medias
- La clase define los campos, pero no tiene validaciones ni métodos para convertir a diccionario y desde diccionario. Hoy se usa vars(e) y Empleado(**dato) en funciones.py.

3. Estilo de código ⚠️ Cumple a medias
- ✅ Los nombres y comentarios están en español.
- ❌ AnioIngreso, TiempoTrabajando y Ejecutar_sistema no están en snake_case. Cambiar los dos primeros rompería los datos guardados en empleados.json, así que según tu regla hay que avisar antes.
- ❌ Ninguna función tiene docstring, solo comentarios #.
- ❌ Hay funciones de más de 30 líneas: Ejecutar_sistema, pedir_cambio_empleado y pedir_datos_nuevo_empleado.

4. Manejo del JSON ❌ No cumple
- Los open() no usan encoding="utf-8".
- Se guarda con indent=2 y sin ensure_ascii=False.
- ✅ Si el archivo no existe, el programa lo maneja.
- ❌ Si el archivo está vacío o dañado, el programa se cae porque no se captura json.JSONDecodeError.

5. Validaciones ⚠️ Cumple a medias
- ✅ No acepta textos vacíos y vuelve a pedir el dato si escribes texto donde va un número.
- ❌ _pedir_decimal acepta salarios, bonos y horas negativos, y los enteros aceptan 0.
- ❌ No hay control de IDs duplicados al cargar, y empleados.json ya tiene dos registros con id: 1.