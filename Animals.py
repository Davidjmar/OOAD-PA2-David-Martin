import abc
from Action import *
from Action.Eat import *
from Action.Exercise import *
from Action.Noise import *

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

    def wake(self):
        print(self.name + " the " + self.family + " is awake!")

    def sleep(self):
        print(self.name + " the " + self.family +
              " reluctantly curls up and goes to bed...")

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
        self.roamBehavior = KittyExercise()
        self.eatBehavior = Carne()


class Cat(Feline):
    def __init__(self, name):
        super().__init__(name)
        self.speakBehavior = MeowSound()
        self.roamBehavior = KittyExercise2()
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

# Below in elephant I implemented the stategy pattern to override the pachyderm's default roam behavior to a secondary


class Elephant(Pachyderm):
    def __init__(self, name):
        __metaclass__ = abc.ABCMeta
        super().__init__(name)
        self.speakBehavior = HuffSound()
        self.roamBehavior = StompingRoam2()
        self.family = "Elephant"


class Rhino(Pachyderm):
    def __init__(self, name):
        __metaclass__ = abc.ABCMeta
        super().__init__(name)
        self.speakBehavior = HuffSound()
        self.roamBehavior = StompingRoam2()
        self.family = "Rhino"
##########################
