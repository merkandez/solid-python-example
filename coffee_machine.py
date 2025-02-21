from abc import ABC, abstractmethod

# 1️⃣ Definimos una abstracción (Interfaz)
class Coffee(ABC):
    @abstractmethod
    def prepare(self):
        pass

# 2️⃣ Definimos una sub-interfaz para cafés con leche
class MilkCoffee(Coffee, ABC):
    @abstractmethod
    def add_milk(self):
        pass

# 3️⃣ Implementaciones concretas de la abstracción
class Espresso(Coffee):
    def prepare(self):
        return "☕ Preparando un Espresso..."

class Cappuccino(MilkCoffee):
    def prepare(self):
        return "☕ Preparando un Cappuccino..."
    
    def add_milk(self):
        return "🥛 Añadiendo leche al Cappuccino..."

class Latte(MilkCoffee):
    def prepare(self):
        return "☕ Preparando un Latte..."
    
    def add_milk(self):
        return "🥛 Añadiendo leche al Latte..."

# 4️⃣ CoffeeMachine depende de la abstracción
class CoffeeMachine:
    def __init__(self, coffee: Coffee):
        self.coffee = coffee  # ✅ Inyección de dependencias

    def prepare(self):
        print(self.coffee.prepare())

    def add_milk(self):
        if isinstance(self.coffee, MilkCoffee):
            print(self.coffee.add_milk())

# 5️⃣ Uso del código con diferentes tipos de café
if __name__ == "__main__":
    espresso = Espresso()
    cappuccino = Cappuccino()
    latte = Latte()

    print("---- Máquina de Café ----")

    machine1 = CoffeeMachine(espresso)
    machine1.prepare()  # ☕ Preparando un Espresso...

    machine2 = CoffeeMachine(cappuccino)
    machine2.prepare()  # ☕ Preparando un Cappuccino...
    machine2.add_milk() # 🥛 Añadiendo leche al Cappuccino...

    machine3 = CoffeeMachine(latte)
    machine3.prepare()  # ☕ Preparando un Latte...
    machine3.add_milk() # 🥛 Añadiendo leche al Latte...

""" Este código sigue SOLID correctamente:

SRP: Cada clase tiene una única responsabilidad.
OCP: Podemos agregar nuevos cafés sin modificar CoffeeMachine.
LSP: Espresso, Cappuccino y Latte pueden intercambiarse sin afectar el código.
ISP: MilkCoffee solo lo implementan los cafés que realmente tienen leche.
DIP: CoffeeMachine depende de Coffee, no de implementaciones concretas. """