#version 330 core 
//Define opengl version and context profile mask

layout (location = 0) out vec4 fragColor; //4 component vector to contain RGBA values

in vec2 uv_0;

void main() {
    vec3 color = vec3(1.0, uv_0.x, 1.0);
    fragColor = vec4(color, 1.0); //Red with full opacity
    
}