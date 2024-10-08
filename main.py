import math
import os
import sys

import glm
import moderngl as mgl
import pygame as pg

from settings import *
from shader_program import ShaderProgram
from scene import Scene
from player import Player


class GraphicsEngine:

  def __init__(self):
    pg.init()
    pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
    pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
    pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
    pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)

    pg.display.set_mode(WIN_RES, flags=pg.OPENGL | pg.DOUBLEBUF)
    self.ctx = mgl.create_context()

    # mgl.CULL_FACE is not enabled since I want all sides when graphing
    self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.BLEND)
    self.ctx.gc_mode = 'auto'

    self.clock = pg.time.Clock()
    self.delta_time = 0
    self.time = 0

    self.is_running = True

    self.on_init()

  def on_init(self):
    self.player = Player(self)
    self.shader_program = ShaderProgram(self, "surface")
    self.scene = Scene(self)

  def update(self):
    self.player.update()
    self.shader_program.update()
    self.scene.update()

    self.delta_time = self.clock.tick()
    self.time = pg.time.get_ticks()

    pg.display.set_caption(f'{self.clock.get_fps() : .0f}')

  def render(self):
    self.ctx.clear(color=BG_COLOR)
    self.scene.render()
    pg.display.flip()

  def handle_events(self):
    for event in pg.event.get():
      if event.type == pg.KEYDOWN:
        if event.key == pg.K_ESCAPE or event.key == pg.K_z:
          self.is_running = False
      elif event.type == pg.MOUSEWHEEL:
        self.player.zoom_in(event.y)
      elif event.type == pg.QUIT:
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
