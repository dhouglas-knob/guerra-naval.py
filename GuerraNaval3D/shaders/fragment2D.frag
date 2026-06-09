#version 330
out vec4 FragColor;
  
uniform sampler2D u_texture;

in vec2 uv;

void main()
{
    FragColor = texture(u_texture, uv);
} 