from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, type):
        self.type = type

    def which_type(self):
        return self.type

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):

    def move(self):
        print("Runs...")


class Cat(Animal):

    def move(self):
        print("Sleeps...")


class AnimalFactory:

    @staticmethod
    def create_animal(type_of_animal):
        if type_of_animal is "Dog":
            return Dog()

        if type_of_animal is "Cat":
            return Cat()

        raise ValueError("Animal not found")