from model import *

class Scene:
    def __init__(self, engine):
        self.engine = engine
        self.objects = []
        self.load()

    def load(self):
        engine = self.engine
        add = self.add_object

        n, s = 30, 3
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(engine, pos=(x, -s, z)))

        add(Cat(engine, pos=(0, -2, -10)))

    def add_object(self, obj):
        self.objects.append(obj)

    def update(self):
        for obj in self.objects:
            obj.update()

    def render(self):
        for obj in self.objects:
            obj.render()

    