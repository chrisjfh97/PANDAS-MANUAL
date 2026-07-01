# Tema 3. Programación en Java y C#.NET

Resumen organizado primero por Java y luego por C#.NET. Ambos bloques abarcan los mismos temas con programas completos.

> **Requisitos:** JDK 17 o posterior y .NET 8 SDK o posterior.

## Tabla de contenido

- [Parte I. Java](#parte-i-java)
  - [Java 3.1. Entorno de Java y NetBeans](#java-31-entorno-de-java-y-netbeans)
    - [Fundamentos básicos de Java](#fundamentos-básicos-de-java)
  - [Java 3.2. Procedimientos y funciones](#java-32-procedimientos-y-funciones)
  - [Java 3.3. Administración de clases](#java-33-administración-de-clases)
  - [Java 3.4. Acceso a medios de almacenamiento](#java-34-acceso-a-medios-de-almacenamiento)
  - [Java 3.5. Hilos y excepciones](#java-35-hilos-y-excepciones)
  - [Java 3.6. Formularios, informes, menús, proyectos y aplicaciones](#java-36-formularios-informes-menús-proyectos-y-aplicaciones)
- [Parte II. C#.NET](#parte-ii-cnet)
  - [C# 3.1. Entorno de C# y .NET](#c-31-entorno-de-c-y-net)
    - [Fundamentos básicos de C#](#fundamentos-básicos-de-c)
  - [C# 3.2. Procedimientos y funciones](#c-32-procedimientos-y-funciones)
  - [C# 3.3. Administración de clases](#c-33-administración-de-clases)
  - [C# 3.4. Acceso a medios de almacenamiento](#c-34-acceso-a-medios-de-almacenamiento)
  - [C# 3.5. Hilos y excepciones](#c-35-hilos-y-excepciones)
  - [C# 3.6. Formularios, informes, menús, proyectos y aplicaciones](#c-36-formularios-informes-menús-proyectos-y-aplicaciones)
- [Equivalencias rápidas](#equivalencias-rápidas)

# Parte I. Java

## Java 3.1. Entorno de Java y NetBeans

### JDK, JVM y proceso de ejecución

El **JDK** contiene el compilador y las herramientas. `javac` transforma un archivo `.java` en bytecode `.class`, que ejecuta la **JVM**.

```text
Archivo .java -> compilador javac -> bytecode .class -> JVM -> sistema operativo
```

- **JDK:** desarrollo, compilación y ejecución.
- **JVM:** ejecución del bytecode.
- **Classpath:** rutas de clases y bibliotecas.
- **Paquete:** agrupación de clases relacionadas.

#### Primer programa Java ejecutable

Guardar como `HolaJava.java` (el archivo debe tener el mismo nombre que la clase pública):

```java
public class HolaJava {
    public static void main(String[] args) {
        // Usa el primer argumento; si no existe, asigna un nombre predeterminado.
        String nombre = args.length > 0 ? args[0] : "estudiante";
        System.out.println("Hola, " + nombre + ". Java funciona correctamente.");
    }
}
```

Compilar y ejecutar desde una terminal:

```powershell
javac HolaJava.java
java HolaJava Ana
```

`main` es el punto de entrada y `String[] args` recibe argumentos de la terminal.

### NetBeans

NetBeans es un **IDE** que utiliza el JDK para editar, compilar, ejecutar y depurar.

Flujo básico:

1. Configurar el JDK en **Tools > Java Platforms**.
2. Elegir **File > New Project > Java Application**.
3. Crear paquetes y clases.
4. Usar **Run Project** para ejecutar o puntos de interrupción para depurar.

### Fundamentos básicos de Java

Los bloques pequeños de esta sección muestran una regla de sintaxis de forma aislada. El apartado **Programa Java con los fundamentos** reúne esas reglas en un archivo completo, compilable y ejecutable.

#### Estructura, nombres y comentarios

- Java distingue mayúsculas: `edad` y `Edad` son identificadores distintos.
- Cada instrucción termina normalmente en `;` y los bloques usan `{ }`.
- Clases: `PascalCase`; variables y métodos: `camelCase`; constantes: `MAYUSCULAS_CON_GUION`.
- Comentarios: `// una línea`, `/* varias líneas */` y `/** documentación Javadoc */`.
- Una clase `public` debe estar en un archivo con el mismo nombre.

#### Imports comunes

`java.lang` se importa automáticamente e incluye `String`, `Math`, `System` y tipos básicos. Los demás paquetes se importan antes de declarar la clase.

| Import | Uso |
|---|---|
| `java.util.Scanner` | Leer desde teclado |
| `java.util.ArrayList` / `List` | Listas dinámicas |
| `java.util.HashMap` / `Map` | Pares clave-valor |
| `java.util.HashSet` / `Set` | Valores únicos |
| `java.util.Arrays` / `Collections` | Operaciones sobre arreglos y colecciones |
| `java.util.Random` | Números pseudoaleatorios |
| `java.time.LocalDate` | Fechas sin hora |
| `java.nio.file.Files` / `Path` | Archivos y rutas |
| `java.io.*` | Flujos y excepciones de entrada/salida |

Se recomienda importar clases concretas y evitar `import paquete.*` cuando pueda ocultar el origen de los nombres.

#### Tipos y declaración de variables

| Tipo | Ejemplo | Uso |
|---|---|---|
| `byte`, `short`, `int`, `long` | `int edad = 20;` | Enteros de distinto rango |
| `float`, `double` | `double precio = 12.5;` | Decimales aproximados |
| `char` | `char inicial = 'A';` | Un carácter Unicode |
| `boolean` | `boolean activo = true;` | `true` o `false` |
| `String` | `String nombre = "Ana";` | Texto |
| Arreglo | `int[] notas = {80, 90};` | Tamaño fijo |
| Objeto | `Scanner lector = new Scanner(System.in);` | Instancia de una clase |

`long` usa sufijo `L` y `float` usa `F`: `long poblacion = 5_000_000L;`, `float tasa = 1.5F;`. Una constante local se declara con `final`: `final double IVA = 0.13;`. `var` permite inferencia local desde Java 10, pero sigue siendo tipado estático: `var total = 25.0;`.

Los tipos primitivos almacenan el valor. Las clases envolventes (`Integer`, `Double`, `Boolean`, etc.) permiten usar esos valores en colecciones y pueden contener `null`. Una referencia `null` no apunta a un objeto; llamar un método sobre ella produce `NullPointerException`.

#### Operadores y control de flujo

- Aritméticos: `+`, `-`, `*`, `/`, `%`.
- Comparación: `==`, `!=`, `<`, `<=`, `>`, `>=`.
- Lógicos: `&&`, `||`, `!`.
- Asignación: `=`, `+=`, `-=`, `*=`, `/=`.
- Incremento: `++`, `--`; ternario: `condicion ? valor1 : valor2`.
- Texto: se compara con `equals`, no con `==`; `equalsIgnoreCase` ignora mayúsculas.

`if`/`else` decide, `switch` elige entre casos, `for` repite con contador, `while` evalúa antes, `do-while` ejecuta al menos una vez y el `for-each` recorre colecciones. `break` termina el ciclo y `continue` pasa a la siguiente iteración.

#### Alcance, memoria y valores iniciales

El **alcance** indica dónde puede usarse una variable. Una variable local existe desde su declaración hasta el cierre de su bloque `{ }`; dos métodos no comparten sus variables locales. Un campo pertenece al objeto y un campo `static` pertenece a la clase.

Las variables locales deben inicializarse antes de usarse. Los campos reciben valores predeterminados: `0`, `0.0`, `false`, `\u0000` o `null`. Java administra la memoria con un recolector de basura, pero los archivos y conexiones deben cerrarse.

```java
int exterior = 10;
if (exterior > 0) {
    int interior = 20; // Solo existe dentro de este bloque.
    exterior += interior;
}
// interior ya no puede utilizarse aquí.
```

#### Números, conversiones y precisión

La división entre enteros descarta los decimales: `5 / 2` produce `2`; para obtener `2.5` se usa `5.0 / 2` o `(double) 5 / 2`. Una conversión **implícita** es segura, como `int` a `double`; una conversión **explícita** puede perder información: `int n = (int) 3.9;` produce `3`.

Para convertir texto se usan `Integer.parseInt`, `Long.parseLong` y `Double.parseDouble`. Estas funciones generan `NumberFormatException` si el texto es inválido, por lo que la entrada del usuario debe validarse. Para dinero y cálculos decimales exactos se prefiere `BigDecimal`, no `double`.

```java
String entrada = "125";
try {
    int numero = Integer.parseInt(entrada);
    System.out.println(numero * 2);
} catch (NumberFormatException error) {
    System.out.println("El valor no es un entero válido");
}
```

#### Cadenas y caracteres

`String` es inmutable: operaciones como `toUpperCase()` crean otra cadena. Métodos frecuentes: `length`, `isBlank`, `trim`, `contains`, `startsWith`, `substring`, `replace`, `split` y `equals`. Para muchas concatenaciones se usa `StringBuilder`.

```java
String nombre = "  Ana López  ";
String limpio = nombre.trim();
System.out.println(limpio.toUpperCase());
System.out.println("Ana".equals(limpio)); // false: compara el contenido completo.
```

#### Arreglos y colecciones

Los índices comienzan en `0`. Un arreglo tiene longitud fija (`arreglo.length`). Una `List` mantiene orden y permite repetidos; un `Set` conserva valores únicos; un `Map` relaciona claves únicas con valores. Los genéricos, como `List<String>`, restringen el tipo y evitan conversiones inseguras.

```java
int[] arreglo = new int[3];       // {0, 0, 0}
List<String> lista = new ArrayList<>();
lista.add("Java");
lista.set(0, "Java 17");
boolean existe = lista.contains("Java 17");
lista.remove("Java 17");
System.out.println(existe + " / tamaño: " + lista.size());
```

Acceder a un índice inexistente genera `ArrayIndexOutOfBoundsException` o `IndexOutOfBoundsException`. Antes de acceder, se comprueba `indice >= 0 && indice < tamaño`.

#### Métodos y paso de argumentos

Un método reúne instrucciones reutilizables. Su declaración contiene modificador, retorno, nombre y parámetros. `void` no retorna un resultado; los demás tipos requieren `return`. Java pasa todo **por valor**: con objetos se copia la referencia, de modo que puede modificarse el objeto, pero no reemplazar la variable del llamador.

```java
private static double promedio(int[] valores) {
    if (valores.length == 0) {
        throw new IllegalArgumentException("El arreglo está vacío");
    }
    int suma = 0;
    for (int valor : valores) suma += valor;
    return (double) suma / valores.length;
}
```

#### Clases, objetos y enums

Una clase agrupa estado y comportamiento. `new` llama al constructor y crea un objeto; `this` representa el objeto actual. Los campos suelen ser `private` y se exponen mediante métodos. Un `enum` limita una variable a opciones conocidas.

```java
enum Estado { ACTIVO, INACTIVO }

class Usuario {
    private final String nombre;
    private Estado estado;

    public Usuario(String nombre) {
        this.nombre = nombre;
        this.estado = Estado.ACTIVO;
    }

    public String getNombre() { return nombre; }
    public Estado getEstado() { return estado; }
}
```

#### Errores básicos que deben evitarse

- Comparar cadenas con `==` en vez de `equals`.
- Usar división entera cuando se esperan decimales.
- Confundir `arreglo.length`, `texto.length()` y `lista.size()`.
- Acceder a `null` o a un índice fuera del rango.
- Escribir ciclos cuya condición nunca cambia.
- Ignorar excepciones o dejar recursos abiertos.
- Colocar todo el programa en `main` en vez de dividirlo en métodos y clases.

#### Programa Java con los fundamentos

Guardar como `FundamentosJava.java`:

```java
import java.util.ArrayList; // Implementa una lista dinámica.
import java.util.HashMap;   // Implementa un mapa de pares clave-valor.
import java.util.List;      // Define las operaciones de una lista.
import java.util.Map;       // Define las operaciones de un mapa.
import java.util.Scanner;   // Lee valores desde la entrada estándar.

public class FundamentosJava {
    private static final double NOTA_MINIMA = 70.0; // Constante de clase.

    public static void main(String[] args) {
        // Variables primitivas y una referencia de tipo String.
        int edad = 20;
        long identificador = 1_000_000L;
        double promedio = 84.5;
        char grupo = 'A';
        boolean matriculado = true;
        String nombre = "Ana";

        // Conversión: explícita si puede perder información; parseo desde texto.
        int promedioEntero = (int) promedio;
        int numeroConvertido = Integer.parseInt("25");
        String promedioComoTexto = String.valueOf(promedio);

        // Un arreglo tiene longitud fija y sus posiciones empiezan en cero.
        int[] notas = {80, 90, 65, 100};
        notas[2] = 70;

        // Una lista crece dinámicamente y solo admite objetos como tipo genérico.
        List<String> cursos = new ArrayList<>();
        cursos.add("Programación");
        cursos.add("Bases de datos");

        // Un mapa asocia una clave única con un valor.
        Map<String, Integer> creditos = new HashMap<>();
        creditos.put("Programación", 4);
        creditos.put("Bases de datos", 3);

        // if/else selecciona una de dos rutas.
        if (promedio >= NOTA_MINIMA && matriculado) {
            System.out.println(nombre + " aprobó");
        } else {
            System.out.println(nombre + " no aprobó");
        }

        // switch selecciona según un valor concreto.
        switch (grupo) {
            case 'A' -> System.out.println("Horario diurno");
            case 'B' -> System.out.println("Horario nocturno");
            default -> System.out.println("Grupo desconocido");
        }

        // for con índice: permite acceder a la posición y modificar elementos.
        int suma = 0;
        for (int i = 0; i < notas.length; i++) {
            suma += notas[i];
        }

        // for-each: recorre valores sin administrar el índice.
        for (String curso : cursos) {
            System.out.println(curso + ": " + creditos.get(curso) + " créditos");
        }

        // while evalúa antes; do-while ejecuta el cuerpo al menos una vez.
        int contador = 0;
        while (contador < 2) contador++;
        do {
            contador--;
        } while (contador > 0);

        // Entrada desde teclado. try-with-resources cierra el Scanner.
        try (Scanner teclado = new Scanner(System.in)) {
            System.out.print("Escriba su ciudad: ");
            String ciudad = teclado.nextLine().trim();
            System.out.printf("%s, edad %d, id %d, promedio %d, ciudad %s%n",
                    nombre, edad, identificador, promedioEntero, ciudad);
        }

        System.out.println("Número convertido: " + numeroConvertido);
        System.out.println("Promedio como texto: " + promedioComoTexto);
        System.out.println("Promedio calculado: " + (double) suma / notas.length);
    }
}
```

Compilar y ejecutar: `javac FundamentosJava.java` y `java FundamentosJava`.

## Java 3.2. Procedimientos y funciones

En Java son **métodos**. `void` no retorna; los demás tipos usan `return`. `static` pertenece a la clase y la sobrecarga usa el mismo nombre con diferentes parámetros. Los argumentos se pasan por valor.

### Programa Java: procedimientos, funciones y sobrecarga

Guardar como `MetodosJava.java`:

```java
import java.util.Locale; // Controla el formato regional de números.

public class MetodosJava {
    public static void main(String[] args) {
        // Fija el punto como separador decimal para obtener una salida consistente.
        Locale.setDefault(Locale.US);

        double precio = 125.50;
        int cantidad = 3;
        double subtotal = calcularSubtotal(precio, cantidad); // Llama a una función.
        double total = aplicarImpuesto(subtotal, 0.13);

        mostrarLinea("Subtotal", subtotal);             // procedimiento
        mostrarLinea("Total", total);                   // método sobrecargado
        System.out.println("Mayor: " + maximo(8, 12));  // función
    }

    private static double calcularSubtotal(double precio, int cantidad) {
        // Impide que el método trabaje con datos fuera de su dominio válido.
        if (precio < 0 || cantidad < 0) {
            throw new IllegalArgumentException("Precio y cantidad no pueden ser negativos");
        }
        return precio * cantidad;
    }

    private static double aplicarImpuesto(double monto, double tasa) {
        return monto * (1 + tasa);
    }

    private static int maximo(int a, int b) {
        return a > b ? a : b;
    }

    private static void mostrarLinea(String etiqueta, double monto) {
        System.out.printf("%s: %.2f%n", etiqueta, monto);
    }

    private static void mostrarLinea(String mensaje) {
        System.out.println(mensaje);
    }
}
```

Compilar y ejecutar: `javac MetodosJava.java` y `java MetodosJava`.

## Java 3.3. Administración de clases

- **Clase/objeto:** modelo e instancia.
- **Campo/método:** estado y comportamiento.
- **Constructor:** inicializa.
- **Encapsulamiento:** `private`, `protected` y `public`.
- **Herencia/interfaz:** `extends` e `implements`.
- **Polimorfismo:** `@Override` selecciona la versión del objeto real.

### Programa Java: encapsulamiento, herencia, interfaz y polimorfismo

Guardar como `ClasesJava.java`:

```java
import java.util.ArrayList; // Implementación modificable de una lista.
import java.util.List;      // Interfaz para trabajar con colecciones ordenadas.

interface Bonificable {
    double calcularBonificacion();
}

abstract class Empleado {
    private final String nombre;
    private double salarioBase;

    protected Empleado(String nombre, double salarioBase) {
        if (nombre == null || nombre.isBlank() || salarioBase < 0) {
            throw new IllegalArgumentException("Datos de empleado inválidos");
        }
        this.nombre = nombre;
        this.salarioBase = salarioBase;
    }

    public String getNombre() { return nombre; }
    public double getSalarioBase() { return salarioBase; }

    public void aumentarSalario(double porcentaje) {
        if (porcentaje < 0) throw new IllegalArgumentException("Porcentaje inválido");
        salarioBase *= 1 + porcentaje / 100.0;
    }

    public abstract double calcularPago();
}

class EmpleadoFijo extends Empleado implements Bonificable {
    public EmpleadoFijo(String nombre, double salarioBase) {
        super(nombre, salarioBase);
    }

    @Override
    public double calcularBonificacion() { return getSalarioBase() * 0.10; }

    @Override
    public double calcularPago() { return getSalarioBase() + calcularBonificacion(); }
}

class EmpleadoPorHoras extends Empleado {
    private final int horas;

    public EmpleadoPorHoras(String nombre, double pagoPorHora, int horas) {
        super(nombre, pagoPorHora);
        if (horas < 0) throw new IllegalArgumentException("Horas inválidas");
        this.horas = horas;
    }

    @Override
    public double calcularPago() { return getSalarioBase() * horas; }
}

public class ClasesJava {
    public static void main(String[] args) {
        // La lista usa el tipo base para almacenar objetos de diferentes subclases.
        List<Empleado> empleados = new ArrayList<>();
        empleados.add(new EmpleadoFijo("Ana", 900_000));
        empleados.add(new EmpleadoPorHoras("Luis", 5_000, 160));

        for (Empleado empleado : empleados) {
            // Java selecciona calcularPago() según el objeto real: polimorfismo.
            System.out.printf("%s recibe %.2f%n",
                    empleado.getNombre(), empleado.calcularPago());
        }
    }
}
```

`calcularPago()` demuestra polimorfismo. Ejecutar con `javac ClasesJava.java` y `java ClasesJava`.

## Java 3.4. Acceso a medios de almacenamiento

Java usa memoria, archivos o bases de datos. Se validan datos, se usa UTF-8 y se cierran recursos con `try-with-resources`. CRUD significa crear, leer, actualizar y eliminar.

### Programa Java: escribir y leer un archivo CSV

Guardar como `ArchivosJava.java`:

```java
import java.io.BufferedReader;               // Lee texto eficientemente, línea por línea.
import java.io.BufferedWriter;               // Escribe texto usando un búfer.
import java.io.IOException;                  // Representa errores de entrada y salida.
import java.nio.charset.StandardCharsets;    // Proporciona la codificación UTF-8.
import java.nio.file.Files;                  // Crea lectores y escritores de archivos.
import java.nio.file.Path;                   // Representa una ruta del sistema de archivos.
import java.nio.file.StandardOpenOption;     // Define cómo se abre o crea un archivo.
import java.util.ArrayList;                  // Lista modificable para los datos leídos.
import java.util.List;                       // Tipo general de colección ordenada.

public class ArchivosJava {
    record Producto(int id, String nombre, double precio) { }

    public static void main(String[] args) {
        Path ruta = Path.of("productos.csv");
        // Datos que se escribirán en el archivo de ejemplo.
        List<Producto> productos = List.of(
                new Producto(1, "Teclado", 25.50),
                new Producto(2, "Ratón", 12.75));

        try {
            // Primero persiste la lista y luego recupera su contenido.
            guardar(ruta, productos);
            for (Producto producto : leer(ruta)) {
                System.out.printf("%d | %s | %.2f%n",
                        producto.id(), producto.nombre(), producto.precio());
            }
        } catch (IOException | IllegalArgumentException error) {
            System.err.println("No fue posible procesar el archivo: " + error.getMessage());
        }
    }

    private static void guardar(Path ruta, List<Producto> productos) throws IOException {
        // try-with-resources cierra el escritor incluso cuando ocurre una excepción.
        try (BufferedWriter escritor = Files.newBufferedWriter(ruta, StandardCharsets.UTF_8,
                StandardOpenOption.CREATE, StandardOpenOption.TRUNCATE_EXISTING)) {
            escritor.write("id,nombre,precio");
            escritor.newLine();
            for (Producto p : productos) {
                if (p.nombre().contains(","))
                    throw new IllegalArgumentException("Este ejemplo no admite comas en el nombre");
                escritor.write(p.id() + "," + p.nombre() + "," + p.precio());
                escritor.newLine();
            }
        }
    }

    private static List<Producto> leer(Path ruta) throws IOException {
        List<Producto> resultado = new ArrayList<>();
        // El lector también se cierra automáticamente al terminar el bloque.
        try (BufferedReader lector = Files.newBufferedReader(ruta, StandardCharsets.UTF_8)) {
            lector.readLine(); // encabezado
            String linea;
            while ((linea = lector.readLine()) != null) {
                String[] partes = linea.split(",", -1);
                if (partes.length != 3) throw new IOException("Línea CSV inválida: " + linea);
                resultado.add(new Producto(
                        Integer.parseInt(partes[0]), partes[1], Double.parseDouble(partes[2])));
            }
        }
        return resultado;
    }
}
```

`try-with-resources` cierra los recursos automáticamente.

### Bases de datos con JDBC

JDBC usa `Connection`, `PreparedStatement` y `ResultSet`. Las consultas llevan parámetros `?`. El controlador y la cadena dependen del motor.

## Java 3.5. Hilos y excepciones

### Hilos y concurrencia

`ExecutorService` administra trabajadores, `Callable` devuelve resultados y `Future` permite esperarlos. La sincronización protege datos compartidos.

### Programa Java: ejecutor y contador seguro

Guardar como `HilosJava.java`:

```java
import java.util.ArrayList;                    // Almacena las tareas que se ejecutarán.
import java.util.List;                         // Interfaz común para listas.
import java.util.concurrent.Callable;          // Tarea que devuelve un resultado.
import java.util.concurrent.ExecutionException;// Envuelve errores producidos por una tarea.
import java.util.concurrent.ExecutorService;   // Administra un conjunto de hilos.
import java.util.concurrent.Executors;         // Crea implementaciones de ejecutores.
import java.util.concurrent.Future;            // Representa un resultado todavía pendiente.

public class HilosJava {
    public static void main(String[] args) {
        // Limita la ejecución concurrente a tres hilos reutilizables.
        ExecutorService ejecutor = Executors.newFixedThreadPool(3);
        List<Callable<Integer>> tareas = new ArrayList<>();

        for (int numero = 1; numero <= 5; numero++) {
            final int valor = numero;
            // La expresión lambda representa una tarea que devuelve un entero.
            tareas.add(() -> {
                Thread.sleep(100);
                return valor * valor;
            });
        }

        try {
            List<Future<Integer>> resultados = ejecutor.invokeAll(tareas); // Espera todas.
            int suma = 0;
            for (Future<Integer> resultado : resultados) suma += resultado.get();
            System.out.println("Suma de cuadrados: " + suma);
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            System.err.println("El hilo principal fue interrumpido");
        } catch (ExecutionException error) {
            System.err.println("Falló una tarea: " + error.getCause().getMessage());
        } finally {
            // Libera los hilos del ejecutor aunque alguna tarea falle.
            ejecutor.shutdown();
        }
    }
}
```

Cada tarea devuelve su resultado; `Future.get()` obtiene el valor o propaga su error.

### Excepciones

`try` contiene la operación, `catch` maneja, `finally` limpia y `throw` genera. Las excepciones *checked* se capturan o declaran con `throws`.

### Programa Java: validación, excepción propia y `finally`

Guardar como `ExcepcionesJava.java`:

```java
import java.util.Scanner; // Lee datos introducidos desde la consola.

class EdadInvalidaException extends Exception {
    public EdadInvalidaException(String mensaje) { super(mensaje); }
}

public class ExcepcionesJava {
    public static void main(String[] args) {
        // Scanner recibe la entrada estándar del teclado.
        Scanner teclado = new Scanner(System.in);
        try {
            System.out.print("Edad: ");
            int edad = Integer.parseInt(teclado.nextLine());
            validarEdad(edad);
            System.out.println("Edad aceptada");
        } catch (NumberFormatException error) {
            System.err.println("Debe escribir un número entero");
        } catch (EdadInvalidaException error) {
            System.err.println(error.getMessage());
        } finally {
            teclado.close();
            System.out.println("Proceso finalizado");
        }
    }

    private static void validarEdad(int edad) throws EdadInvalidaException {
        // Genera una excepción propia cuando se incumple la regla del negocio.
        if (edad < 0 || edad > 130)
            throw new EdadInvalidaException("La edad debe estar entre 0 y 130");
    }
}
```

## Java 3.6. Formularios, informes, menús, proyectos y aplicaciones

Swing crea formularios por eventos. Los controles reciben datos, los manejadores responden y los menús organizan comandos.

### Programa Java Swing: formulario y menú ejecutables

Swing viene incluido en el JDK. Guardar como `FormularioJava.java`:

```java
import java.awt.BorderLayout;       // Distribuye componentes en cinco regiones.
import java.awt.GridLayout;         // Ordena componentes en una cuadrícula.
import javax.swing.JButton;         // Botón que genera eventos al pulsarlo.
import javax.swing.JFrame;          // Ventana principal de Swing.
import javax.swing.JLabel;          // Muestra texto no editable.
import javax.swing.JMenu;           // Menú desplegable.
import javax.swing.JMenuBar;        // Barra que contiene los menús.
import javax.swing.JMenuItem;       // Opción seleccionable de un menú.
import javax.swing.JOptionPane;     // Muestra cuadros de diálogo.
import javax.swing.JPanel;          // Contenedor para agrupar controles.
import javax.swing.JTextField;      // Campo de entrada de texto.
import javax.swing.SwingUtilities;  // Ejecuta la interfaz en el hilo de eventos.

public class FormularioJava extends JFrame {
    private final JTextField campoNombre = new JTextField(20);
    private final JLabel resultado = new JLabel("Escriba su nombre");

    public FormularioJava() {
        super("Registro");
        // Divide la construcción para mantener cada método enfocado.
        configurarVentana();
        crearContenido();
        crearMenu();
    }

    private void configurarVentana() {
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(420, 180);
        setLocationRelativeTo(null);
    }

    private void crearContenido() {
        JPanel formulario = new JPanel(new GridLayout(2, 2, 8, 8));
        formulario.add(new JLabel("Nombre:"));
        formulario.add(campoNombre);
        JButton boton = new JButton("Saludar");
        // Registra la función que se ejecutará cuando el usuario haga clic.
        boton.addActionListener(evento -> saludar());
        formulario.add(boton);
        formulario.add(resultado);
        add(formulario, BorderLayout.CENTER);
    }

    private void crearMenu() {
        JMenuItem limpiar = new JMenuItem("Limpiar");
        limpiar.addActionListener(evento -> {
            campoNombre.setText("");
            resultado.setText("Escriba su nombre");
            campoNombre.requestFocus();
        });
        JMenuItem salir = new JMenuItem("Salir");
        salir.addActionListener(evento -> dispose());
        JMenu archivo = new JMenu("Archivo");
        archivo.add(limpiar);
        archivo.addSeparator();
        archivo.add(salir);
        JMenuBar barra = new JMenuBar();
        barra.add(archivo);
        setJMenuBar(barra);
    }

    private void saludar() {
        String nombre = campoNombre.getText().trim();
        if (nombre.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Debe escribir un nombre",
                    "Validación", JOptionPane.WARNING_MESSAGE);
            return;
        }
        resultado.setText("Hola, " + nombre);
    }

    public static void main(String[] args) {
        // Toda modificación de Swing debe comenzar en el hilo de eventos.
        SwingUtilities.invokeLater(() -> new FormularioJava().setVisible(true));
    }
}
```

Ejecutar con `javac FormularioJava.java` y `java FormularioJava`.

### Informes en Java

Seleccionar → filtrar → agrupar → totalizar → formatear → mostrar o exportar.

### Organización de un proyecto Java

```text
presentación -> lógica de negocio -> acceso a datos -> almacenamiento
                         |
                       modelo
```

Los paquetes organizan clases y Maven/Gradle administran dependencias.

# Parte II. C#.NET

## C# 3.1. Entorno de C# y .NET

### SDK, CLR y proceso de ejecución

El **SDK de .NET** incluye compilador, runtime, comando `dotnet` y bibliotecas. C# se compila a **CIL** dentro de un ensamblado, que ejecuta el **CLR**.

```text
Archivo .cs -> compilador -> CIL/ensamblado -> CLR -> sistema operativo
```

- **CLR:** ejecución, memoria, excepciones e hilos.
- **BCL:** biblioteca base de .NET.
- **`.csproj`:** configuración y dependencias del proyecto.
- **Namespace:** organización de tipos.
- **NuGet:** gestor de paquetes.

#### Primer programa C# ejecutable

Crear el proyecto y reemplazar `Program.cs` por el código indicado:

```powershell
dotnet new console -n HolaCSharp
cd HolaCSharp
dotnet run -- Ana
```

```csharp
using System; // Proporciona Console, String y tipos fundamentales.

namespace HolaCSharp;

internal static class Program
{
    private static void Main(string[] args)
    {
        // Usa el primer argumento o un nombre predeterminado cuando no se recibe ninguno.
        string nombre = args.Length > 0 ? args[0] : "estudiante";
        Console.WriteLine($"Hola, {nombre}. C# funciona correctamente.");
    }
}
```

Java y C# liberan automáticamente objetos sin uso; archivos y conexiones sí deben cerrarse.

### Fundamentos básicos de C#

Los bloques pequeños de esta sección muestran una regla de sintaxis de forma aislada. El apartado **Programa C# con los fundamentos** reúne esas reglas en un proyecto completo, compilable y ejecutable.

#### Estructura, nombres y comentarios

- C# distingue mayúsculas y normalmente termina instrucciones con `;`.
- Clases, métodos y propiedades: `PascalCase`; variables locales: `camelCase`.
- Comentarios: `// una línea`, `/* varias líneas */` y `/// documentación XML`.
- Los bloques usan `{ }`; un *namespace* organiza tipos relacionados.

#### Usings comunes

`using` permite utilizar tipos sin escribir su nombre completo. Los proyectos modernos pueden habilitar *implicit usings*, pero declararlos ayuda a reconocer su procedencia.

| Using | Uso |
|---|---|
| `System` | Consola, cadenas, fechas, matemáticas y excepciones |
| `System.Collections.Generic` | `List<T>`, `Dictionary<TKey,TValue>`, `HashSet<T>` |
| `System.Linq` | Filtrar, ordenar, transformar y agregar colecciones |
| `System.IO` | Archivos, directorios y flujos |
| `System.Text` | Codificaciones y `StringBuilder` |
| `System.Globalization` | Formatos regionales |
| `System.Threading` | Cancelación y sincronización |
| `System.Threading.Tasks` | Tareas y programación asíncrona |

#### Tipos y declaración de variables

| Tipo | Ejemplo | Uso |
|---|---|---|
| `byte`, `short`, `int`, `long` | `int edad = 20;` | Enteros de distinto rango |
| `float`, `double`, `decimal` | `decimal precio = 12.5m;` | Decimales; `decimal` es apropiado para dinero |
| `char` | `char inicial = 'A';` | Un carácter Unicode |
| `bool` | `bool activo = true;` | `true` o `false` |
| `string` | `string nombre = "Ana";` | Texto |
| Arreglo | `int[] notas = {80, 90};` | Tamaño fijo |
| Objeto | `Random azar = new Random();` | Instancia de una clase |

Sufijos frecuentes: `10L` (`long`), `1.5F` (`float`), `1.5M` (`decimal`). `const` crea una constante de compilación; `readonly` permite asignar un campo al declararlo o en el constructor. `var` infiere el tipo local, pero no lo vuelve dinámico: `var total = 25.0;` sigue siendo `double`.

Los tipos valor contienen directamente sus datos; las clases normalmente son tipos referencia. `int?` es un valor nullable. Con referencias anulables habilitadas, `string?` puede contener `null`, `?.` accede de forma segura y `??` proporciona un valor alternativo.

#### Operadores y control de flujo

- Aritméticos: `+`, `-`, `*`, `/`, `%`.
- Comparación: `==`, `!=`, `<`, `<=`, `>`, `>=`.
- Lógicos: `&&`, `||`, `!`.
- Asignación: `=`, `+=`, `-=`, `*=`, `/=`.
- Incremento: `++`, `--`; ternario: `condicion ? valor1 : valor2`.
- Cadenas: se concatenan con `+` o se interpolan con `$"{variable}"`.

`if`/`else`, `switch`, `for`, `while`, `do-while`, `foreach`, `break` y `continue` cumplen las mismas funciones generales que en Java.

#### Alcance, memoria y valores iniciales

Una variable local existe únicamente dentro de su bloque `{ }`. Un campo pertenece al objeto; un campo `static` pertenece al tipo. Las variables locales deben inicializarse antes de leerse. Los campos reciben valores predeterminados como `0`, `false` o `null`.

Los **tipos valor** (`int`, `bool`, `decimal`, `struct`) contienen el dato. Los **tipos referencia** (`class`, `string`, arreglos) contienen una referencia al objeto. El recolector libera memoria administrada, pero archivos y conexiones se cierran con `using`.

```csharp
int exterior = 10;
if (exterior > 0)
{
    int interior = 20; // Solo existe dentro de este bloque.
    exterior += interior;
}
// interior ya no puede utilizarse aquí.
```

#### Números, conversiones y precisión

La división entre enteros descarta decimales: `5 / 2` produce `2`; `(double)5 / 2` produce `2.5`. Una conversión implícita no pierde información; un *cast* explícito puede perderla. `Convert` transforma tipos generales; `Parse` convierte texto y falla si es inválido; `TryParse` permite validar sin lanzar una excepción. Para dinero se recomienda `decimal`.

```csharp
string entrada = "125";
if (int.TryParse(entrada, out int numero))
    Console.WriteLine(numero * 2);
else
    Console.WriteLine("El valor no es un entero válido");
```

#### Cadenas y caracteres

`string` es inmutable. Propiedades y métodos frecuentes: `Length`, `IsNullOrWhiteSpace`, `Trim`, `Contains`, `StartsWith`, `Substring`, `Replace`, `Split` y `Equals`. La interpolación `$"{valor}"` facilita construir mensajes; `StringBuilder` es útil para muchas modificaciones.

```csharp
string nombre = "  Ana López  ";
string limpio = nombre.Trim();
Console.WriteLine(limpio.ToUpper());
Console.WriteLine(string.Equals("Ana", limpio, StringComparison.OrdinalIgnoreCase));
```

#### Arreglos y colecciones

Los índices comienzan en `0`. Un arreglo tiene tamaño fijo (`Length`). `List<T>` mantiene orden y repetidos; `HashSet<T>` guarda valores únicos; `Dictionary<TKey,TValue>` relaciona claves únicas con valores.

```csharp
int[] arreglo = new int[3]; // {0, 0, 0}
var lista = new List<string>();
lista.Add("C#");
lista[0] = "C# 12";
bool existe = lista.Contains("C# 12");
lista.Remove("C# 12");
Console.WriteLine($"{existe} / tamaño: {lista.Count}");
```

Antes de acceder se comprueba `indice >= 0 && indice < coleccion.Count` (o `< arreglo.Length`). Un índice inválido produce `IndexOutOfRangeException` o `ArgumentOutOfRangeException`.

#### Métodos y paso de argumentos

Un método declara accesibilidad, retorno, nombre y parámetros. `void` no retorna resultado; otros tipos usan `return`. El paso normal es por valor. `ref` permite leer y modificar una variable existente; `out` obliga al método a asignarla; `in` la pasa por referencia sin permitir modificarla. Los parámetros opcionales llevan valor predeterminado.

```csharp
private static double Promedio(int[] valores)
{
    if (valores.Length == 0)
        throw new ArgumentException("El arreglo está vacío", nameof(valores));

    int suma = 0;
    foreach (int valor in valores) suma += valor;
    return (double)suma / valores.Length;
}
```

#### Clases, objetos, propiedades y enums

Una clase agrupa estado y comportamiento. `new` llama al constructor. `this` representa el objeto actual. Las propiedades controlan el acceso a datos; `get` lee y `set` asigna. Un `enum` restringe una variable a opciones conocidas.

```csharp
internal enum Estado { Activo, Inactivo }

internal sealed class Usuario
{
    public string Nombre { get; }
    public Estado EstadoActual { get; private set; }

    public Usuario(string nombre)
    {
        Nombre = nombre;
        EstadoActual = Estado.Activo;
    }
}
```

#### Errores básicos que deben evitarse

- Usar división entera cuando se esperan decimales.
- Confundir `Length` de arreglos/cadenas con `Count` de colecciones.
- Usar `Parse` con datos no validados cuando corresponde `TryParse`.
- Acceder a referencias `null` o índices fuera del rango.
- Bloquear una operación asíncrona con `.Result` o `.Wait()` sin necesidad.
- Ignorar excepciones o no cerrar recursos.
- Colocar toda la lógica en `Main` en vez de crear métodos y clases.

#### Programa C# con los fundamentos

Crear un proyecto de consola y usar este `Program.cs`:

```csharp
using System;                    // Proporciona Console y conversiones básicas.
using System.Collections.Generic;// Proporciona List<T> y Dictionary<TKey,TValue>.

namespace FundamentosCSharp;

internal static class Program
{
    private const decimal NotaMinima = 70.0m; // Constante de clase.

    private static void Main()
    {
        // Variables de tipos valor y una referencia de tipo string.
        int edad = 20;
        long identificador = 1_000_000L;
        decimal promedio = 84.5m;
        char grupo = 'A';
        bool matriculado = true;
        string nombre = "Ana";

        // Conversión explícita y conversión desde/hacia texto.
        int promedioEntero = (int)promedio;
        int numeroConvertido = int.Parse("25");
        string promedioComoTexto = promedio.ToString();

        // Un arreglo tiene tamaño fijo y sus posiciones empiezan en cero.
        int[] notas = { 80, 90, 65, 100 };
        notas[2] = 70;

        // List<T> crece dinámicamente; Dictionary relaciona claves y valores.
        var cursos = new List<string> { "Programación", "Bases de datos" };
        var creditos = new Dictionary<string, int>
        {
            ["Programación"] = 4,
            ["Bases de datos"] = 3
        };

        // if/else selecciona una de dos rutas.
        if (promedio >= NotaMinima && matriculado)
            Console.WriteLine($"{nombre} aprobó");
        else
            Console.WriteLine($"{nombre} no aprobó");

        // switch expression devuelve un valor según el caso coincidente.
        string horario = grupo switch
        {
            'A' => "diurno",
            'B' => "nocturno",
            _ => "desconocido"
        };
        Console.WriteLine($"Horario {horario}");

        // for con índice: permite consultar o modificar cada posición.
        int suma = 0;
        for (int i = 0; i < notas.Length; i++)
            suma += notas[i];

        // foreach recorre los elementos sin administrar un índice.
        foreach (string curso in cursos)
            Console.WriteLine($"{curso}: {creditos[curso]} créditos");

        // while evalúa antes; do-while ejecuta al menos una vez.
        int contador = 0;
        while (contador < 2) contador++;
        do
        {
            contador--;
        } while (contador > 0);

        // ?? sustituye null; Trim elimina espacios de los extremos.
        Console.Write("Escriba su ciudad: ");
        string ciudad = (Console.ReadLine() ?? "Sin indicar").Trim();

        Console.WriteLine($"{nombre}, edad {edad}, id {identificador}, " +
                          $"promedio {promedioEntero}, ciudad {ciudad}");
        Console.WriteLine($"Número convertido: {numeroConvertido}");
        Console.WriteLine($"Promedio como texto: {promedioComoTexto}");
        Console.WriteLine($"Promedio calculado: {(decimal)suma / notas.Length:F2}");
    }
}
```

Ejecución: `dotnet new console -n FundamentosCSharp`, sustituir `Program.cs` y usar `dotnet run`.

## C# 3.2. Procedimientos y funciones

En C# son **métodos**. `void` no retorna; los demás tipos usan `return`. `static` pertenece a la clase, la sobrecarga usa diferentes parámetros y también existen `ref`, `out` e `in`.

### Programa C#: procedimientos, funciones, sobrecarga y `out`

Crear un proyecto de consola y usar este `Program.cs`:

```csharp
using System;              // Proporciona Console y excepciones básicas.
using System.Globalization;// Controla el formato regional de números.

namespace MetodosCSharp;

internal static class Program
{
    private static void Main()
    {
        // Garantiza que el ejemplo use el punto como separador decimal.
        CultureInfo.CurrentCulture = CultureInfo.InvariantCulture;
        double precio = 125.50;
        int cantidad = 3;
        double subtotal = CalcularSubtotal(precio, cantidad); // Llama a una función.

        MostrarLinea("Subtotal", subtotal);
        MostrarLinea("Total", AplicarImpuesto(subtotal, 0.13));

        if (IntentarDividir(10, 4, out double cociente))
            Console.WriteLine($"Cociente: {cociente:F2}");
    }

    private static double CalcularSubtotal(double precio, int cantidad)
    {
        if (precio < 0 || cantidad < 0)
            throw new ArgumentOutOfRangeException(nameof(precio), "Los valores no pueden ser negativos");
        return precio * cantidad;
    }

    private static double AplicarImpuesto(double monto, double tasa) => monto * (1 + tasa);

    private static bool IntentarDividir(double dividendo, double divisor, out double resultado)
    {
        // out permite devolver el cociente además del valor bool.
        if (divisor == 0)
        {
            resultado = 0;
            return false;
        }
        resultado = dividendo / divisor;
        return true;
    }

    private static void MostrarLinea(string etiqueta, double monto) =>
        Console.WriteLine($"{etiqueta}: {monto:F2}");

    private static void MostrarLinea(string mensaje) => Console.WriteLine(mensaje);
}
```

Ejecución: `dotnet new console -n MetodosCSharp`, sustituir `Program.cs` y usar `dotnet run`.

## C# 3.3. Administración de clases

- **Clase/objeto:** modelo e instancia.
- **Campo, propiedad y método:** estado, acceso y comportamiento.
- **Constructor:** inicializa.
- **Encapsulamiento:** `private`, `protected` y `public`.
- **Herencia/interfaz:** se indican con `:`.
- **Polimorfismo:** `override` selecciona la versión del objeto real.

### Programa C#: encapsulamiento, herencia, interfaz y polimorfismo

Usar como `Program.cs` de un proyecto de consola:

```csharp
using System;                    // Proporciona Console y excepciones básicas.
using System.Collections.Generic;// Proporciona la colección genérica List<T>.

namespace ClasesCSharp;

internal interface IBonificable
{
    decimal CalcularBonificacion();
}

internal abstract class Empleado
{
    public string Nombre { get; }
    public decimal SalarioBase { get; private set; }

    protected Empleado(string nombre, decimal salarioBase)
    {
        if (string.IsNullOrWhiteSpace(nombre) || salarioBase < 0)
            throw new ArgumentException("Datos de empleado inválidos");
        Nombre = nombre;
        SalarioBase = salarioBase;
    }

    public void AumentarSalario(decimal porcentaje)
    {
        if (porcentaje < 0) throw new ArgumentOutOfRangeException(nameof(porcentaje));
        SalarioBase *= 1 + porcentaje / 100;
    }

    public abstract decimal CalcularPago();
}

internal sealed class EmpleadoFijo : Empleado, IBonificable
{
    public EmpleadoFijo(string nombre, decimal salarioBase) : base(nombre, salarioBase) { }
    public decimal CalcularBonificacion() => SalarioBase * 0.10m;
    public override decimal CalcularPago() => SalarioBase + CalcularBonificacion();
}

internal sealed class EmpleadoPorHoras : Empleado
{
    private int Horas { get; }

    public EmpleadoPorHoras(string nombre, decimal pagoPorHora, int horas)
        : base(nombre, pagoPorHora)
    {
        if (horas < 0) throw new ArgumentOutOfRangeException(nameof(horas));
        Horas = horas;
    }

    public override decimal CalcularPago() => SalarioBase * Horas;
}

internal static class Program
{
    private static void Main()
    {
        // El tipo base permite reunir objetos de distintas subclases.
        var empleados = new List<Empleado>
        {
            new EmpleadoFijo("Ana", 900_000m),
            new EmpleadoPorHoras("Luis", 5_000m, 160)
        };

        // Se ejecuta CalcularPago() de la clase real: polimorfismo.
        foreach (Empleado empleado in empleados)
            Console.WriteLine($"{empleado.Nombre} recibe {empleado.CalcularPago():N2}");
    }
}
```

## C# 3.4. Acceso a medios de almacenamiento

C# usa memoria, archivos o bases de datos. Se validan datos, se usa UTF-8 y se cierran recursos con `using`. CRUD significa crear, leer, actualizar y eliminar.

### Programa C#: escribir y leer un archivo CSV

Usar como `Program.cs`:

```csharp
using System;                    // Proporciona Console y tipos fundamentales.
using System.Collections.Generic;// Proporciona List<T> e IEnumerable<T>.
using System.Globalization;      // Permite guardar números con formato estable.
using System.IO;                 // Proporciona lectores, escritores y IOException.
using System.Text;               // Proporciona Encoding y UTF8Encoding.

namespace ArchivosCSharp;

internal record Producto(int Id, string Nombre, decimal Precio);

internal static class Program
{
    private static void Main()
    {
        string ruta = "productos.csv";
        // Datos que se guardarán en el archivo CSV.
        var productos = new List<Producto>
        {
            new(1, "Teclado", 25.50m),
            new(2, "Ratón", 12.75m)
        };

        try
        {
            // Persiste los productos y después vuelve a leerlos.
            Guardar(ruta, productos);
            foreach (Producto producto in Leer(ruta))
                Console.WriteLine($"{producto.Id} | {producto.Nombre} | {producto.Precio:F2}");
        }
        catch (IOException error)
        {
            Console.Error.WriteLine($"Error de archivo: {error.Message}");
        }
        catch (FormatException error)
        {
            Console.Error.WriteLine($"Formato inválido: {error.Message}");
        }
    }

    private static void Guardar(string ruta, IEnumerable<Producto> productos)
    {
        // using libera el escritor automáticamente al salir del método.
        using var escritor = new StreamWriter(ruta, false, new UTF8Encoding(false));
        escritor.WriteLine("id,nombre,precio");
        foreach (Producto p in productos)
        {
            if (p.Nombre.Contains(',')) throw new FormatException("El nombre contiene una coma");
            escritor.WriteLine($"{p.Id},{p.Nombre},{p.Precio.ToString(CultureInfo.InvariantCulture)}");
        }
    }

    private static List<Producto> Leer(string ruta)
    {
        var resultado = new List<Producto>();
        // StreamReader interpreta el contenido usando UTF-8.
        using var lector = new StreamReader(ruta, Encoding.UTF8);
        lector.ReadLine();
        string? linea;
        while ((linea = lector.ReadLine()) is not null)
        {
            string[] partes = linea.Split(',');
            if (partes.Length != 3) throw new FormatException($"Línea inválida: {linea}");
            resultado.Add(new Producto(int.Parse(partes[0]), partes[1],
                decimal.Parse(partes[2], CultureInfo.InvariantCulture)));
        }
        return resultado;
    }
}
```

### Bases de datos con ADO.NET

ADO.NET usa una conexión, `DbCommand`, parámetros y `DbDataReader`. El proveedor y la cadena dependen del motor.

## C# 3.5. Hilos y excepciones

### Hilos, tareas y concurrencia

`Task` representa una operación; `async` y `await` esperan sin bloquear y `CancellationToken` solicita cancelación.

### Programa C#: tareas asíncronas y resultado seguro

Usar como `Program.cs`:

```csharp
using System;                // Proporciona Console y TimeSpan.
using System.Linq;           // Permite crear, transformar y sumar secuencias.
using System.Threading;      // Proporciona CancellationToken.
using System.Threading.Tasks;// Proporciona Task y operaciones asíncronas.

namespace HilosCSharp;

internal static class Program
{
    private static async Task Main()
    {
        // Cancela automáticamente si el conjunto tarda más de cinco segundos.
        using var cancelacion = new CancellationTokenSource(TimeSpan.FromSeconds(5));
        try
        {
            Task<int>[] tareas = Enumerable.Range(1, 5)
                .Select(numero => CuadradoAsync(numero, cancelacion.Token))
                .ToArray();
            int[] resultados = await Task.WhenAll(tareas); // Espera sin bloquear.
            Console.WriteLine($"Suma de cuadrados: {resultados.Sum()}");
        }
        catch (OperationCanceledException)
        {
            Console.Error.WriteLine("La operación fue cancelada");
        }
    }

    private static async Task<int> CuadradoAsync(int numero, CancellationToken token)
    {
        // Simula una operación de entrada/salida que acepta cancelación.
        await Task.Delay(100, token);
        return numero * numero;
    }
}
```

`async` permite esperar sin bloquear; no significa necesariamente crear otro hilo.

### Excepciones

`try` contiene la operación, `catch` maneja, `finally` limpia y `throw` genera. C# no obliga a declarar excepciones.

### Programa C#: validación, excepción propia y `finally`

```csharp
using System; // Proporciona Console, Exception y tipos fundamentales.

namespace ExcepcionesCSharp;

internal sealed class EdadInvalidaException : Exception
{
    public EdadInvalidaException(string mensaje) : base(mensaje) { }
}

internal static class Program
{
    private static void Main()
    {
        try
        {
            // ReadLine puede devolver null; en ese caso se usa una cadena vacía.
            Console.Write("Edad: ");
            string entrada = Console.ReadLine() ?? "";
            int edad = int.Parse(entrada);
            ValidarEdad(edad);
            Console.WriteLine("Edad aceptada");
        }
        catch (FormatException)
        {
            Console.Error.WriteLine("Debe escribir un número entero");
        }
        catch (EdadInvalidaException error)
        {
            Console.Error.WriteLine(error.Message);
        }
        finally
        {
            Console.WriteLine("Proceso finalizado");
        }
    }

    private static void ValidarEdad(int edad)
    {
        // Genera una excepción propia al incumplir la regla del negocio.
        if (edad is < 0 or > 130)
            throw new EdadInvalidaException("La edad debe estar entre 0 y 130");
    }
}
```

## C# 3.6. Formularios, informes, menús, proyectos y aplicaciones

Windows Forms crea formularios por eventos. Los controles reciben datos, los manejadores responden y los menús organizan comandos.

### Programa C# Windows Forms: formulario y menú ejecutables

Windows Forms se ejecuta en Windows. Crear el proyecto:

```powershell
dotnet new winforms -n FormularioCSharp
cd FormularioCSharp
```

Reemplazar `Program.cs` con este código; no necesita el diseñador:

```csharp
using System;              // Proporciona tipos y eventos fundamentales.
using System.Drawing;      // Proporciona Size para las dimensiones.
using System.Windows.Forms;// Proporciona formularios y controles de Windows.

namespace FormularioCSharp;

internal sealed class VentanaPrincipal : Form
{
    private readonly TextBox campoNombre = new() { Width = 220 };
    private readonly Label resultado = new() { AutoSize = true, Text = "Escriba su nombre" };

    public VentanaPrincipal()
    {
        // Configura las propiedades básicas de la ventana.
        Text = "Registro";
        ClientSize = new Size(420, 170);
        StartPosition = FormStartPosition.CenterScreen;

        var etiqueta = new Label { Text = "Nombre:", AutoSize = true };
        var boton = new Button { Text = "Saludar", AutoSize = true };
        // Suscribe una expresión lambda al evento Click.
        boton.Click += (_, _) => Saludar();

        var panel = new FlowLayoutPanel
        {
            Dock = DockStyle.Fill,
            Padding = new Padding(15),
            FlowDirection = FlowDirection.TopDown
        };
        panel.Controls.Add(etiqueta);
        panel.Controls.Add(campoNombre);
        panel.Controls.Add(boton);
        panel.Controls.Add(resultado);
        Controls.Add(panel);
        MainMenuStrip = CrearMenu();
        Controls.Add(MainMenuStrip);
    }

    private MenuStrip CrearMenu()
    {
        var limpiar = new ToolStripMenuItem("Limpiar");
        limpiar.Click += (_, _) =>
        {
            campoNombre.Clear();
            resultado.Text = "Escriba su nombre";
            campoNombre.Focus();
        };
        var salir = new ToolStripMenuItem("Salir");
        salir.Click += (_, _) => Close();
        var archivo = new ToolStripMenuItem("Archivo");
        archivo.DropDownItems.Add(limpiar);
        archivo.DropDownItems.Add(new ToolStripSeparator());
        archivo.DropDownItems.Add(salir);
        var barra = new MenuStrip();
        barra.Items.Add(archivo);
        return barra;
    }

    private void Saludar()
    {
        string nombre = campoNombre.Text.Trim();
        if (nombre.Length == 0)
        {
            MessageBox.Show("Debe escribir un nombre", "Validación",
                MessageBoxButtons.OK, MessageBoxIcon.Warning);
            return;
        }
        resultado.Text = $"Hola, {nombre}";
    }
}

internal static class Program
{
    [STAThread]
    private static void Main()
    {
        // Inicializa Windows Forms e inicia su ciclo de eventos.
        ApplicationConfiguration.Initialize();
        Application.Run(new VentanaPrincipal());
    }
}
```

Ejecutar con `dotnet run`.

### Informes en C#

Seleccionar → filtrar → agrupar → totalizar → formatear → mostrar o exportar.

### Organización de un proyecto C#

```text
presentación -> lógica de negocio -> acceso a datos -> almacenamiento
                         |
                       modelo
```

Los *namespaces* organizan tipos, las soluciones agrupan proyectos y NuGet administra dependencias.

## Equivalencias rápidas

| Concepto | Java | C#.NET |
|---|---|---|
| Entrada | `public static void main` | `static void Main` |
| Salida | `System.out.println` | `Console.WriteLine` |
| Cadena | `String` | `string` |
| Lista | `ArrayList<T>` | `List<T>` |
| Herencia | `extends` | `:` |
| Interfaz | `implements` | `:` |
| Cierre | `try-with-resources` | `using` |
| Concurrencia | `ExecutorService` | `Task`, `async`/`await` |
| Interfaz | Swing/JavaFX | Windows Forms/WPF |
