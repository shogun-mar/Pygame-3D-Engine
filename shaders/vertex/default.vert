#version 330 core 
//Define opengl version and context profile mask

//Input position
layout (location = 0) in vec2 in_texcoord_0;
layout (location = 1) in vec3 in_normal;
layout (location = 2) in vec3 in_position;

out vec2 uv_0;
out vec3 normal;
out vec3 fragPos;

uniform mat4 m_proj; //Uniform variable = global variable that remains constant for the duration of a rendering call
                     //mat4 is a GLSL data type representing a 4 by 4 matrix.
                     //m_proj means projection matrix, which is the projection matrix used to transfrom coordinates from the camera space to the clip space
                     //and it defines how a 3d scene is projected onto a 2d screen, including perspective or orthographic projection (orthographic projection is a type of projection which does not account for the perspective effect, meaning objects retain their size regardless of their distance to the camera)
uniform mat4 m_view; //View matrix, which is the view matrix used to transform coordinates from the world space to the camera space
uniform mat4 m_model; //Model matrix, which is the model matrix used to transform coordinates from the object space to the world space

void main() {
    uv_0 = in_texcoord_0; //Output texture coordinate
    fragPos = vec3(m_model * vec4(in_position,1.0)); //Position of the fragment in world space
    normal = mat3(transpose(inverse(m_model))) * normalize(in_normal); //Output normal vector (technically, multiplying the model matrix and input normal should work but only if the model is not uniformly scaled)
    gl_Position = m_proj * m_view *  m_model * vec4(in_position,1.0); //Four component vector
}