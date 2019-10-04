class EatBehavior(object):
    def eat(self):
        pass


class Herbivore(EatBehavior):
    def eat(self):
        print("Cronching on some Hay and fruit")


class Carne(EatBehavior):
    def eat(self):
        print("Eating some meats!")
