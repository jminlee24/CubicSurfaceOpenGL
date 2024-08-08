from settings import *

from meshes.quad_mesh import QuadMesh
from meshes.marching_cubes_mesh import MarchingCubesMesh

from objects.lines import Lines


class Scene:
  def __init__(self, app):
    self.app = app
    self.chunk = MarchingCubesMesh(self.app)
    self.lines = Lines(self.app)

  def update(self):
    pass

  def render(self):
    self.chunk.render()
