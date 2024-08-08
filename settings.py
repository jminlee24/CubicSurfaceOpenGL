import numpy as np
import math
import glm

# resolution
WIN_RES = glm.vec2(1600, 800)

# chunk
CHUNK_SIZE = 32
H_CHUNK_SIZE = CHUNK_SIZE // 2
CHUNK_AREA = CHUNK_SIZE * CHUNK_SIZE
CHUNK_VOL = CHUNK_AREA * CHUNK_SIZE

# camera
ASPECT_RATIO = WIN_RES.x / WIN_RES.y
FOV_DEG = 90
V_FOV = glm.radians(FOV_DEG)
H_FOV = 2 * math.atan(math.tan(V_FOV * .5) * ASPECT_RATIO)
NEAR = 0.1
FAR = 2000.0
PITCH_MAX = glm.radians(90)

# player
PLAYER_SPEED = .05
PLAYER_ROT_SPEED = .003
PLAYER_POS = glm.vec3(0, 0, 0)
MOUSE_SENS = .002
ZOOM_SPEED = 1

# colors
BG_COLOR = glm.vec3(0, 0, .1)
