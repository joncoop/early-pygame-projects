class Player:

    # Attributes
    character = None
    controls = None
    name = None
    score = 0


    # Constructor
    def __init__(self, character, controls, name=None):
        self.character = character
        self.controls = controls
        self.name = name


    # Functions
    def __str__(self):
        return str(self.name)      + '\n' + \
               str(self.character) + '\n' + \
               str(self.controls)  + '\n' + \
               str(self.score)
