import pygame as pg
from camera import Camera
from settings import *


class Player(Camera):
  def __init__(self, app, position=PLAYER_POS, yaw=-90, pitch=0):
    self.app = app
    super().__init__(position, yaw, pitch)

  def update(self):
    self.keyboard_control()
    self.mouse_control()
    super().update()

  def mouse_control(self):

    mouse_dx, mouse_dy = pg.mouse.get_rel()

    b1, b2, b3 = pg.mouse.get_pressed(num_buttons=3)

    if (b1):
      if mouse_dx:
        self.move_left(mouse_dx * MOUSE_SENS)
      if mouse_dy:
        self.move_up(mouse_dy * MOUSE_SENS)

    if (b3):
      if mouse_dx:
        self.rotate_yaw(mouse_dx * MOUSE_SENS)
      if mouse_dy:
        self.rotate_pitch(mouse_dy * MOUSE_SENS)

  def zoom_in(self, dx):
    self.move_forward(dx * ZOOOM_SPEED)

  def keyboard_control(self):
    key_state = pg.key.get_pressed()
    vel = PLAYER_SPEED * self.app.delta_time

    if key_state[pg.K_w]:
      self.move_forward(vel)
    if key_state[pg.K_s]:
      self.move_backward(vel)
    if key_state[pg.K_a]:
      self.move_left(vel)
    if key_state[pg.K_d]:
      self.move_right(vel)
    if key_state[pg.K_q]:
      self.move_up(vel)
    if key_state[pg.K_e]:
      self.move_down(vel)
