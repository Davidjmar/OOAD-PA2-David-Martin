class SpeakBehavior(object):
    def makeNoise(self):
        pass


class RoarSound(SpeakBehavior):
    def makeNoise(self):
        print("ROARRRRR")


class MeowSound(SpeakBehavior):
    def makeNoise(self):
        print("I'm a kitty kitty cat. m-e-owwwwww")


class HuffSound(SpeakBehavior):
    def makeNoise(self):
        print("Hufffff, *kicks dirt up with horn*")


class BarkSound(SpeakBehavior):
    def makeNoise(self):
        print("AWOOOOOOOOOOOOOOOOOO *in a badass wild tone*")
