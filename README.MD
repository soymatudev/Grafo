# Sistema de Grafo asi bien chonchamente perrones AF

Generamos un grafo a partir de las indicaciones dadas por un archivo de texto.

El formtato para nuestro archivo de texto es el siguiente:

### Formato

| Nodo 1 | Nodo 2 | Aristo / Camino / Etiqueta |
| :----- | :----- | :------------------------- |

### Ejemplo

| Nodo 1 | Nodo 2 | Aristo / Camino / Etiqueta |
| :----- | :----- | :------------------------- |
| **A**  | F      | 0                          |
| **A**  | r      | 1                          |
| **r**  | r      | 0                          |
| **r**  | r      | 1                          |
| **F**  | r      | 1                          |
| **F**  | F      | 0                          |

### Parametros

```bash
--edges # Archivo con las aritas y nodos
--max-edges # Cantidad de aristas por grafo
--inicial # Estado (nodo) inicial (por defecto A)
--finales # Estados (nodos) finales (por defecto F)
```

```bash
python3 grafo.py --edges a.txt --inicial q1 --finales q1 q3 # Ej. 1
python3 grafo.py --edges b.txt --inicial A --finales A B C # Ej. 2
```

### Depedencias

| Rol            | Tecnología | Propósito Específico                                                                                    |
| :------------- | :--------- | :------------------------------------------------------------------------------------------------------ |
| **Argumentos** | argparse   | Módulo estándar de Python para analizar argumentos de línea de comandos.                                |
| **Grafos**     | networkx   | Librería principal para la creación, manipulación y estudio de estructuras de grafos (redes complejas). |
| **Graficos**   | matplotlib | Librería estándar para trazar gráficos y, en este caso, se usa para dibujar y guardar el grafo.         |

### Instalación

1.  Instala las dependencias del proyecto:

```bash
sudo pip install argparse networkx matplotlib
```
