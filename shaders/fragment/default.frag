#version 330 core 
//Define opengl version and context profile mask

layout (location = 0) out vec4 fragColor; //4 component vector to contain RGBA values

//in vec2 uv_0; //Input from vertex shader

void main() {
    //Let all the fragments be red
    vec3 color = vec3(1, 0, 0);
    fragColor = vec4(color, 1.0); //Red with full opacity
    
}