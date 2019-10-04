import abc
from Action import *

# Initalize the Animal Class


class Animal(object):
    def __init__(self, name):
        __metaclass__ = abc.ABCMeta
        self.name = name
        self.family = None
        self.species = None
        self.roamBehavior = None
        self.speakBehavior = None
        self.eatBehavior = None

    def species(self):
        return self.species

    def family(self):
        return self.family

    def name(self):
        return self.name

    def noise(self, sb):
        self.speakBehavior = sb

    def eat(self, eb):
        self.eatBehavior = eb

    def exercise(self, rb):
        self.roamBehavior = rb

    def executeNoise(self):
        self.speakBehavior.makeNoise()

    def executeEat(self):
        self.eatBehavior.eat()

    def executeExercise(self):
        self.roamBehavior.roam()

    def printAnimal(self):
        print("This animal is a(n) " + self.getAnimalSpecies() + " of the " + self.getAnimalFamily()
              + " family, and its name is " + self.getAnimalName())
##########################

# Initialize the Felines
##########################


class Feline(Animal):
    def __init__(self, name):
        __metaclass__ = abc.ABCMeta
        super().__init__(name)
        self.name = name
        self.family = None
        self.species = "Feline"
        self.roamBehavior = ZoomiesRoam()
        self.eatBehavior = Carne()


class Cat(Feline):
    def __init__(self, name):
        super().__init__(name)
        self.speakBehavior = MeowSound()
        self.family = "Cat"


class Lion(Feline):
    def __init__(self, name):
        super().__init__(name)
        self.speakBehavior = MeowSound()
        self.family = "Lion"


class Tiger(Feline):
    def __init__(self, name):
        super().__init__(name)
        self.speakBehavior = MeowSound()
        self.family = "Tiger"
##########################

# Initialize the Canines
##########################


class Canine(Animal):
    def __init__(self, name):
        __metaclass__ = abc.ABCMeta
        super().__init__(name)
        self.name = name
        self.family = None
        self.species = "Canine"
        self.roamBehavior = ZoomiesRoam()
        self.eatBehavior = Carne()


class Dog(Canine):
    def __init__(self, name):
        __metaclass__ = abc.ABCMeta
        super().__init__(name)
        self.speakBehavior = BarkSound()
        self.family = "Dog"


class Wolf(Canine):
    def __init__(self, name):
        __metaclass__ = abc.ABCMeta
        super().__init__(name)
        self.speakBehavior = BarkSound()
        self.family = "Wolf"
##########################

# Initialize the Pachyderms
##########################


class Pachyderm(Animal):
    def __init__(self, name):
        __metaclass__ = abc.ABCMeta
        super().__init__(name)
        self.name = name
        self.family = None
        self.species = "Pachyderm"
        self.roamBehavior = StompingRoam()
        self.eatBehavior = Herbivore()


class Hippo(Pachyderm):
    def __init__(self, name):
        __metaclass__ = abc.ABCMeta
        super().__init__(name)
        self.speakBehavior = HuffSound()
        self.family = "Hippo"


class Elephant(Pachyderm):
    def __init__(self, name):
        __metaclass__ = abc.ABCMeta
        super().__init__(name)
        self.speakBehavior = HuffSound()
        self.family = "Elephant"


class Rhino(Pachyderm):
    def __init__(self, name):
        __metaclass__ = abc.ABCMeta
        super().__init__(name)
        self.speakBehavior = HuffSound()
        self.family = "Rhino"
##########################


class ZooKeeper():
    animalArray = [Hippo("Harry"), Hippo("Harvy"), Rhino("Roger"), Rhino("Ronny"), Elephant("Earl"), Elephant("Edgar"), Dog("Daryl"),
                   Dog("Dayna"), Wolf("Wesley"), Wolf("Wyatt"), Lion("Larry"), Lion("Linda"), Tiger("Tony"), Tiger("Terri"), Cat("Cathy"), Cat("Chris")]
