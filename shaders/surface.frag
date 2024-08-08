#version 330 core

in vec3 color;

out vec4 fragColor;

#define M_PI 3.1415926535897932384626433832795

struct Ray{
  vec3 o;
  vec3 d;
};

void main(){
  vec3 new_color = abs(color);
  float disFromCenter = atan(dot(new_color, new_color) / 100) / M_PI + .5 ;

  fragColor = vec4(vec3(0.6, .3 + sin(exp(- new_color.y * new_color.y / 10)),  0.6) * disFromCenter , 1.0);
}