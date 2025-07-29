"""Родительский класс: Vehicle
•	Атрибуты: brand, model, year
•	Методы: info() (вывод всей информации)
Дочерний класс: Car
•	Доп. атрибуты: fuel_type, max_speed, engine_capacity, rotation_speed, pe
•	Методы: info() (вывод всей информации), engine_power_calc() (расчет мощности двигателя)
"""
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        print("Создание объекта Vehicle")

    def __del__(self):
        print("Удаление объекта Vehicle")

    def info(self):
        print(f"Марка: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.year}")

class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type, max_speed, engine_capacity, rotation_speed, pe):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_type = fuel_type
        self.max_speed = max_speed
        self.engine_capacity = engine_capacity
        self.rotation_speed = rotation_speed
        self.pe = pe
        print("Создание объекта Car")

    def __del__(self):
        print("Удаление объекта Car")

    def info(self):
        print(f"Марка: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.year}\nТип исп. топлива: {self.fuel_type}\nМаксимальная скорость(км\ч): {self.max_speed}\nОбъём двигателя(куб.см): {self.engine_capacity}\nМакс. кол-во оборотов (rpm): {self.rotation_speed}\nПе?: {self.pe}")
    def engine_power_calc(self):
        print(f"{self.pe * self.rotation_speed / 7025:.2f} л.с. ({self.pe * self.rotation_speed / 9550:.2f} н.м.)")