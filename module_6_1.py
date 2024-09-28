class Animal:
    def __init__(self, name):
        self.alive = True  # жива ли животное
        self.fed = False   # накормлено ли животное
        self.name = name   # имя животного

# Определяем класс Plant
class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name

class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)  # True
print(a2.fed)    # False
a1.eat(p1)      # Волк с Уолл-Стрит не стал есть Цветик семицветик
a2.eat(p2)      # Хатико съел Заводной апельсин
print(a1.alive)  # False
print(a2.fed)    # True