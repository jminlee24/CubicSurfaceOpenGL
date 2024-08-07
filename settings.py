import numpy as np
import math
import glm

# resolution
WIN_RES = glm.vec2(1600, 800)

# camera
ASPECT_RATIO = WIN_RES.x / WIN_RES.y
FOV_DEG = 90
V_FOV = glm.radians(FOV_DEG)
H_FOV = 2 * math.atan(math.tan(V_FOV * .5) * ASPECT_RATIO)
NEAR = 0.1
FAR = 2000.0
PITCH_MAX = glm.radians(90)

# player
PLAYER_SPEED = .005
PLAYER_ROT_SPEED = .003
PLAYER_POS = glm.vec3(0, 0, 1)
MOUSE_SENS = .002

# colors
BG_COLOR = glm.vec3(0, 0, .1)
