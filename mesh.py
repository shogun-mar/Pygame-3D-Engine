from vao import VAO
from texture import Texture

class Mesh:
    def __init__(self, engine):
        self.engine = engine
        self.vao = VAO(engine.ctx)
        self.texture = Texture(engine.ctx)

    def destroy(self):
        self.vao.destroy()
        self.texture.destroy()