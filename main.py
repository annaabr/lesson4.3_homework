import json


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")

    def info(self):
        return f"This is an animal {self.__class__.__name__} named {self.name}, aged {self.age} years"

    def eat(self):
        return f"{self.name} is eating."


class Bird(Animal):
    def make_sound(self):
        return f"{self.name} says chirp!"


class Mammal(Animal):
    def make_sound(self):
        return f"{self.name} says roar!"


class Reptile(Animal):
    def make_sound(self):
        return f"{self.name} says hsss!"

def animal_info(animals):
    for animal in animals:
        print(animal.info())


def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

def animal_info(animals):
    for animal in animals:
        print(animal.info())


class Employee:
    def __init__(self, name):
        self.name = name

    def works_with_animals(self):
        raise NotImplementedError("Subclasses must implement this method")


class ZooKeeper(Employee):
    def works_with_animals(self, animal):
        return f"{self.name} is feeding {animal.name}."


class Veterinarian(Employee):
    def works_with_animals(self, animal):
        return f"{self.name} is healing {animal.name}."


def employee_info(employee,animals):
    for somebody in employee:
        for animal in animals:
            print(somebody.works_with_animals(animal))

class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def save_zoo(self, filename):
        zoo_data = {
            "animals": [{"name": animal.name, "age": animal.age, "type": animal.__class__.__name__} for animal in
                        self.animals],
            "employees": [employee.name for employee in self.employees]
        }
        with open(filename, 'w') as f:
            json.dump(zoo_data, f)

    def load_zoo(self, filename):
        with open(filename, 'r') as f:
            zoo_data = json.load(f)
            for animal_data in zoo_data['animals']:
                if animal_data['type'] == 'Bird':
                    animal = Bird(animal_data['name'], animal_data['age'])
                elif animal_data['type'] == 'Mammal':
                    animal = Mammal(animal_data['name'], animal_data['age'])
                elif animal_data['type'] == 'Reptile':
                    animal = Reptile(animal_data['name'], animal_data['age'])
                self.add_animal(animal)
            for employee_name in zoo_data['employees']:
                self.add_employee(Employee(employee_name))


# Пример использования
zoo = Zoo()

# Добавление животных
zoo.add_animal(Bird("Parrot", 2))
zoo.add_animal(Mammal("Lion", 5))
zoo.add_animal(Reptile("Snake", 3))

# Добавление сотрудников
zoo.add_employee(ZooKeeper("Alice"))
zoo.add_employee(Veterinarian("Bob"))

print("Демонстрация полиморфизма:")
print("Creating a zoo:")
animal_sound(zoo.animals)
print()
animal_info(zoo.animals)
print()
employee_info(zoo.employees, zoo.animals)


# Сохранение состояния зоопарка
zoo.save_zoo("zoo_data.json")

# Создание нового зоопарка и загрузка данных
print("\nRestoring a zoo from a json file.")
new_zoo = Zoo()
new_zoo.load_zoo("zoo_data.json")

print("\nПроверка загруженных данных\n")
animal_sound(new_zoo.animals)
print()
animal_info(zoo.animals)
print()
employee_info(zoo.employees, zoo.animals)