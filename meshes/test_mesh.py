import struct
import numpy as np

from meshes.base_mesh import BaseMesh


class TestMesh(BaseMesh):
  def __init__(self, app):
    super().__init__()

    self.app = app
    self.ctx = app.ctx
    self.program = app.shader_program.chunk
    self.vbo_format = '3f 3f'
    self.attrs = ('vert')
    self.vao = self.get_vao()

  def get_vertex_data(self):

    pass

  def get_vao(self):

    vbo = self.ctx.buffer(np.array([

      [-1, -1, -1],
      [+1, -1, -1],
      [+1, +1, -1],
      [-1, +1, -1],
      [-1, -1, +1],
      [+1, -1, +1],
      [+1, +1, +1],
      [-1, +1, +1],

    ], dtype="float32"))

    ibo = self.ctx.buffer(np.array([
      [0, 3, 1],
      [1, 3, 2],
      [0, 4, 7],
      [0, 7, 3],
      [4, 5, 6],
      [4, 6, 7],
      [5, 1, 2],
      [5, 2, 6],
      [2, 3, 6],
      [3, 7, 6],
      [0, 1, 5],
      [0, 5, 4],
    ], dtype="int32"))

    content = [
        (vbo, '3f', *['vert']),
    ]

    vao = self.ctx.vertex_array(self.program, content, ibo)

    return vao
