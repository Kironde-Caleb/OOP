class Speaker:
    def play_music(self):
        print("Boom am playing music")

class DancingRobot:
    def __init__(self):
        self.speaker = Speaker()

    def dance(self):
        self.speaker.play_music()
        print("Black Sheep by Ben Fuller")
        print("Living testimony by Terrian")
        print("I'd do it again by Andrew Ripp")

