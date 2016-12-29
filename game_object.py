class Game_Object:
    def __init__(self, name):
        self.__name = name
        self.__sprite = None
        self.__x = 0
        self.__y = 0
        self.X_MAX = 640
        self.Y_MAX = 704

    # Setters and Getters

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def sprite(self):
        return self.__sprite

    @sprite.setter
    def sprite(self, value):
        self.__sprite = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if value > X_MAX:
            self.__x = X_MAX
        elif value < 0:
            self.__x = 0
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value > Y_MAX:
            self.__y = Y_MAX
        elif value < 0:
            self.__y = 0
        else:
            self.__y = value

    def pos(self):
        return self.x, self.y

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self.name)
