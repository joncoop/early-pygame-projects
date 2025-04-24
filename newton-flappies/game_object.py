class GameObject:

    #--- Class attributes ---
    x = 0
    y = 0
    w = 0
    h = 0    
    v_x = 0
    v_y = 0


    #--- Functions ---
    def move(self):
        self.x += self.v_x
        self.y += self.v_y

    
    def intersects(self, other):

        if self.x + self.w < other.x or \
           self.x > other.x + other.w or \
           self.y + self.h < other.y or \
           self.y > other.y + other.h:
            return False
        else:
            return True


    def __str__(self):
        return str(type(self)) + ' ' + \
               ' [x=' + str(self.x) + ', ' + \
               ' [y=' + str(self.y) + ', ' + \
               ' [w=' + str(self.w) + ', ' + \
               ' [h=' + str(self.h) + ', ' + \
               ' [v_x=' + str(self.v_x) + ', ' + \
               ' [v_y=' + str(self.v_y) + ']'
