from abc import ABC, abstractmethod

# Абстрактний базовий клас Transport (замість Vehicle для кращої семантики)
class Vehicle(ABC):
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self):
        pass

# Реалізація класу Car
class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.spec} Spec): Двигун запущено")

# Реалізація класу Motorcycle
class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.spec} Spec): Мотор заведено")

# Абстрактний клас фабрики
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass

# Фабрика для транспортних засобів США
class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "US")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US")

# Фабрика для транспортних засобів ЄС
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "EU")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "EU")

# Клієнтський код
def create_and_start_vehicle(factory: VehicleFactory, vehicle_type: str, make: str, model: str):
    if vehicle_type == "car":
        vehicle = factory.create_car(make, model)
    elif vehicle_type == "motorcycle":
        vehicle = factory.create_motorcycle(make, model)
    else:
        raise ValueError("Невідомий тип транспортного засобу")
    vehicle.start_engine()

# Використання
print("US Vehicles:")
us_factory = USVehicleFactory()
create_and_start_vehicle(us_factory, "car", "Ford", "Mustang")
create_and_start_vehicle(us_factory, "motorcycle", "Harley-Davidson", "Sportster")

print("\nEU Vehicles:")
eu_factory = EUVehicleFactory()
create_and_start_vehicle(eu_factory, "car", "Volkswagen", "Golf")
create_and_start_vehicle(eu_factory, "motorcycle", "Ducati", "Monster")


def create_and_start_vehicle(factory, vehicle_type, make, model):
    if vehicle_type == "car":
        vehicle = factory.create_car(make, model)
    elif vehicle_type == "motorcycle":
        vehicle = factory.create_motorcycle(make, model)
    else:
        raise ValueError("Невідомий тип транспортного засобу")
    vehicle.start_engine()

if __name__ == "__main__":
    print("US Vehicles:")
    us_factory = USVehicleFactory()
    create_and_start_vehicle(us_factory, "car", "Ford", "Mustang")
    create_and_start_vehicle(us_factory, "motorcycle", "Harley-Davidson", "Sportster")

    print("\nEU Vehicles:")
    eu_factory = EUVehicleFactory()
    create_and_start_vehicle(eu_factory, "car", "Volkswagen", "Golf")
    create_and_start_vehicle(eu_factory, "motorcycle", "Ducati", "Monster")
