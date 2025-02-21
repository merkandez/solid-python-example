# 🏗️ Principios SOLID en Python con Ejemplo Evolutivo

## 📌 **Contexto del ejemplo**
Vamos a modelar una **cafetera** que puede preparar distintos tipos de café. Iremos evolucionando el código para que siga los principios SOLID.

---

## ❌ **Versión 1: Código incorrecto (sin SOLID)**
Este código es funcional, pero **viola varios principios**. Lo analizaremos y luego lo mejoraremos.

```python
class CoffeeMachine:
    def prepare_coffee(self, coffee_type):
        if coffee_type == "Espresso":
            print("☕ Preparando un Espresso...")
        elif coffee_type == "Cappuccino":
            print("☕ Preparando un Cappuccino...")
        else:
            print("❌ Tipo de café no soportado")
```

### 🔴 **Problemas con esta versión**
1. **❌ No sigue el Principio de Responsabilidad Única (SRP)**: `CoffeeMachine` maneja la lógica de **todos los tipos de café** en una sola clase.
2. **❌ No sigue el Principio Abierto/Cerrado (OCP)**: Si queremos agregar un nuevo café, tenemos que modificar `CoffeeMachine`.
3. **❌ No sigue el Principio de Sustitución de Liskov (LSP)**: `coffee_type` es un simple string, lo que no permite reutilizar el código correctamente.

---

## ✅ **Versión 2: Aplicamos el Principio de Responsabilidad Única (SRP)**
Separamos la lógica de preparación del café en clases diferentes.

```python
class Espresso:
    def prepare(self):
        return "☕ Preparando un Espresso..."

class Cappuccino:
    def prepare(self):
        return "☕ Preparando un Cappuccino..."

class CoffeeMachine:
    def prepare_coffee(self, coffee):
        print(coffee.prepare())  # ✅ La cafetera ya no maneja la lógica de cada café
```

✅ **Cada clase tiene una única responsabilidad**: `Espresso` y `Cappuccino` solo preparan su tipo de café.

❌ **Pero aún violamos OCP**, porque si queremos añadir más tipos de café, la cafetera sigue dependiendo de clases concretas.

---

## ✅ **Versión 3: Aplicamos el Principio Abierto/Cerrado (OCP)**
Definimos una **interfaz base** para los cafés y permitimos que `CoffeeMachine` trabaje con cualquier tipo de café sin modificarse.

```python
from abc import ABC, abstractmethod

# 1️⃣ Definimos una abstracción (Interfaz)
class Coffee(ABC):
    @abstractmethod
    def prepare(self):
        pass

# 2️⃣ Implementaciones concretas de la abstracción
class Espresso(Coffee):
    def prepare(self):
        return "☕ Preparando un Espresso..."

class Cappuccino(Coffee):
    def prepare(self):
        return "☕ Preparando un Cappuccino..."

# 3️⃣ CoffeeMachine ahora depende de la abstracción
class CoffeeMachine:
    def prepare_coffee(self, coffee: Coffee):
        print(coffee.prepare())

# 4️⃣ Uso del código con inyección de dependencias
espresso = Espresso()
cappuccino = Cappuccino()

machine = CoffeeMachine()
machine.prepare_coffee(espresso)  # ✅ No importa el tipo de café, sigue el mismo contrato
machine.prepare_coffee(cappuccino)
```

✅ **CoffeeMachine ya no necesita modificaciones** si queremos agregar nuevos cafés.

✅ **Cumple con OCP**: Si queremos agregar `Latte`, solo creamos una nueva clase sin tocar `CoffeeMachine`:

```python
class Latte(Coffee):
    def prepare(self):
        return "☕ Preparando un Latte..."
```

---

## ✅ **Versión 4: Aplicamos el Principio de Sustitución de Liskov (LSP)**

Ya cumplimos con LSP porque `Espresso`, `Cappuccino` y `Latte` **son intercambiables** en `CoffeeMachine`.

```python
latte = Latte()
machine.prepare_coffee(latte)  # ✅ Funciona sin modificar CoffeeMachine
```

Si en el futuro agregamos **más cafés**, la cafetera seguirá funcionando sin cambios.

---

## ✅ **Versión 5: Aplicamos el Principio de Segregación de Interfaces (ISP)**
Si agregamos **una cafetera con más funciones**, como añadir leche, no todos los cafés usan esa función. Para evitar métodos innecesarios, **separamos interfaces**.

```python
class Coffee(ABC):
    @abstractmethod
    def prepare(self):
        pass

class MilkCoffee(Coffee, ABC):
    @abstractmethod
    def add_milk(self):
        pass

class Espresso(Coffee):
    def prepare(self):
        return "☕ Preparando un Espresso..."

class Cappuccino(MilkCoffee):
    def prepare(self):
        return "☕ Preparando un Cappuccino..."
    
    def add_milk(self):
        return "🥛 Añadiendo leche al Cappuccino..."

class CoffeeMachine:
    def prepare_coffee(self, coffee: Coffee):
        print(coffee.prepare())

    def add_milk(self, coffee: MilkCoffee):
        if isinstance(coffee, MilkCoffee):
            print(coffee.add_milk())
```

✅ **No obligamos a todas las clases a implementar `add_milk()`**, solo las que realmente usan leche.

---

## ✅ **Versión 6: Aplicamos el Principio de Inversión de Dependencias (DIP)**

Para que `CoffeeMachine` no dependa de implementaciones concretas, usamos **inyección de dependencias**.

```python
class CoffeeMachine:
    def __init__(self, coffee: Coffee):
        self.coffee = coffee  # ✅ CoffeeMachine solo depende de la abstracción

    def prepare(self):
        print(self.coffee.prepare())

# Uso con inyección de dependencias
espresso = Espresso()
machine = CoffeeMachine(espresso)
machine.prepare()
```

✅ `CoffeeMachine` no depende de clases concretas, sino de la abstracción `Coffee`.

---

## 🎯 **Resumen de las mejoras aplicadas**

| **Principio**  | **Problema inicial** | **Solución aplicada** |
|---------------|--------------------|----------------------|
| **SRP** (Responsabilidad Única) | `CoffeeMachine` manejaba todos los tipos de café | Separar cada café en su propia clase |
| **OCP** (Abierto/Cerrado) | `CoffeeMachine` necesitaba modificaciones para nuevos cafés | Usar una interfaz `Coffee` y herencia |
| **LSP** (Sustitución de Liskov) | No todas las clases podían ser intercambiadas | Todas las clases cumplen con `Coffee` |
| **ISP** (Segregación de Interfaces) | Todos los cafés tenían que manejar `add_milk()` | Separamos `Coffee` y `MilkCoffee` |
| **DIP** (Inversión de Dependencias) | `CoffeeMachine` dependía de clases concretas | Usar inyección de dependencias |

✅ **Ahora tenemos una cafetera flexible, escalable y reutilizable**.

🔥 **Espero que te sea útil! 🚀**
