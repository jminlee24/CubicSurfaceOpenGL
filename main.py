import math
import os
import sys

import glm
import moderngl as mgl
import pygame as pg


class GraphicsEngine:

  def __init__(self):
    pg.init()
    pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
    pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
    pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
    pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)

    pg.display.set_mode((800, 800), flags=pg.OPENGL | pg.DOUBLEBUF, vsync=False)
    self.ctx = mgl.create_context()

    self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)
    self.ctx.gc_mode = 'auto'

    self.clock = pg.time.Clock()
    self.delta_time = 0
    self.time = 0

    self.is_running = True

  def update(self):
    self.delta_time = self.clock.tick()
    self.time = pg.time.get_ticks()

    pg.display.set_caption(f'{self.clock.get_fps() : .0f}')

  def render(self):
    self.ctx.clear()
    pg.display.flip()

  def handle_events(self):
    for event in pg.event.get():
      if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE) or (event.type == pg.KEYDOWN and event.key == pg.K_q):
        self.is_runnning = False

  def run(self):
    while self.is_running:
      self.handle_events()
      self.update()
      self.render()
    pg.quit()
    sys.exit()


if __name__ == "__main__":

  app = GraphicsEngine()
  app.run()
