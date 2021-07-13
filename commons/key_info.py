class KeyInfo:

    def __init__(self, x, y, code):
        self._x = x
        self._y = y
        self._code = code

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def code(self):
        return self._code

    @x.setter
    def x(self, x):
        if isinstance(x, str):
            self._x = int(x)
        elif isinstance(x, int):
            self._x = x

    @y.setter
    def y(self, y):
        if isinstance(y, str):
            self._y = int(y)
        elif isinstance(y, int):
            self._y = y

    @code.setter
    def code(self, code):
        self._code = code

    @x.deleter
    def x(self):
        del self._x

    @y.deleter
    def y(self):
        del self._y

    @code.deleter
    def code(self):
        del self._code

