# version 330 core 

//Define opengl version and context profile mask

layout (location = 0) in vec2 in_textcoord_0; //Texture coordinates
layout (location = 1) in vec3 in_position; //Layout specifies the location of the input variable, the keyword in specifies that the variable is an input variable.
                                           // In this case location indicates that the in_position variable is bound to the first attribute location.

out vec2 uv_0; //Output variable that will be passed to the fragment shader

uniform mat4 m_proj; //Uniform variable = global variable that remains constant for the duration of a rendering call
                     //mat4 is a GLSL data type representing a 4 by 4 matrix.
                     //m_proj means projection matrix, which is the projection matrix used to transfrom coordinates from the camera space to the clip space
                     //and it defines how a 3d scene is projected onto a 2d screen, including perspective or orthographic projection (orthographic projection is a type of projection which does not account for the perspective effect, meaning objects retain their size regardless of their distance to the camera)
uniform mat4 m_view; //Matrix that defines the view of the camera
uniform mat4 m_model;  //Matrix that transforms the vertex from local object space to world space

/*
Model Matrix (m_model): Transforms the vertex from local object space to world space.
View Matrix (m_view): Transforms the vertex from world space to camera (view) space.
Projection Matrix (m_proj): Transforms the vertex from camera space to clip space, which is then mapped to screen space.
*/

void main() {
    //uv_0 = in_textcoord_0; //Set the output variable uv_0 to the input variable in_textcoord_0
    gl_Position = m_model * m_view * m_proj * vec4(in_position, 1.0); //Four component vector
}