#version 330 core 
//Define opengl version and context profile mask

layout (location = 0) out vec4 fragColor; //4 component vector to contain RGBA values

in vec2 uv_0;
in vec3 normal;
in vec3 fragPos;

struct Light {
    vec3 position;
    vec3 ambient_intensity;
    vec3 diffuse_intensity;
    vec3 specular_intensity;
};

uniform Light light;
uniform sampler2D u_texture_0;
uniform vec3 camPos;

vec3 getLight(vec3 color){ //Function that modifies the color to apply the light effect
    vec3 Normal = normalize(normal);
    
    //ambient light component
    vec3 ambient = light.ambient_intensity;

    //diffuse light component using lambert's law
    vec3 lightDir = normalize(light.position - fragPos);
    float diff = max(0, dot(lightDir, Normal)); //Without the max function the angle between the vectors could be negative resulting in incorrect lighting
    vec3 diffuse = light.diffuse_intensity * diff;

    //specular light component using phong's model
    vec3 viewDir = normalize(camPos-fragPos);
    vec3 reflectDir = reflect(-lightDir, Normal);
    float spec = pow(max(dot(viewDir, reflectDir), 0), 32);
    vec3 specular = light.specular_intensity * spec;

    return (ambient + diffuse + specular) * color;
}

void main() {
    vec3 color = texture(u_texture_0, uv_0).rgb;
    color = getLight(color);
    fragColor = vec4(color, 1.0); //Red with full opacity
    
}