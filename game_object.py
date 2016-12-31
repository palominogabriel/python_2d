from pygame import display, Rect

class Game_Object(Rect):
    def __init__(self, name, screen):
        Rect.__init__(self,(0,0),(0,0))
        self.__name = name
        self.__screen = screen
        self.__sprite = None
        self.__x = 0
        self.__y = 0
        self.__width = 0
        self.__height = 0

    # Setters and Getters
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def screen(self):
        return self.__screen

    @screen.setter
    def screen(self, value):
        self.__screen = value

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
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    def pos(self):
        return self.x, self.y

    def update_pos(self,x,y):
        self.x = x
        self.y = y

    def get_screen_size(self):
        display_info = display.Info()
        return display_info.current_w, display_info.current_h

    def rectBox(self):
        self.rect = self.sprite.get_rect()
        self.image_w, self.image_h = self.sprite.get_size()
        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self.name)


