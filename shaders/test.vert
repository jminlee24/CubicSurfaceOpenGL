#version 330

uniform mat4 m_proj;
uniform mat4 m_model;
uniform mat4 m_view;

in vec3 vert;

void main() {
  gl_Position = m_proj * m_view * m_model * vec4(vert, 1.0);
}