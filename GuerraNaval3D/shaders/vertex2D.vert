#version 330

in vec2 in_vert; 

uniform mat4 u_translate;

uniform vec2 u_uv;
uniform vec2 uv_offset;

out vec2 uv;

void main()
{
    gl_Position = u_translate * vec4(in_vert, 0.0 , 1.0);

    uv = ((in_vert * u_uv) + u_uv) + uv_offset;

}