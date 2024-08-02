#version 330 core //Define opengl version and context profile mask

//Input position
layout (location = 0) in vec3 in_position; //Layout specifies the location of the input variable, the keyword in specifies that the variable is an input variable.
                                           // In this case location indicates that the in_position variable is bound to the first attribute location.


void main() {
    gl_Position = vec4(in_position, 1.0); //Four component vector

}