class GameObject:

    def __init__(self, x, y, width, height, v_x=0, v_y=0):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

        self.v_x = v_x
        self.v_y = v_y

    
    def move(self):
        self.x += self.v_x
        self.y += self.v_y


    def get_rect(self):
        return [self.x, self.y, self.width, self.height]


