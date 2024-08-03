import glm
import pygame as pg
import numpy as np

class Cube:
    def __init__(self, engine):
        self.engine = engine
        self.ctx = engine.ctx
        self.vbo = self.get_vbo()
        self.shader_program = self.get_shader_program("default")
        self.vao = self.get_vao()
        self.m_model = self.get_model_matrix()
        self.texture = self.get_texture(path = 'textures/crate.jpg')
        self.on_init()

    def get_texture(self, path):
        texture = pg.image.load(path).convert_alpha()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True) #Flip the image vertically because in pygame the y axis down and in opengl it extends up
        texture = self.ctx.texture(size = texture.get_size(), components = 3,
                                   data = pg.image.tostring(texture, 'RGB'))
        
        return texture

    def get_model_matrix(self):
        m_model = glm.mat4(1.0) #Identity matrix
        return m_model

    def on_init(self): #Pass the projection matrix from the camera instance to the shader program
        #Texture
        self.shader_program['u_texture_0'] = 0
        self.texture.use()
        #Matrices
        self.shader_program['m_proj'].write(self.engine.camera.m_proj)
        self.shader_program['m_view'].write(self.engine.camera.m_view)
        self.shader_program['m_model'].write(self.m_model)

    def update(self):
        m_model = glm.rotate(self.m_model, self.engine.time * 0.5, glm.vec3(0, 1, 0))
        self.shader_program['m_model'].write(m_model)
        self.shader_program['m_view'].write(self.engine.camera.m_view) #Update view matrix because the camera moving changes the view matrix

    def render(self):
        self.vao.render()

    def destroy(self): #Method to remove all resources since there's no garbage collector in moderngl
        self.vao.release()
        self.vbo.release()
        self.shader_program.release()

    def get_vertex_data(self):
        vertices = [(-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1),
                    (-1, 1, -1), (-1, -1, -1), (1, -1, -1), (1, 1, -1)] #In opengl the origin is at the center of the screen
        
        #In opengl by default the order of describing vertices is counter-clockwise
        indices = [(0, 2, 3), (0, 1, 2),
                   (1, 7, 2), (1, 6, 7),
                   (6, 5, 4), (4, 7, 6),
                   (3, 4, 5), (3, 5, 0),
                   (3, 7, 4), (3, 2, 7),
                   (0, 6, 1), (0, 5, 6)]
        
        vertex_data = self.get_data(vertices, indices)

        tex_coord = [(0, 0), (1, 0), (1, 1), (0, 1)] #Coordinates of the vertices of one face of the cube in local object space
        tex_coord_indices = [(0, 2, 3), (0, 1, 2),
                             (0, 2, 3), (0, 1, 2),
                             (0, 1, 2), (2, 3, 0),
                             (2, 3, 0), (2, 0, 1),
                             (0, 2, 3), (0, 1, 2),
                             (3, 1, 2), (3, 0, 1)]
        tex_coord_data = self.get_data(tex_coord, tex_coord_indices)

        vertex_data = np.hstack([tex_coord_data, vertex_data]) #Horizontally stack the vertex data and the texture coordinate data

        return vertex_data 
        
    @staticmethod #Utility function to get the data from the vertices and indices
    def get_data(vertices, indices):
        #Associate the indices in indices to the corresponding vertices in vertices
        #for example (0, 2, 3) means that the first triangle is formed by the vertices at index 0, 2, 3
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

    def get_vbo(self): #Get the vertex buffer object to sent to GPU memory
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        return vbo
    
    def get_shader_program(self, shader_name): #Load the shader program
        with open(f"shaders/vertex/{shader_name}.vert", "r") as file:
            vertex_shader = file.read()

        with open(f"shaders/fragment/{shader_name}.frag", "r") as file:
            fragment_shader = file.read()

        #Compile both shaders from source code and combine them in a shader program
        shader_program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return shader_program
    
    def get_vao(self):
        #Create a vertex array object to store the vertex buffer object and the shader program (3f means 3 floats per vertex, in_position is the name of the attribute in the vertex shader)
        vao = self.ctx.vertex_array(self.shader_program, [(self.vbo, ' 2f 3f', 'in_texcoord_0', 'in_position')])
        #2floats for the texture coordinates and 3 floats for the position
        return vao