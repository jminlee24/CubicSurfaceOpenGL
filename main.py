import math
import os
import sys

import glm
import moderngl as mgl
import pygame as pg

class GraphicsEngine:
    
    def __init__(self):
        pg.init()
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)
        
        pg.display.set_mode((800, 800), flags = pg.OPENGL | pg.DOUBLEBUF, vsync = True)
        self.ctx = mgl.create_context()
        
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)
        self.ctx.gc_mode = 'auto'
        
        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.time = 0
        
        self.is_running = True
        
    def update(self):
        return

    def render(self):
        return

if __name__ == "__main__":

    ctx = mgl.create_context()


