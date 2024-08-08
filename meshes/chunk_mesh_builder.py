from settings import *


def is_void(voxel_pos, chunk_voxels):
  x, y, z = voxel_pos

  if 0 <= x < CHUNK_SIZE and 0 <= y <= CHUNK_SIZE and 0 <= z < CHUNK_SIZE:
    if chunk_voxels[x + CHUNK_SIZE * z + CHUNK_AREA * y]:
      return False
    return True


def add_date(vertex_data, index, *vertices):
  for vertex in vertices:
    for attr in vertx:
      vertex_data[index] = attr
      index += 1
    return index


def build_chunk_mesh(chunk_voxels):
  vertex_data = np.empty(CHUNK_VOL * 18 * 5, dtype='uint8')
  index = 0

  for x in range(CHUNK_SIZE):
    for y in range(CHUNK_SIZE):
      for z in range(CHUNK_SIZE):
        voxel_id = chunk_voxels[x + CHUNK_SIZE * z + CHUNK_SIZE * y]
        if not voxel_id:
          continue

        if is_void((x, y + 1, z), chunk_voxels):
          v0 = (x, y + 1, z, voxel_id, 0)
          v1 = (x + 1, y + 1, z, voxel_id, 0)
          v2 = (x + 1, y + 1, z + 1, voxel_id, 0)
          v3 = (x, y + 1, z + 1, voxel_id, 0)

          index = add_data(vertex_data, index, v0, v3, v2, v0, v2, v1)
