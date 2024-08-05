import pygame as pg
import moderngl as mgl
import sys
from settings import *

from camera import Camera
from model import *
from mesh import Mesh
from light import LightSource
from scene import Scene

class GraphicsEngine:
    def __init__(self, window_title):
        #Init pygame modules
        pg.init()
        #Mouse settings
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)
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
        self.delta_time = 0 #variable to keep movement speed and physics indipendent from framerate
        #Lightsource object
        self.light = LightSource()
        #Camera object
        self.camera = Camera(self)
        #Mesh object
        self.mesh = Mesh(self)
        #Scene objects
        self.scene = Scene(self)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.mesh.destroy() #Remove all resources
                pg.quit()
                sys.exit()

    def update(self):
        #Update time
        self.time = pg.time.get_ticks() * 0.001 #In seconds
        #Update the camera
        self.camera.update()
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
            self.delta_time = self.clock.tick(60)

if __name__ == "__main__":
    engine = GraphicsEngine("ModernGL 3D Graphics")
    engine.run()