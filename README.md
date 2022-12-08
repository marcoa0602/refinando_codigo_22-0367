# refinando_codigo_22-0367

# **Introducción**

En este repositorio se hará el ejercicio de "Refinando código" de la actividad PP5 - Calidad y archivos.
Los objetivos de este es limpiar el código usando herramientas como pylint y autopep8., y subirlo a un repositiorio de GitHub.

# **Refactorización**

El primer paso fue crear la función que convierte el archivo externo a una lista usando herramientas como with open() y se guardó en una variable que luego es retornada al usuario. Luego de esto se hizo la segunda función que toma como parametro la variable de la primera función, y luego sumo todos los valores de la lista. La tercera función es la principal que llama a las dos funciones anteriores e imprime el resultado.

# **Limpieza**
Se uso pylint para conseguir una puntuación de mi trabajo y los errores que se deberían arreglar. La mayoría de estos errores eran agregar docstrings a las funciones y agregar datos como el encoding al abrir el archivo. Al acabar con esto, use autopep8 para formatear el trabajo de ese modo, y luego copié el resultado.

# **Gestión de errores**
**Control de errores**

En la ejecución de código, los errores que más salieron fueron al usar 'with open()' para abrir el archivo con los precios que luego fue arreglado al cambiar el formato de la función y algunos errores de indentación. Además de esto, otro error que encontre fue en la creación de la función principal 'main()' en la que no imprimía la respuesta correcta, este fue arreglado al hacer que la segunda función 'total()' coja como parámetro la primera función 'costs_list()'.

**Pruebas unitarias**

Todas estas pruebas fueron hecha con la herramienta pytest. Las primera prueba utilizada fue para comprobar que la lista de precios sea correcta. La segunda prueba fue para confirmar que el costo total sea correcto. La última prueba se uso para cofnirmar que la función principal no devuelva ningún otro dato excepto el resultado de las dos funciones anteriores.

# **Control de versiones**
Link de GitHub: https://github.com/marcoa0602/refinando_codigo_22-0367.git
![Alt text](Screenshot%202022-12-08%20112032.png)
