class ShaderPrograms:
    def __init__(self, ctx):
        self.ctx = ctx
        self.programs = {}
        self.programs['default'] = self.get_shader_program('default')

    def get_shader_program(self, shader_name): #Load the shader program
        with open(f"shaders/vertex/{shader_name}.vert", "r") as file:
            vertex_shader = file.read()

        with open(f"shaders/fragment/{shader_name}.frag", "r") as file:
            fragment_shader = file.read()

        #Compile both shaders from source code and combine them in a shader program
        shader_program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return shader_program
    
    def destroy(self):
        [program.release() for program in self.programs.values()]