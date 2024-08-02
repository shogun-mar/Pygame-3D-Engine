import glm
from settings import *

#Camera frustum settings
FOV = 50
NEAR = 0.1
FAR = 100

class Camera:
    def __init__(self, engine):
        self.engine = engine
        self.aspect_ratio = WINDOW_SIZE[0] / WINDOW_SIZE[1]
        #Projection matrix
        self.m_proj = self.get_projection_matrix()

    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)
