import random


class EatBehavior(object):
    def eat(self):
        pass


class Herbivore(EatBehavior):
    def eat(self):
        veggieChoices = ["Watermelon", "Celery", "Cabbage", "Lettuce"]
        print("is cronching on some " + random.choice(veggieChoices))


class Carne(EatBehavior):
    def eat(self):
        meatChoices = ["Chicken nuggets", "Pork",
                       "Beef", "a stray child that fell in... oops"]
        print("is eating " + random.choice(meatChoices))
