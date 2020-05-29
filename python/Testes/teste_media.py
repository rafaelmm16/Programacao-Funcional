class Media(object):

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def media(self):
        return self.a + self.b + self.c + self.d / 4

from Media import calculadora
f = calculadora(4,6,5,2)
print("media:", f.media())
