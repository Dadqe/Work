class Animal(object):
    def __init__(self, name):
        self.name = name

    def say(self):
        print(self.name + " хочет что-то сказать")

    def swim(self):
        print(self.name + " подходит к воде")


class Cat(Animal):
    def say(self):
        super(Cat, self).say()
        print(self.name + " говорит Мяу")

    def swim(self):
        super(Cat, self).swim()
        print(self.name + " боится воды")


class Dog(Animal):
    def say(self):
        super(Dog, self).say()
        print(self.name + " говорит Гав")

    def swim(self):
        super(Dog, self).swim()
        print(self.name + " плывет по-собачьи")


class CatDog(Cat,Dog):
    swim = Dog.swim

    def say(self):
        super(CatDog, self).say()

cat = Cat("Кот")
dog = Dog("Пес")
catDog = CatDog("КотоПес")

cat.say()
# Кот хочет что-то сказать
# Кот говорит Мяу

dog.say()
# Пес хочет что-то сказать
# Пес говорит Гав

catDog.say()
# КотоПес хочет что-то сказать
# КотоПес говорит Гав
# КотоПес говорит Мяу

cat.swim()
# Кот подходит к воде
# Кот боится воды

dog.swim()
# Пес подходит к воде
# Пес плывет по-собачьи

catDog.swim()
# КотоПес подходит к воде
# КотоПес плывет по-собачьи
# Наследование в Python