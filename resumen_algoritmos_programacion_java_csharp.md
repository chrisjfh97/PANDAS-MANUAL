# Resumen teórico: Algoritmos y Estructuras de Datos

Este archivo cubre los puntos 1 y 2 del temario. La programación práctica en Java y C#.NET se estudia por separado.

### Guía visual

- <span style="color:#1976D2"><strong>Definición:</strong></span> concepto que debes poder explicar.
- <span style="color:#2E7D32"><strong>Uso o ventaja:</strong></span> cuándo conviene aplicarlo.
- <span style="color:#C77700"><strong>Comparación:</strong></span> diferencia que debes recordar.
- <span style="color:#D32F2F"><strong>Atención:</strong></span> error, límite o riesgo importante.

Los bloques **Java** y **C#.NET** utilizan resaltado sintáctico al abrir la vista previa de Markdown. Salvo que se muestre una clase completa, son fragmentos para colocar dentro de una clase o método; cada bloque incluye los `import` o `using` que requiere.

## 1. Aspectos básicos sobre algoritmos

### 1.1 Definición de algoritmo

<span style="color:#1976D2"><strong>Definición:</strong></span> un **algoritmo** es una secuencia finita, ordenada y precisa de pasos que transforma datos de entrada en resultados para resolver un tipo de problema.

Propiedades esenciales:

- **Entrada:** datos que recibe.
- **Salida:** resultados que produce.
- **Finitud:** termina después de una cantidad limitada de pasos.
- **Precisión:** cada instrucción es clara y no ambigua.
- **Corrección:** produce el resultado esperado para toda entrada válida.
- **Generalidad:** resuelve una clase de casos, no solo un ejemplo.
- **Eficiencia:** utiliza razonablemente tiempo y memoria.

Un algoritmo puede describirse mediante lenguaje natural, pseudocódigo, diagramas de flujo o código. El **pseudocódigo** suele ser la opción más útil para diseñar porque expresa la lógica sin depender de la sintaxis de un lenguaje.

| Parte | Pregunta que responde |
|---|---|
| Precondición | ¿Qué debe cumplirse antes de comenzar? |
| Entrada | ¿Qué datos recibe? |
| Proceso | ¿Cómo transforma los datos? |
| Salida | ¿Qué resultado produce? |
| Postcondición | ¿Qué debe ser verdadero al terminar? |

<span style="color:#C77700"><strong>Correcto no significa eficiente:</strong></span> dos algoritmos pueden producir el mismo resultado, pero uno puede necesitar mucho más tiempo o memoria.

<span style="color:#C77700"><strong>Algoritmo frente a programa:</strong></span> el algoritmo es la solución lógica e independiente del lenguaje; el programa es esa solución implementada en un lenguaje ejecutable.

```text
Entrada: tres notas
Proceso: sumarlas y dividir entre tres
Salida: promedio
```

#### Ejemplo completo: obtener el mayor de tres números

**Especificación:** recibe tres números y devuelve el mayor. Si hay valores iguales, devuelve ese mismo valor sin ningún tratamiento especial.

```text
mayor ← a
Si b > mayor
    mayor ← b
Fin Si
Si c > mayor
    mayor ← c
Fin Si
Devolver mayor
```

Prueba de escritorio con `a = 4`, `b = 9`, `c = 6`:

| Paso | Operación | Valor de `mayor` |
|---|---|---:|
| 1 | `mayor ← a` | 4 |
| 2 | `b > mayor` es verdadero | 9 |
| 3 | `c > mayor` es falso | 9 |

**Java:**

```java
static int encontrarMayor(int a, int b, int c) {
    int mayor = a;
    if (b > mayor) mayor = b;
    if (c > mayor) mayor = c;
    return mayor;
}
```

**C#.NET:**

```csharp
static int EncontrarMayor(int a, int b, int c)
{
    int mayor = a;
    if (b > mayor) mayor = b;
    if (c > mayor) mayor = c;
    return mayor;
}
```

### 1.2 Estructuras de los algoritmos

<span style="color:#1976D2"><strong>Idea central:</strong></span> todo algoritmo puede construirse combinando tres estructuras de control:

1. **Secuencia:** ejecuta instrucciones una después de otra. El orden importa porque un paso puede depender del anterior.
2. **Selección:** elige un camino según una condición verdadera o falsa. Puede ser simple, doble o múltiple.
3. **Repetición:** ejecuta instrucciones varias veces.
   - **Para (`for`):** cuando se conoce la cantidad de repeticiones.
   - **Mientras (`while`):** comprueba la condición antes de cada repetición; puede no ejecutarse.
   - **Hacer-mientras (`do-while`):** comprueba al final; se ejecuta al menos una vez.

| Estructura | Pregunta para elegirla | Ejemplo |
|---|---|---|
| Secuencia | ¿Solo debo ejecutar pasos en orden? | Calcular subtotal y después impuesto |
| Selección | ¿La acción depende de una condición? | Aprobar si la nota es al menos 70 |
| `for` | ¿Conozco cuántas veces repetir? | Recorrer un arreglo |
| `while` | ¿Repito mientras se cumpla algo? | Leer hasta recibir un dato válido |
| `do-while` | ¿Debe ejecutarse al menos una vez? | Mostrar un menú |

```text
Leer nota
Si nota >= 70
    Mostrar "Aprobado"
Si no
    Mostrar "Reprobado"
```

<span style="color:#D32F2F"><strong>Atención:</strong></span> las estructuras pueden anidarse, pero todo ciclo debe avanzar hacia su condición de terminación para evitar una repetición infinita.

Todo ciclo posee normalmente:

1. **Inicialización:** establece el estado inicial.
2. **Condición:** decide si continúa.
3. **Cuerpo:** realiza el trabajo.
4. **Actualización:** acerca el ciclo a su terminación.

```text
Para i ← 0 hasta longitud - 1
    Mostrar arreglo[i]
Fin Para
```

<span style="color:#D32F2F"><strong>Errores frecuentes:</strong></span> límites incorrectos (`<` frente a `<=`), olvidar actualizar la condición y acceder fuera del arreglo.

### 1.3 Técnicas para resolver problemas

Proceso recomendado:

1. Comprender el objetivo.
2. Identificar entradas, salidas, reglas y restricciones.
3. Dividir el problema en partes pequeñas.
4. Diseñar la solución con pseudocódigo o diagramas.
5. Probarla manualmente.
6. Implementarla.
7. Corregir errores.
8. Optimizar solo después de comprobar su corrección.

#### Del problema a la solución

1. **Especificar:** definir exactamente qué debe resolverse.
2. **Descomponer:** separar el problema en tareas pequeñas.
3. **Reconocer patrones:** identificar cálculos, decisiones, recorridos o búsquedas conocidos.
4. **Elegir estructuras:** seleccionar cómo organizar los datos.
5. **Diseñar:** escribir pasos independientes del lenguaje.
6. **Verificar:** justificar que los pasos siempre producen la salida correcta.

Un algoritmo es correcto cuando cumple su postcondición para todas las entradas que satisfacen la precondición. Para razonar sobre un ciclo se comprueba que:

- Empieza en un estado válido.
- Cada repetición conserva la lógica esperada.
- Progresa y finalmente termina.

Los casos de prueba deben incluir:

- Un caso normal.
- Valores mínimos, máximos y límites.
- Datos vacíos o repetidos, si son posibles.
- Entradas inválidas.

<span style="color:#2E7D32"><strong>Prueba de escritorio:</strong></span> simula el algoritmo a mano y registra el cambio de sus variables para comprobar la lógica antes de programar.

<span style="color:#C77700"><strong>Prueba frente a depuración:</strong></span> probar busca descubrir fallos; depurar localiza su causa y la corrige. Una prueba exitosa aumenta la confianza, pero no demuestra por sí sola que nunca existan errores.

### 1.4 Diagramas de flujo

<span style="color:#1976D2"><strong>Definición:</strong></span> un **diagrama de flujo** representa gráficamente el orden de ejecución de un algoritmo.

| Símbolo | Significado |
|---|---|
| Óvalo | Inicio o fin |
| Rectángulo | Proceso o cálculo |
| Rombo | Decisión |
| Paralelogramo | Entrada o salida |
| Flecha | Dirección del flujo |

Las decisiones se escriben como preguntas y sus salidas se identifican, por ejemplo, con “sí” y “no”. Los diagramas facilitan visualizar la lógica, pero se vuelven difíciles de mantener cuando el sistema es grande.

Reglas básicas:

- Mantener una dirección de flujo clara, normalmente de arriba hacia abajo.
- Conectar todos los símbolos mediante flechas.
- Etiquetar cada salida de una decisión.
- Evitar cruces innecesarios de líneas.
- Representar una sola acción principal en cada símbolo de proceso.

<span style="color:#C77700"><strong>Diagrama frente a pseudocódigo:</strong></span> ambos representan el mismo algoritmo. El diagrama facilita visualizar caminos; el pseudocódigo es más rápido de escribir y modificar.

```text
         Inicio
            │
       Leer promedio
            │
     ¿Promedio >= 70?
        /          \
      Sí            No
      │              │
 "Aprobado"    "Reprobado"
        \          /
             Fin
```

### 1.5 Diagramación modular

<span style="color:#1976D2"><strong>Definición:</strong></span> la **programación modular** divide un problema grande en módulos pequeños, cada uno con una responsabilidad concreta.

```text
Programa principal
├── Leer datos
├── Validar datos
├── Calcular resultado
└── Mostrar resultado
```

Un buen módulo posee:

- **Alta cohesión:** todos sus pasos colaboran en una sola tarea.
- **Bajo acoplamiento:** depende lo menos posible de otros módulos.
- Entradas y salidas claramente definidas.

El diseño **descendente** o *top-down* comienza con la tarea general y la divide progresivamente hasta obtener módulos simples. El programa principal debe mostrar la secuencia general y delegar los detalles.

Un módulo puede:

- Recibir datos mediante parámetros.
- Devolver un resultado.
- Llamar a otros módulos.
- Ocultar detalles internos que el resto del programa no necesita conocer.

<span style="color:#D32F2F"><strong>Atención:</strong></span> modularizar no significa crear métodos arbitrariamente pequeños; cada módulo debe representar una responsabilidad completa y comprensible.

<span style="color:#2E7D32"><strong>Ventajas:</strong></span> reduce la complejidad, evita duplicación y facilita comprensión, reutilización, pruebas y mantenimiento.

## 2. Algoritmos y estructuras de datos

<span style="color:#1976D2"><strong>Definición:</strong></span> una **estructura de datos** organiza información junto con las operaciones permitidas sobre ella.

<span style="color:#C77700"><strong>Criterio de elección:</strong></span> depende de la operación más frecuente: acceder, buscar, insertar, eliminar, ordenar o representar relaciones.

### Complejidad algorítmica

<span style="color:#1976D2"><strong>Notación O grande:</strong></span> describe cómo crece el consumo de tiempo o memoria al aumentar la entrada; no mide segundos exactos.

| Complejidad | Interpretación |
|---|---|
| O(1) | Costo constante |
| O(log n) | El problema se reduce en cada paso |
| O(n) | Se recorre la entrada una vez |
| O(n log n) | Rendimiento eficiente típico de ordenamiento |
| O(n²) | Se procesan muchas parejas de elementos |

Para evaluar una estructura o algoritmo se consideran el mejor caso, el promedio, el peor caso y la memoria auxiliar.

#### Búsqueda lineal y búsqueda binaria

La **búsqueda lineal** revisa los elementos uno por uno. Funciona aunque los datos no estén ordenados y cuesta O(n) en el peor caso.

La **búsqueda binaria** compara con el elemento central y descarta la mitad que no puede contener el valor. Cuesta O(log n), pero exige datos ordenados y acceso eficiente por índice.

```text
Buscar 23 en [4, 8, 15, 16, 23, 42]

Centro = 15 → 23 es mayor → descartar mitad izquierda
Centro = 23 → encontrado
```

| Búsqueda | Requisito | Peor caso | Conviene cuando |
|---|---|---:|---|
| Lineal | Ninguno | O(n) | Hay pocos datos o están desordenados |
| Binaria | Datos ordenados | O(log n) | Hay muchas consultas sobre datos ordenados |

**Java:**

```java
static int busquedaLineal(int[] datos, int objetivo) {
    for (int i = 0; i < datos.length; i++)
        if (datos[i] == objetivo) return i;
    return -1;
}

static int busquedaBinaria(int[] datos, int objetivo) {
    int izquierda = 0, derecha = datos.length - 1;
    while (izquierda <= derecha) {
        int medio = izquierda + (derecha - izquierda) / 2;
        if (datos[medio] == objetivo) return medio;
        if (datos[medio] < objetivo) izquierda = medio + 1;
        else derecha = medio - 1;
    }
    return -1;
}
```

**C#.NET:**

```csharp
static int BusquedaLineal(int[] datos, int objetivo)
{
    for (int i = 0; i < datos.Length; i++)
        if (datos[i] == objetivo) return i;
    return -1;
}

static int BusquedaBinaria(int[] datos, int objetivo)
{
    int izquierda = 0, derecha = datos.Length - 1;
    while (izquierda <= derecha)
    {
        int medio = izquierda + (derecha - izquierda) / 2;
        if (datos[medio] == objetivo) return medio;
        if (datos[medio] < objetivo) izquierda = medio + 1;
        else derecha = medio - 1;
    }
    return -1;
}
```

<span style="color:#D32F2F"><strong>Atención:</strong></span> ordenar una sola vez puede compensar si después se harán muchas búsquedas binarias; para una única búsqueda, el costo de ordenar podría no justificarse.

#### Estrategias comunes de diseño

- **Fuerza bruta:** prueba directamente las posibilidades. Es sencilla, pero puede ser costosa.
- **Divide y vencerás:** divide el problema, resuelve las partes y combina resultados; se usa en merge sort y quick sort.
- **Voraz o *greedy*:** elige en cada paso la mejor opción local; solo funciona correctamente cuando el problema posee la propiedad adecuada.
- **Recursividad:** expresa la solución en términos de instancias más pequeñas del mismo problema.

Estas estrategias no son estructuras de datos: son formas generales de construir algoritmos.

### 2.1 Arreglos, pilas y colas

#### Arreglos

<span style="color:#1976D2"><strong>Arreglo:</strong></span> almacena elementos del mismo tipo en posiciones contiguas identificadas por índices. El primer índice suele ser cero.

```text
Valores: [85, 90, 75, 100]
Índices:   0   1   2    3
```

- Acceso o modificación por índice: **O(1)**.
- Búsqueda no ordenada: **O(n)**.
- Inserción o eliminación en medio: **O(n)** por los desplazamientos.
- Ventaja: acceso directo y poco gasto adicional de memoria.
- Desventaja: tamaño normalmente fijo y movimientos costosos.

<span style="color:#2E7D32"><strong>Cuándo usarlo:</strong></span> cuando importa acceder rápidamente por posición y la cantidad de datos es conocida o cambia poco.

**Java:**

```java
static void recorrer(int[] datos, int cantidad) {
    for (int i = 0; i < cantidad; i++)
        System.out.println(datos[i]);
}

static int buscar(int[] datos, int cantidad, int objetivo) {
    for (int i = 0; i < cantidad; i++)
        if (datos[i] == objetivo) return i;
    return -1;
}

static int insertar(int[] datos, int cantidad, int valor) {
    if (cantidad == datos.length) return cantidad; // Sin espacio
    datos[cantidad] = valor;
    return cantidad + 1;
}

static int eliminar(int[] datos, int cantidad, int indice) {
    if (indice < 0 || indice >= cantidad) return cantidad;
    for (int i = indice; i < cantidad - 1; i++)
        datos[i] = datos[i + 1];
    return cantidad - 1;
}
```

**C#.NET:**

```csharp
using System;

static void Recorrer(int[] datos, int cantidad)
{
    for (int i = 0; i < cantidad; i++)
        Console.WriteLine(datos[i]);
}

static int Buscar(int[] datos, int cantidad, int objetivo)
{
    for (int i = 0; i < cantidad; i++)
        if (datos[i] == objetivo) return i;
    return -1;
}

static int Insertar(int[] datos, int cantidad, int valor)
{
    if (cantidad == datos.Length) return cantidad; // Sin espacio
    datos[cantidad] = valor;
    return cantidad + 1;
}

static int Eliminar(int[] datos, int cantidad, int indice)
{
    if (indice < 0 || indice >= cantidad) return cantidad;
    for (int i = indice; i < cantidad - 1; i++)
        datos[i] = datos[i + 1];
    return cantidad - 1;
}
```

`cantidad` representa el **tamaño lógico**: cuántas posiciones contienen datos válidos. La capacidad física del arreglo no cambia; insertar y eliminar actualizan esa cantidad y desplazan elementos cuando es necesario.

#### Pilas

<span style="color:#1976D2"><strong>Pila:</strong></span> estructura lineal **LIFO**; el último elemento que entra es el primero que sale, como una pila de platos.

```text
        cima
          ↓
       ┌─────┐
pop ←  │  C  │  ← último en entrar
       ├─────┤
       │  B  │
       ├─────┤
       │  A  │
       └─────┘
          ↑
         push
```

- `push`: agregar en la parte superior.
- `pop`: retirar el elemento superior.
- `peek`: consultar el superior sin retirarlo.
- Operaciones principales: **O(1)**.
- Usos: deshacer acciones, historial, evaluación de expresiones, DFS y llamadas recursivas.

<span style="color:#D32F2F"><strong>Límite:</strong></span> solo se accede directamente al extremo superior; no está diseñada para retirar elementos intermedios.

**Java:**

```java
import java.util.Stack;

Stack<String> pila = new Stack<>();
pila.push("A");
pila.push("B");

if (!pila.isEmpty()) {
    System.out.println(pila.peek()); // B, no lo elimina
    System.out.println(pila.pop());  // B, sí lo elimina
}
```

**C#.NET:**

```csharp
using System;
using System.Collections.Generic;

Stack<string> pila = new Stack<string>();
pila.Push("A");
pila.Push("B");

if (pila.Count > 0)
{
    Console.WriteLine(pila.Peek()); // B, no lo elimina
    Console.WriteLine(pila.Pop());  // B, sí lo elimina
}
```

#### Colas

<span style="color:#1976D2"><strong>Cola:</strong></span> estructura lineal **FIFO**; el primer elemento que entra es el primero que sale, como una fila de atención.

```text
frente                                   final
  ↓                                        ↓
[ A ] → [ B ] → [ C ] → [ D ]  ← encolar
  │
  └── desencolar: sale A
```

- Encolar: agregar al final.
- Desencolar: retirar del frente.
- Consultar el frente.
- Operaciones principales: **O(1)** con una implementación adecuada.
- Usos: impresión, mensajería, planificación de tareas y BFS.

<span style="color:#C77700"><strong>Cola de prioridad:</strong></span> sale primero el elemento de mayor o menor prioridad, no necesariamente el más antiguo.

**Java:**

```java
import java.util.LinkedList;
import java.util.Queue;

Queue<String> cola = new LinkedList<>();
cola.offer("A");
cola.offer("B");

if (!cola.isEmpty()) {
    System.out.println(cola.peek()); // A, no lo elimina
    System.out.println(cola.poll()); // A, sí lo elimina
}
```

**C#.NET:**

```csharp
using System;
using System.Collections.Generic;

Queue<string> cola = new Queue<string>();
cola.Enqueue("A");
cola.Enqueue("B");

if (cola.Count > 0)
{
    Console.WriteLine(cola.Peek());    // A, no lo elimina
    Console.WriteLine(cola.Dequeue()); // A, sí lo elimina
}
```

| Estructura | Regla | Uso característico |
|---|---|---|
| Arreglo | Acceso por índice | Consultas frecuentes por posición |
| Pila | LIFO | Procesar primero lo más reciente |
| Cola | FIFO | Respetar el orden de llegada |

### 2.2 Árboles

<span style="color:#1976D2"><strong>Árbol:</strong></span> estructura jerárquica de nodos conectados, sin ciclos. Entre dos nodos existe un único camino; con `n` nodos posee `n - 1` aristas.

Conceptos:

- **Raíz:** nodo inicial.
- **Padre e hijo:** relación entre niveles.
- **Hoja:** nodo sin hijos.
- **Profundidad:** distancia desde la raíz hasta un nodo.
- **Altura:** camino más largo desde un nodo hasta una hoja.
- **Subárbol:** un nodo y todos sus descendientes.

#### Recorridos

- **Preorden:** raíz, izquierda, derecha. Útil para copiar o representar la estructura.
- **Inorden:** izquierda, raíz, derecha. En un ABB produce los valores ordenados.
- **Postorden:** izquierda, derecha, raíz. Útil para eliminar o calcular desde las hojas.
- **Por niveles:** visita nivel por nivel mediante una cola.

#### Tipos de árboles

- **Árbol binario:** cada nodo tiene como máximo dos hijos.
- **Árbol binario de búsqueda (ABB):** valores menores a la izquierda y mayores a la derecha. Buscar, insertar y eliminar cuestan O(log n) si está equilibrado, pero O(n) si se deforma como una lista.
- **Árbol N-ario:** cada nodo admite hasta N hijos. Representa carpetas, menús y organigramas.
- **Árbol AVL:** ABB autoequilibrado. El factor de equilibrio (altura izquierda menos derecha) debe ser -1, 0 o 1. Utiliza rotaciones y mantiene operaciones O(log n).
- **Árbol B:** almacena varias claves e hijos en cada nodo. Su poca altura reduce lecturas de disco; se usa en índices de bases de datos y sistemas de archivos.

**Árbol binario general:**

```text
          A
         / \
        B   C
         \   \
          D   E
```

Cada nodo tiene como máximo dos hijos, pero los valores no tienen que estar ordenados.

**Árbol binario de búsqueda:**

```text
        50
       /  \
     30    70
    / \    / \
   20 40  60 80
```

Los valores menores están a la izquierda y los mayores a la derecha.

**Árbol N-ario:**

```text
             Raíz
          /    |    \
         A     B     C
       /  \          |\
      D    E         F  G
```

Cada nodo puede tener más de dos hijos.

**Árbol AVL:**

```text
Antes de equilibrar:       Después de rotar:

        30                         20
       /                          /  \
      20                         10   30
     /
    10
```

La rotación reduce la diferencia de alturas sin perder el orden del ABB.

**Árbol B:**

```text
                 [ 30 | 60 ]
                /     |      \
       [10|20]     [40|50]    [70|80|90]
```

Cada nodo puede contener varias claves y conducir a varios hijos.

Representación mínima de un nodo binario:

**Java:**

```java
class Nodo {
    int valor;
    Nodo izquierdo;
    Nodo derecho;
}
```

**C#.NET:**

```csharp
class Nodo
{
    public int Valor { get; set; }
    public Nodo? Izquierdo { get; set; }
    public Nodo? Derecho { get; set; }
}
```

<span style="color:#C77700"><strong>Idea clave:</strong></span> un ABB ordena; un AVL además se equilibra; un árbol B optimiza almacenamiento secundario; un N-ario representa jerarquías con muchos hijos.

### 2.3 Grafos y dígrafos

<span style="color:#1976D2"><strong>Grafo:</strong></span> modela relaciones generales mediante:

- **Vértices:** entidades o nodos.
- **Aristas:** conexiones entre vértices.

Tipos de aristas:

- **No dirigidas:** la relación funciona en ambos sentidos.
- **Dirigidas:** poseen un origen y un destino; el grafo se llama **dígrafo**.
- **Ponderadas:** incluyen un costo como distancia, tiempo o precio.

```text
Grafo no dirigido:       Dígrafo:

A ─── B                  A ──→ B ──→ C
│     │                  ↑           │
C ─── D                  └───────────┘
```

**Grafo ponderado:**

```text
       5
 A ─────── B
 │         │
2│         │3
 │    4    │
 C ─────── D
```

Los números representan costos, distancias o tiempos.

Conceptos:

- **Camino:** secuencia de vértices conectados.
- **Ciclo:** camino que regresa al punto inicial.
- **Grado:** cantidad de aristas conectadas a un vértice. En un dígrafo se distingue entrada y salida.
- **Componente conexo:** grupo de vértices que pueden alcanzarse entre sí.

#### Representaciones

| Representación | Ventaja | Desventaja |
|---|---|---|
| Matriz de adyacencia | Comprobar una conexión cuesta O(1) | Consume O(V²) memoria |
| Lista de adyacencia | Consume O(V + E) memoria | Consultar una conexión depende de los vecinos |

<span style="color:#2E7D32"><strong>Elección:</strong></span> la matriz conviene en grafos densos; la lista, en grafos dispersos.

Ejemplo de matriz de adyacencia del grafo no dirigido anterior:

```text
    A B C D
A [ 0 1 1 0 ]
B [ 1 0 0 1 ]
C [ 1 0 0 1 ]
D [ 0 1 1 0 ]
```

`1` indica que existe una arista y `0` que no existe. En un grafo no dirigido, la matriz es simétrica.

Ejemplo de lista de adyacencia:

```text
A: [B, C]
B: [A, D]
C: [A, D]
D: [B, C]
```

**Java:**

```java
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

Map<String, List<String>> grafo = new HashMap<>();
grafo.put("A", Arrays.asList("B", "C"));
```

**C#.NET:**

```csharp
using System.Collections.Generic;

Dictionary<string, List<string>> grafo = new();
grafo["A"] = new List<string> { "B", "C" };
```

#### Recorridos

- **BFS o búsqueda en anchura:** usa una cola y explora por niveles. Encuentra el camino con menos aristas en un grafo no ponderado.
- **DFS o búsqueda en profundidad:** usa una pila o recursividad y explora una rama antes de retroceder. Sirve para detectar ciclos y explorar componentes.

<span style="color:#D32F2F"><strong>Atención:</strong></span> ambos cuestan **O(V + E)** con listas de adyacencia y deben marcar los vértices visitados para no repetir ciclos.

<span style="color:#C77700"><strong>Árbol frente a grafo:</strong></span> un árbol es jerárquico, conectado y sin ciclos; un grafo puede tener ciclos, varios caminos y componentes desconectados.

### 2.4 Métodos de ordenamiento

<span style="color:#1976D2"><strong>Ordenamiento:</strong></span> reorganiza datos según una clave. Los algoritmos se comparan mediante:

- **Tiempo:** mejor, promedio y peor caso.
- **Memoria auxiliar:** espacio adicional.
- **Estabilidad:** conserva el orden relativo de elementos con la misma clave.
- **Adaptabilidad:** aprovecha si los datos ya están parcialmente ordenados.

| Algoritmo | Funcionamiento | Mejor | Promedio / peor | Estable | Memoria auxiliar |
|---|---|---:|---:|---|---:|
| Burbuja | Intercambia vecinos desordenados | O(n)* | O(n²) | Sí | O(1) |
| Selección | Busca el menor y lo coloca al inicio | O(n²) | O(n²) | No, normalmente | O(1) |
| Inserción | Inserta cada elemento en la parte ordenada | O(n) | O(n²) | Sí | O(1) |
| Merge sort | Divide y mezcla partes ordenadas | O(n log n) | O(n log n) | Sí | O(n) |
| Quick sort | Divide alrededor de un pivote | O(n log n) | O(n log n) / O(n²) | No, normalmente | O(log n)** |

\* Burbuja alcanza O(n) si se detiene al no efectuar intercambios.  
\** Espacio promedio de la pila recursiva; puede llegar a O(n) en el peor caso.

Ideas para recordar:

- **Burbuja:** el mayor “sube” al final en cada pasada.
- **Selección:** realiza pocas permutas, pero siempre muchas comparaciones.
- **Inserción:** funciona como ordenar cartas; es bueno para pocos datos o datos casi ordenados.
- **Merge sort:** rendimiento predecible y estable, a cambio de memoria adicional.
- **Quick sort:** suele ser rápido, pero depende de una buena elección del pivote.

#### Implementaciones

##### Burbuja

**Java:**

```java
static void burbuja(int[] datos) {
    for (int i = 0; i < datos.length - 1; i++) {
        boolean cambio = false;
        for (int j = 0; j < datos.length - 1 - i; j++) {
            if (datos[j] > datos[j + 1]) {
                int temporal = datos[j];
                datos[j] = datos[j + 1];
                datos[j + 1] = temporal;
                cambio = true;
            }
        }
        if (!cambio) break;
    }
}
```

**C#.NET:**

```csharp
static void Burbuja(int[] datos)
{
    for (int i = 0; i < datos.Length - 1; i++)
    {
        bool cambio = false;
        for (int j = 0; j < datos.Length - 1 - i; j++)
        {
            if (datos[j] > datos[j + 1])
            {
                int temporal = datos[j];
                datos[j] = datos[j + 1];
                datos[j + 1] = temporal;
                cambio = true;
            }
        }
        if (!cambio) break;
    }
}
```

La bandera `cambio` permite terminar en O(n) si el arreglo ya está ordenado.

##### Inserción

**Java:**

```java
static void insercion(int[] datos) {
    for (int i = 1; i < datos.length; i++) {
        int actual = datos[i];
        int j = i - 1;
        while (j >= 0 && datos[j] > actual) {
            datos[j + 1] = datos[j];
            j--;
        }
        datos[j + 1] = actual;
    }
}
```

**C#.NET:**

```csharp
static void Insercion(int[] datos)
{
    for (int i = 1; i < datos.Length; i++)
    {
        int actual = datos[i];
        int j = i - 1;
        while (j >= 0 && datos[j] > actual)
        {
            datos[j + 1] = datos[j];
            j--;
        }
        datos[j + 1] = actual;
    }
}
```

La parte izquierda del arreglo permanece ordenada; cada elemento se desplaza hasta encontrar su posición.

##### Merge sort

**Java:**

```java
static void mergeSort(int[] datos) {
    mergeSort(datos, 0, datos.length - 1);
}

static void mergeSort(int[] datos, int inicio, int fin) {
    if (inicio >= fin) return;
    int medio = inicio + (fin - inicio) / 2;
    mergeSort(datos, inicio, medio);
    mergeSort(datos, medio + 1, fin);
    mezclar(datos, inicio, medio, fin);
}

static void mezclar(int[] datos, int inicio, int medio, int fin) {
    int[] temporal = new int[fin - inicio + 1];
    int i = inicio, j = medio + 1, k = 0;

    while (i <= medio && j <= fin)
        temporal[k++] = datos[i] <= datos[j]
                ? datos[i++] : datos[j++];
    while (i <= medio) temporal[k++] = datos[i++];
    while (j <= fin) temporal[k++] = datos[j++];

    for (k = 0; k < temporal.length; k++)
        datos[inicio + k] = temporal[k];
}
```

**C#.NET:**

```csharp
static void MergeSort(int[] datos)
{
    MergeSort(datos, 0, datos.Length - 1);
}

static void MergeSort(int[] datos, int inicio, int fin)
{
    if (inicio >= fin) return;
    int medio = inicio + (fin - inicio) / 2;
    MergeSort(datos, inicio, medio);
    MergeSort(datos, medio + 1, fin);
    Mezclar(datos, inicio, medio, fin);
}

static void Mezclar(int[] datos, int inicio, int medio, int fin)
{
    int[] temporal = new int[fin - inicio + 1];
    int i = inicio, j = medio + 1, k = 0;

    while (i <= medio && j <= fin)
        temporal[k++] = datos[i] <= datos[j]
            ? datos[i++] : datos[j++];
    while (i <= medio) temporal[k++] = datos[i++];
    while (j <= fin) temporal[k++] = datos[j++];

    for (k = 0; k < temporal.Length; k++)
        datos[inicio + k] = temporal[k];
}
```

La división llega a subarreglos de un elemento; `mezclar` los combina ordenadamente usando memoria temporal O(n).

##### Quick sort

**Java:**

```java
static void quickSort(int[] datos) {
    quickSort(datos, 0, datos.length - 1);
}

static void quickSort(int[] datos, int inicio, int fin) {
    if (inicio >= fin) return;
    int pivote = particionar(datos, inicio, fin);
    quickSort(datos, inicio, pivote - 1);
    quickSort(datos, pivote + 1, fin);
}

static int particionar(int[] datos, int inicio, int fin) {
    int pivote = datos[fin];
    int i = inicio - 1;
    for (int j = inicio; j < fin; j++) {
        if (datos[j] <= pivote) {
            i++;
            intercambiar(datos, i, j);
        }
    }
    intercambiar(datos, i + 1, fin);
    return i + 1;
}

static void intercambiar(int[] datos, int a, int b) {
    int temporal = datos[a];
    datos[a] = datos[b];
    datos[b] = temporal;
}
```

**C#.NET:**

```csharp
static void QuickSort(int[] datos)
{
    QuickSort(datos, 0, datos.Length - 1);
}

static void QuickSort(int[] datos, int inicio, int fin)
{
    if (inicio >= fin) return;
    int pivote = Particionar(datos, inicio, fin);
    QuickSort(datos, inicio, pivote - 1);
    QuickSort(datos, pivote + 1, fin);
}

static int Particionar(int[] datos, int inicio, int fin)
{
    int pivote = datos[fin];
    int i = inicio - 1;
    for (int j = inicio; j < fin; j++)
    {
        if (datos[j] <= pivote)
        {
            i++;
            Intercambiar(datos, i, j);
        }
    }
    Intercambiar(datos, i + 1, fin);
    return i + 1;
}

static void Intercambiar(int[] datos, int a, int b)
{
    int temporal = datos[a];
    datos[a] = datos[b];
    datos[b] = temporal;
}
```

La partición deja valores menores o iguales antes del pivote y mayores después. Elegir siempre el último elemento es sencillo, pero puede provocar el peor caso O(n²) con entradas desfavorables.

### 2.5 Listas enlazadas

<span style="color:#1976D2"><strong>Lista enlazada:</strong></span> almacena datos en nodos conectados mediante referencias. Los nodos no necesitan estar contiguos en memoria.

- Acceso por posición: **O(n)**, porque se recorren enlaces desde la cabeza.
- Búsqueda: **O(n)**.
- Inserción o eliminación: **O(1)** si ya se conoce el nodo adecuado; localizarlo puede costar O(n).
- <span style="color:#2E7D32"><strong>Ventaja:</strong></span> tamaño dinámico y ausencia de desplazamientos masivos.
- <span style="color:#D32F2F"><strong>Desventaja:</strong></span> memoria adicional y falta de acceso directo por índice.

Tipos:

- **Simple:** cada nodo apunta al siguiente; solo avanza en una dirección.
- **Doble:** cada nodo apunta al anterior y al siguiente; permite recorrer en ambos sentidos.
- **Circular:** el último apunta al primero; sirve para turnos repetitivos y no termina en `null`.
- **Doblemente circular:** combina navegación bidireccional con conexión entre primero y último.

```text
Simple:

cabeza → [10|•] → [20|•] → [30|null]

Doble:

null ← [10] ⇄ [20] ⇄ [30] → null

Circular simple:

       ┌─────────────────┐
       ↓                 │
     [10] → [20] → [30] ┘

Doblemente circular:

       ┌───────────────────┐
       ↓                   │
     [10] ⇄ [20] ⇄ [30]
       │                   ↑
       └───────────────────┘
```

Representación de un nodo simple:

**Java:**

```java
class ListaSimple {
    private static class Nodo {
        int valor;
        Nodo siguiente;

        Nodo(int valor) {
            this.valor = valor;
        }
    }

    private Nodo cabeza;

    void insertarFinal(int valor) {
        Nodo nuevo = new Nodo(valor);
        if (cabeza == null) {
            cabeza = nuevo;
            return;
        }
        Nodo actual = cabeza;
        while (actual.siguiente != null)
            actual = actual.siguiente;
        actual.siguiente = nuevo;
    }

    boolean buscar(int valor) {
        for (Nodo actual = cabeza; actual != null;
                actual = actual.siguiente)
            if (actual.valor == valor) return true;
        return false;
    }

    boolean eliminar(int valor) {
        if (cabeza == null) return false;
        if (cabeza.valor == valor) {
            cabeza = cabeza.siguiente;
            return true;
        }
        Nodo actual = cabeza;
        while (actual.siguiente != null
                && actual.siguiente.valor != valor)
            actual = actual.siguiente;
        if (actual.siguiente == null) return false;
        actual.siguiente = actual.siguiente.siguiente;
        return true;
    }

    void recorrer() {
        for (Nodo actual = cabeza; actual != null;
                actual = actual.siguiente)
            System.out.println(actual.valor);
    }
}
```

**C#.NET:**

```csharp
#nullable enable
using System;

class ListaSimple
{
    private class Nodo
    {
        public int Valor;
        public Nodo? Siguiente;

        public Nodo(int valor) { Valor = valor; }
    }

    private Nodo? cabeza;

    public void InsertarFinal(int valor)
    {
        Nodo nuevo = new Nodo(valor);
        if (cabeza is null)
        {
            cabeza = nuevo;
            return;
        }
        Nodo actual = cabeza;
        while (actual.Siguiente is not null)
            actual = actual.Siguiente;
        actual.Siguiente = nuevo;
    }

    public bool Buscar(int valor)
    {
        for (Nodo? actual = cabeza; actual is not null;
             actual = actual.Siguiente)
            if (actual.Valor == valor) return true;
        return false;
    }

    public bool Eliminar(int valor)
    {
        if (cabeza is null) return false;
        if (cabeza.Valor == valor)
        {
            cabeza = cabeza.Siguiente;
            return true;
        }
        Nodo actual = cabeza;
        while (actual.Siguiente is not null
               && actual.Siguiente.Valor != valor)
            actual = actual.Siguiente;
        if (actual.Siguiente is null) return false;
        actual.Siguiente = actual.Siguiente.Siguiente;
        return true;
    }

    public void Recorrer()
    {
        for (Nodo? actual = cabeza; actual is not null;
             actual = actual.Siguiente)
            Console.WriteLine(actual.Valor);
    }
}
```

La inserción al final y la búsqueda cuestan O(n) en esta versión. Insertar sería O(1) si la lista mantuviera también una referencia al último nodo. La eliminación enlaza el nodo anterior con el siguiente y no desplaza los demás datos.

| Necesidad | Elección |
|---|---|
| Acceso frecuente por índice | Arreglo |
| Inserciones al inicio | Lista simple |
| Recorrido en ambos sentidos | Lista doble |
| Turnos repetitivos | Lista circular |

### 2.6 Recursividad

<span style="color:#1976D2"><strong>Recursividad:</strong></span> resuelve un problema mediante llamadas a versiones más pequeñas del mismo problema.

Requiere:

- **Caso base:** resultado directo que detiene las llamadas.
- **Caso recursivo:** reduce el problema.
- **Progreso:** cada llamada debe acercarse al caso base.

```text
factorial(n):
    si n <= 1, devolver 1           ← caso base
    devolver n × factorial(n - 1)  ← caso recursivo
```

**Java:**

```java
static long factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
```

**C#.NET:**

```csharp
static long Factorial(int n)
{
    if (n <= 1) return 1;
    return n * Factorial(n - 1);
}
```

Cada llamada crea un marco en la pila con parámetros y variables propias. Al alcanzar el caso base, las llamadas regresan en orden inverso.

<span style="color:#D32F2F"><strong>Atención:</strong></span> una recursión sin terminación o demasiado profunda provoca un **desbordamiento de pila**.

<span style="color:#2E7D32"><strong>Cuándo usarla:</strong></span> en árboles, DFS, directorios y algoritmos de divide y vencerás, cuando expresa el problema con claridad y su profundidad es segura.

## Cuadro comparativo esencial

| Estructura | Regla o forma | Operación destacada | Uso principal |
|---|---|---|---|
| Arreglo | Posiciones contiguas | Acceso O(1) | Datos indexados |
| Lista enlazada | Nodos conectados | Inserción O(1)* | Tamaño dinámico |
| Pila | LIFO | `push/pop` O(1) | Retroceso y llamadas |
| Cola | FIFO | encolar/desencolar O(1) | Orden de llegada |
| ABB equilibrado | Menores izquierda, mayores derecha | Buscar O(log n) | Datos ordenados dinámicos |
| Grafo | Vértices y aristas | Recorrer O(V + E) | Relaciones y rutas |

\* Si ya se conoce el nodo; encontrarlo puede costar O(n).

## Repaso mínimo

1. Algoritmo = solución lógica; programa = implementación.
2. Un algoritmo correcto cumple su postcondición y siempre termina.
3. Control = secuencia, selección y repetición.
4. Modularidad = alta cohesión y bajo acoplamiento.
5. Lineal busca en O(n); binaria exige orden y busca en O(log n).
6. Arreglo = acceso rápido; lista = inserción flexible.
7. Pila = LIFO; cola = FIFO.
8. ABB ordena; AVL equilibra; B reduce accesos al disco.
9. Grafo relaciona; dígrafo añade dirección.
10. BFS usa cola; DFS usa pila o recursividad.
11. Los ordenamientos se comparan por tiempo, memoria y estabilidad.
12. Recursividad = caso base + reducción + progreso.
