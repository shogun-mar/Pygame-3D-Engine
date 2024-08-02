import numpy as np

class Cube:
    def __init__(self, engine):
        self.engine = engine
        self.ctx = engine.ctx
        self.vbo = self.get_vbo()
        self.shader_program = self.get_shader_program("default")
        self.vao = self.get_vao()
        self.on_init()

    def on_init(self): #Pass the projection matrix from the camera instance to the shader program
        self.shader_program['m_proj'].write(self.engine.camera.m_proj)

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
        return np.array(vertex_data, dtype='f4') #Float32 data type
        
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
        vao = self.ctx.vertex_array(self.shader_program, [(self.vbo, '3f', 'in_position')])
        #So in the buffer each vertex is assigned 3 float numbers and that group of numbers corresponds to an input attribute named in_position
        return vao