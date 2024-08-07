from settings import *


class Camera:
  def __init__(self, position, yaw, pitch):
    self.position = position
    self.yaw = yaw
    self.pitch = pitch

    self.up = glm.vec3(0, 1, 0)
    self.right = glm.vec3(1, 0, 0)
    self.forward = glm.vec3(0, 0, 1)

    self.m_proj = glm.perspective(V_FOV, ASPECT_RATIO, NEAR, FAR)
    self.m_view = glm.mat4()

  def update(self):
    self.update_vectors()
    self.update_view_matrix()

  def update_view_matrix(self):
    self.m_view = glm.lookAt(self.position, self.position + self.forward, self.up)

  def update_vectors(self):
    self.forward.x = glm.cos(self.yaw) * glm.cos(self.pitch)
    self.forward.y = glm.sin(self.pitch)
    self.forward.z = glm.sin(self.yaw) * glm.cos(self.pitch)

    self.forward = glm.normalize(self.forward)
    self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
    self.up = glm.normalize(glm.cross(self.right, self.forward))

  def rotate_pitch(self, dy):
    self.pitch -= dy
    self.pitch = glm.clamp(self.pitch, -PITCH_MAX, PITCH_MAX)

  def rotate_yaw(self, dx):
    self.yaw += dx

  def move_left(self, vel):
    self.position -= self.right * vel

  def move_right(self, vel):
    self.position += self.right * vel

  def move_up(self, vel):
    self.position += self.up * vel

  def move_down(self, vel):
    self.position -= self.up * vel

  def move_forward(self, vel):
    self.position += self.forward * vel

  def move_backward(self, vel):
    self.position -= self.forward * vel
