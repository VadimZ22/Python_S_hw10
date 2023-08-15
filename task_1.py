class Animal:
    def __init__(self, name, age, voice='groal'):
        self.name = name
        self.age = age
        self.voice = voice

    def make_voice(self):
        print(self.voice)


class Fish(Animal):
    def __init__(self, name, age, scales, voice):
        super().__init__(name, age, voice)
        self.scales = scales

    def action(self):
        print("i'm swiming")


class Dog(Animal):
    def __init__(self, name, age, breed, voice):
        super().__init__(name, age, voice)
        self.breed = breed

    def action(self):
        print('Bark!')


class Bird(Animal):
    def __init__(self, name, age, color, voice):
        super().__init__(name, age, voice)
        self.color = color

    def action(self):
        print('Fly!')


class Factory:

    def make_animal(self, type_c, name, age, param, voice):
        animal = type_c(name, age, param, voice)
        return animal


f = Factory()

animal_1 = f.make_animal(Bird, 'Chizh', 1, 'white', 'pi')
animal_1.action()
animal_2 = f.make_animal(Dog, 'Spark', 5, 'pitbull', 'bark')
animal_2.action()
animal_3 = f.make_animal(Fish, 'Nemo', 2, 'silver', 'bul')
animal_3.action()

# ___________ВЫВОД______________
# Fly!
# Bark!
# i'm swiming