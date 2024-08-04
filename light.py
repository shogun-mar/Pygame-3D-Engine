import glm

class LightSource: #Phong reflection
    def __init__(self, position = (3, 3, -3), color = (1, 1, 1)):
        self.position = glm.vec3(position)
        self.color = glm.vec3(color)
        #Intensities
        self.ambient_intensity = 0.1 * self.color #Ambient light intentisity
        self.diffuse_intensity = 0.8 * self.color #Diffuse light intensity
        self.specular_intensity = 1.0 * self.color #Spectacular light intensity