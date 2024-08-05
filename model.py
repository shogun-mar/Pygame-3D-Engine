import glm
from random import randint

class BaseModel:
    def __init__(self, engine, vao_name, texture_id, pos = (0, 0, 0)):
        self.engine = engine
        self.pos = pos
        self.m_model = self.get_model_matrix()
        print(f"model matrix of object at pos: {self.pos} \n{self.m_model} \n")
        self.texture_id = texture_id
        self.vao = engine.mesh.vao.vaos[vao_name]
        self.shader_program = self.vao.program
        self.camera = self.engine.camera

    def update(self): ...

    def get_model_matrix(self):
        m_model = glm.mat4() #identity matrix
        #translation local object space position to world position
        m_model = glm.translate(m_model, self.pos)
        return m_model
    
    def render(self):
        self.vao.render()

class Cube(BaseModel):
    def __init__(self, engine, vao_name = 'cube', texture_id = 0, pos = (0, 0, 0)): #Default parameters that can be overwritten in the init call
        super().__init__(engine, vao_name, texture_id, pos) #vao_name is the name of the vao in the vao dictionary
        self.on_init()
        self.rotation_vec = glm.vec3(randint(0, 1), randint(0, 1), randint(0, 1))

    def on_init(self):
        #texture
        self.texture = self.engine.mesh.texture.textures[self.texture_id]
        self.shader_program['u_texture_0'] = 0
        self.texture.use()
        #light
        self.shader_program['light.position'].write(self.engine.light.position)
        self.shader_program['light.ambient_intensity'].write(self.engine.light.ambient_intensity)
        self.shader_program['light.diffuse_intensity'].write(self.engine.light.diffuse_intensity)
        self.shader_program['light.specular_intensity'].write(self.engine.light.specular_intensity)
        #matrices
        self.shader_program['m_proj'].write(self.camera.m_proj)
        self.shader_program['m_view'].write(self.camera.m_view)
        self.shader_program['m_model'].write(self.m_model)
    
    def update(self):
        self.texture.use()
        #self.m_model = glm.rotate(self.m_model, self.engine.time * 0.005, self.rotation_vec)
        self.shader_program['camPos'].write(self.camera.position)
        self.shader_program['m_model'].write(self.m_model)
        self.shader_program['m_view'].write(self.camera.m_view)
