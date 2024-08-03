#version 330 core 
//Define opengl version and context profile mask

layout (location = 0) out vec4 fragColor; //4 component vector to contain RGBA values

in vec2 uv_0;

uniform sampler2D u_texture_0;

void main() {
    vec3 color = texture(u_texture_0, uv_0).rgb;
    fragColor = vec4(color, 1.0); //Red with full opacity
    
}