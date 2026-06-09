#version 330

in vec3 in_vert;

in vec3 in_normal;

uniform mat4 u_transform;

uniform mat4 u_viewMatrix;

uniform mat4 u_projection;

uniform vec3 u_color;


out vec3 SurNormal;

out vec3 RGB;

out vec3 Dir;


void main() {
    
    mat4 MatrixComposed = u_transform * u_viewMatrix;
    
    mat3 NormalMatrix = mat3(MatrixComposed);
    
    
    NormalMatrix = inverse(NormalMatrix);
    NormalMatrix = transpose(NormalMatrix);
    
    SurNormal = normalize(NormalMatrix * in_normal);
    
    RGB = u_color;
    

    vec4 position = u_projection * u_viewMatrix * u_transform * vec4(in_vert, 1.0);
    
    gl_Position = position;

}