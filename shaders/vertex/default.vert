#version 330 core 
//Define opengl version and context profile mask

//Input position
layout (location = 0) in vec3 in_position; //Layout specifies the location of the input variable, the keyword in specifies that the variable is an input variable.
                                           // In this case location indicates that the in_position variable is bound to the first attribute location.

uniform mat4 m_proj; //Uniform variable = global variable that remains constant for the duration of a rendering call
                     //mat4 is a GLSL data type representing a 4 by 4 matrix.
                     //m_proj means projection matrix, which is the projection matrix used to transfrom coordinates from the camera space to the clip space
                     //and it defines how a 3d scene is projected onto a 2d screen, including perspective or orthographic projection (orthographic projection is a type of projection which does not account for the perspective effect, meaning objects retain their size regardless of their distance to the camera)

void main() {
    gl_Position = m_proj * vec4(in_position.xy, in_position.z - 4.5, 1.0); //Four component vector
}