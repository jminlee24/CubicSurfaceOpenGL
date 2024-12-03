import numpy as np
import struct

from meshes.base_mesh import BaseMesh
from skimage import measure


def f(x, y, z):
  return x * x + y * y + z * z - x * y * z - 4


def g(x, y, z):
  return x * x + y * y + z * z - 16


class MarchingCubesMesh(BaseMesh):
  def __init__(self, app):
    super().__init__()
    self.app = app
    self.ctx = app.ctx
    self.program = app.shader_program.chunk

    self.vbo_format = '3f 3f'
    self.attrs = ('in_position', 'in_color')
    self.vao = self.get_vao()

  def get_vertex_data(self):
    x_ = np.linspace(-10, 10, 400)

    x, y, z = np.meshgrid(x_, x_, x_)
    F = f(x, y, z)

    verts, faces, normals, values = measure.marching_cubes(F, 0, spacing=[np.diff(x_)[0]] * 3)

    verts = np.hstack([np.array(verts, dtype=np.float32), np.array(verts / 10, dtype=np.float32)])
    verts -= 10
    faces = np.array(faces, dtype=np.uint32)

    return verts, faces

  def get_vao(self):

    verts, index = self.get_vertex_data()

    vbo = self.ctx.buffer(verts)
    ibo = self.ctx.buffer(index)

    vao = self.ctx.vertex_array(
      self.program, [(vbo, self.vbo_format, 'in_position', 'in_color')], ibo, skip_errors=True
    )

    return vao
