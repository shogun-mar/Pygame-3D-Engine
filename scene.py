from model import *

class Scene:
    def __init__(self, engine):
        self.engine = engine
        self.objects = []
        self.load()

    def load(self):
        self.add_object(Cube(self.engine, texture_id = 0, pos = (0, 2, 0)))
        self.add_object(Cube(self.engine, texture_id = 0, pos = (-2.5, 0, 2)))
        self.add_object(Cube(self.engine, texture_id = 0, pos = (2.5, 0, -2)))

    def add_object(self, obj):
        self.objects.append(obj)

    def update(self):
        for obj in self.objects:
            obj.update()

    def render(self):
        for obj in self.objects:
            obj.render()

    