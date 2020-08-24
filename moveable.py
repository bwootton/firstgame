class Movable(object):

    def __init__(self, screen, image, init_x, init_y):
        self.screen = screen
        self.image = image
        self.delta_x = 0
        self.delta_y = 0
        self.x = init_x
        self.y = init_y
        self._set_bg_limits()

    def _set_bg_limits(self):
        (self.width, self.height) = self.screen.get_size()
        print("{},{}".format(self.width, self.height))
    def set_delta(self, x, y):
        self.delta_x += x
        self.delta_y += y

    def clear_delta(self):
        self.delta_x = 0
        self.delta_y = 0

    def do_it(self):
        self.x += self.delta_x
        self.y += self.delta_y
        if self.y > self.height-50:
            self.y = self.height-50
            self.delta_y = 0
        if self.y < 0:
            self.y = 0
            self.delta_y = 0
        if self.x > self.width-50:
            self.x = self.width-50
            self.delta_x = 0
        if self.x < 0:
            self.x = 0
            self.delta_x = 0

        print(self.x, self.y)
        self.screen.blit(self.image, (self.x, self.y))
