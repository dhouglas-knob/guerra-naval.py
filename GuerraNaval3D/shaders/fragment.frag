#version 330

out vec4 f_color;

in vec3 SurNormal;
in vec3 RGB;

const float R_coeffecient = 0.04;

const float Power = 5.0; 

void main() {
    
    float theta = dot(normalize(vec3(0.01,0.01,0.01)),SurNormal);
    
    float ShlickAprroimation = R_coeffecient + (1 - R_coeffecient ) * pow(1 - theta, Power); // fresnel

    f_color = vec4(mix(RGB * 0.5, RGB, ShlickAprroimation),1.0);
    
}