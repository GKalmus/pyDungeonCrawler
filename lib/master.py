class Klass:
    def __init__(self):
        self.x = 0

class Alamklass(Klass):
    def __init__(self):
        self.y = 1

    def su(self):
        return "su"

a = Klass()
b = Alamklass()
print(a.su())