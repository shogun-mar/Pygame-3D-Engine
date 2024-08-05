from vbo import VBOs
from shader_program import ShaderPrograms

class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbos = VBOs(ctx)
        self.shader_programs = ShaderPrograms(ctx)
        self.vaos = {}

        #Cube vao
        self.vaos['cube'] = self.get_vao(vbo = self.vbos.vbos['cube'], program = self.shader_programs.programs['default'])

    def get_vao(self, vbo, program):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)])
        return vao
    
    def destroy(self):
        #[vao.release() for vao in self.vaos.values()]
        self.vbos.destroy()
        self.shader_programs.destroy()