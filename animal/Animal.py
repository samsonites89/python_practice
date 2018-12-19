import requests


class Tiger:
    def jump(self):
        print("jump")
    def cry(self):
        print("어흥")


class Lion:
    def pounce(self):
        print("pounce")
    def cry(self):
        print("흥어")

class Liger(Lion,Tiger):
    def run(self):
        print("run")

bee = Liger()
bee.jump()
bee.pounce()
bee.run()
bee.cry()
print(Liger.__mro__)


