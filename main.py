import pygame as pg
import moderngl as mgl
import sys
from settings import *

from camera import Camera
from triangle import Triangle
from cube import Cube

class GraphicsEngine:
    def __init__(self, window_title):
        #Init pygame modules
        pg.init()
        #Set opengl attributes
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3) #OpenGL 3.3 version
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE) #Core profile to exclude deprecated functions
        #Create opengl context
        pg.display.set_mode(WINDOW_SIZE, FLAGS) #Double buffering provides two complete color buffers one for display and one for drawing that switch roles after each frame
        self.ctx = mgl.create_context() #Create moderngl context from already existing opengl context
        #self.ctx.front_face = 'cw' #Set the front face of the cube to clockwise to see the internal faces
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE) #Enable depth test flag (maybe synonym of z buffering) and cull face flag to not render invisible faces
        pg.display.set_caption(window_title) #Set window title
        #Clock object
        self.clock = pg.time.Clock()
        self.time = 0
        #Camera object
        self.camera = Camera(self)
        #Scene objects
        self.scene = Cube(self)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.scene.destroy() #Remove all resources
                pg.quit()
                sys.exit()

    def update(self):
        #Update time
        self.update_time()
        #Update the scene
        self.scene.update()

    def render(self):
        #Clear the framebuffer with a color
        self.ctx.clear(color = (0.08, 0.16, 0.18))
        #Render the scene
        self.scene.render()
        #Swap the buffers
        pg.display.flip()
    
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.render()
            self.clock.tick(60)

    def update_time(self):
        self.time = pg.time.get_ticks() * 0.001

if __name__ == "__main__":
    engine = GraphicsEngine("ModernGL 3D Graphics")
    engine.run()