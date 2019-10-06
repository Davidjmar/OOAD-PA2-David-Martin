import abc
from abc import *
from Action import *
from Animals import *
import random

# OBSERVER PATTERN
# Below is the implementation of the observable pattern the announcer is an instance of the subject which is
# maintained and updated by the conreteSubject class


class subject(ABC):
    # Know its observers. Any number of Observer objects may observe a
    # subject.
    # Send a notification to its observers when its state changes.

    def __init__(self, name):
        self.name = None

    def update(self, message):
        pass


class concreteSubject(ABC):
    # Define an updating interface for objects that should be notified of
    # changes in a subject.

    def __init__(self):
        self._observers = set()

    def attach(self, observer):
        self._observers.add(observer)

    def detach(self, observer):
        self._observers.discard(observer)


class announcer(subject):
    # Implement the Observer updating interface to keep its state
    # consistent with the subject's.
    # Store state that should stay consistent with the subject's.
    def __init__(self, name):
        __metaclass__ = abc.ABCMeta
        super().__init__(name)
        self.name = name

    def update(self, announcement):
        print("Hi, this is the Zoo Announcer. The Zookeeper is about to " + announcement)


class zooKeeper(concreteSubject):

    def wake(self, announcement):
        for observer in self._observers:
            observer.update(announcement)
        print("\nGOOOOOOOOOD MOOOOOORNIIIIING Zoo!! \n")
        for animal in AnimalArray:
            (animal.executeNoise(), animal.wake())
            print()

    def rollCall(self, announcement):
        for observer in self._observers:
            observer.update(announcement)
        print("\nRoll Call!! Let's see if we had any runners last night! \n")
        for animal in AnimalArray:
            print("\n" + animal.name +
                  " the " + animal.family + " is here! \n")

    def exercise(self, announcement):
        for observer in self._observers:
            observer.update(announcement)
        print()
        print("\niiiiit's grind time, let's get that blood pumping! \n")
        for animal in AnimalArray:
            print(animal.name + " the " + animal.family +
                  " is at it, watch them go!!")
            (animal.executeExercise())
            print("\n")

    def feed(self, announcement):
        for observer in self._observers:
            observer.update(announcement)
        print()
        print("\n Chow Time!!! \n")
        for animal in AnimalArray:
            (print(animal.name + " the " + animal.family), (animal.executeEat()))
            print("\n")

    def sleep(self, announcement):
        for observer in self._observers:
            observer.update(announcement)
        print()
        print("\n Time for bed everyone!! \n")
        for animal in AnimalArray:
            (animal.sleep())
            print("\n")


if __name__ == "__main__":
    zoo_keeper = zooKeeper()
    zoo_announcer = announcer("Zoo Announcer")
    zoo_keeper.attach(zoo_announcer)
    # subject.attach(zoo_keeper)
    AnimalArray = [Hippo("Harry"), Hippo("Harvy"), Rhino("Roger"), Rhino("Ronny"), Elephant("Earl"), Elephant("Edgar"), Dog("Daryl"),
                   Dog("Dayna"), Wolf("Wesley"), Wolf("Wyatt"), Lion("Larry"), Lion("Linda"), Tiger("Tony"), Tiger("Terri"), Cat("Cathy"), Cat("Chris")]
    zoo_keeper.wake("wake up the animals")
    zoo_keeper.rollCall("roll call the animals")
    zoo_keeper.exercise("exercise and play with the animals")
    zoo_keeper.feed("feed the animals")
    zoo_keeper.sleep("send the animals to bed")
    zoo_keeper.detach(zoo_announcer)
