import numpy as np

class Triangle:
    def __init__(self, engine):
        self.engine = engine
        self.ctx = engine.ctx
        self.vbo = self.get_vbo()
        self.shader_program = self.get_shader_program("default")
        self.vao = self.get_vao()

    def render(self):
        self.vao.render()

    def destroy(self): #Method to remove all resources since there's no garbage collector in moderngl
        self.vao.release()
        self.vbo.release()
        self.shader_program.release()

    def get_vertex_data(self):
        vertex_data = [(-0.6, -0.8, 0.0), (0.6, -0.8, 0.0), (0.0, 0.8, 0.0)] #In opengl the origin is at the center of the screen
        return np.array(vertex_data, dtype='f4') #Float32 data type
        
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