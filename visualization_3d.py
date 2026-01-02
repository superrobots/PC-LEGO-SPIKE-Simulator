from ursina import *
from ursina.shaders import lit_with_shadows_shader

def create_hub():
    # Light gray hub body matching real LEGO Spike Hub color with rounded edges
    # Use multiple components to create more realistic hub shape
    main_body = Entity(
        model='cube',
        color=color.rgb(210, 210, 210),
        scale=(2.5, 1.2, 3.5),
        position=(0, 0, 0),
        shader=lit_with_shadows_shader
    )
    
    # Add subtle rounded edges by adding small corner pieces
    corner_radius = 0.15
    corners = []
    for x in [-1.25, 1.25]:
        for y in [-0.6, 0.6]:
            for z in [-1.75, 1.75]:
                corner = Entity(
                    model='sphere',
                    color=color.rgb(210, 210, 210),
                    scale=corner_radius,
                    position=(x, y, z),
                    shader=lit_with_shadows_shader
                )
                corners.append(corner)
    
    return main_body

def create_logo_and_button():
    # Yellow square LEGO logo on the front (matching real hub) with better depth
    logo_base = Entity(
        model='cube',
        color=color.rgb(255, 204, 0),
        scale=(0.8, 0.12, 0.8),
        position=(0, 0.65, -1.85),
        shader=lit_with_shadows_shader
    )
    # Add embossed effect with slightly raised center
    logo_top = Entity(
        model='cube',
        color=color.rgb(255, 215, 20),
        scale=(0.7, 0.02, 0.7),
        position=(0, 0.72, -1.86),
        shader=lit_with_shadows_shader
    )
    Text(text='LEGO', position=(0, 0.75, -1.87), origin=(0, 0), scale=1.8, color=color.rgb(220, 0, 0))
    
    # Circular Bluetooth/power button with better appearance
    button_base = Entity(
        model='cylinder',
        color=color.rgb(90, 190, 230),
        scale=(0.28, 0.12, 0.28),
        position=(0.85, 0.65, -1.6),
        rotation=(90, 0, 0),
        shader=lit_with_shadows_shader
    )
    # Add button highlight
    button_highlight = Entity(
        model='sphere',
        color=color.rgb(140, 220, 255),
        scale=(0.15, 0.04, 0.15),
        position=(0.85, 0.72, -1.6),
        shader=lit_with_shadows_shader
    )
    
    return logo_base, button_base

def create_ports():
    port_labels = ['A','B','C','D','E','F']
    # Place ports on left and right sides of hub, matching real LEGO Spike Hub layout
    y_pos = 0.1  # Middle height of the hub
    x_left = -1.35
    x_right = 1.35
    z_positions = [-1.0, -0.3, 0.4, 1.1]  # Spread vertically
    ports = []
    
    for i, z in enumerate(z_positions[:3]):
        # Left side ports (A, B, C) - black rectangular ports with depth
        port_outer = Entity(
            model='cube',
            color=color.rgb(50, 50, 50),
            scale=(0.2, 0.35, 0.45),
            position=(x_left, y_pos, z),
            shader=lit_with_shadows_shader
        )
        # Inner port hole (darker)
        port_inner = Entity(
            model='cube',
            color=color.rgb(20, 20, 20),
            scale=(0.12, 0.25, 0.35),
            position=(x_left - 0.05, y_pos, z),
            shader=lit_with_shadows_shader
        )
        ports.append(port_outer)
        Text(text=port_labels[i], position=(x_left-0.28, y_pos+0.2, z), origin=(0,0), scale=1.6, color=color.white)
        
    for i, z in enumerate(z_positions[:3]):
        # Right side ports (D, E, F) - black rectangular ports with depth
        port_outer = Entity(
            model='cube',
            color=color.rgb(50, 50, 50),
            scale=(0.2, 0.35, 0.45),
            position=(x_right, y_pos, z),
            shader=lit_with_shadows_shader
        )
        # Inner port hole (darker)
        port_inner = Entity(
            model='cube',
            color=color.rgb(20, 20, 20),
            scale=(0.12, 0.25, 0.35),
            position=(x_right + 0.05, y_pos, z),
            shader=lit_with_shadows_shader
        )
        ports.append(port_outer)
        Text(text=port_labels[i+3], position=(x_right+0.28, y_pos+0.2, z), origin=(0,0), scale=1.6, color=color.white)
        
    return ports

def create_motors():
    # Place motors away from hub to avoid overlap
    motor_a = Entity(model='cube', color=color.light_gray, scale=(0.3,0.3,0.3), position=(-1.5,-0.3,1.2))
    motor_b = Entity(model='cube', color=color.light_gray, scale=(0.3,0.3,0.3), position=(1.5,-0.3,1.2))
    motor_c = Entity(model='cube', color=color.light_gray, scale=(0.3,0.3,0.3), position=(1.5,0.7,0.0))
    for m, label in zip([motor_a, motor_b, motor_c], ['Motor A', 'Motor B', 'Motor C']):
        Text(text=label, position=(m.x, m.y+0.2, m.z), origin=(0,0), scale=1.5, color=color.black)
    return motor_a, motor_b, motor_c

def create_wheels_and_arm():
    # Wheels: blue cubes, blocky and always visible
    wheel_scale = (0.3, 1.2, 1.2)
    wheel_y = -0.25
    wheel_z = 1.2
    left_wheel = Entity(model='sphere', color=color.azure, scale=wheel_scale, position=(-2.0, wheel_y, wheel_z))
    right_wheel = Entity(model='sphere', color=color.azure, scale=wheel_scale, position=(2.0, wheel_y, wheel_z))
    # Arm on the right side, away from hub
    arm = Entity(model='cube', color=color.orange, scale=(0.2,0.7,0.2), position=(2.0,0.0,0.0))
    return left_wheel, right_wheel, arm

def draw_connection(start, end, color=color.yellow):
    from ursina.mesh_importer import Mesh
    Entity(model=Mesh(vertices=[start, end], mode='line'), color=color, scale=1)

def create_connections(ports, motors, wheels_and_arm):
    # Port to motor
    for port, motor in zip(ports[:3], motors):
        draw_connection(port.position, motor.position, color=color.azure)
    # Motor to wheel/arm
    for motor, part in zip(motors, wheels_and_arm):
        draw_connection(motor.position, part.position, color=color.gray)

def create_light_matrix():
    light_matrix = []
    light_matrix_size = 5
    led_size = 0.24
    # Place LED matrix on the front face of hub (Z is forward/back, front is negative Z)
    hub_front_z = -1.77  # Front face of the hub
    matrix_start_x = -0.48 * (light_matrix_size-1)/2
    matrix_start_y = -0.48 * (light_matrix_size-1)/2
    
    # Create a slight recess for the LED matrix
    matrix_background = Entity(
        model='cube',
        color=color.rgb(40, 40, 40),
        scale=(1.3, 1.3, 0.05),
        position=(0, 0, hub_front_z + 0.02),
        shader=lit_with_shadows_shader
    )
    
    for row in range(light_matrix_size):
        row_items = []
        for col in range(light_matrix_size):
            # LEDs with more realistic appearance - slightly rounded
            led_base = Entity(
                model='cube',
                color=color.rgb(25, 25, 25),
                scale=(led_size, led_size, 0.06),
                position=(matrix_start_x+col*0.48, matrix_start_y+row*0.48, hub_front_z),
                shader=lit_with_shadows_shader
            )
            # Add LED lens effect
            led_lens = Entity(
                model='sphere',
                color=color.rgb(30, 30, 30),
                scale=(led_size * 0.7, led_size * 0.7, 0.03),
                position=(matrix_start_x+col*0.48, matrix_start_y+row*0.48, hub_front_z - 0.04),
                shader=lit_with_shadows_shader
            )
            row_items.append(led_base)
        light_matrix.append(row_items)
    return light_matrix

def set_light_matrix(light_matrix, matrix):
    for row in range(len(light_matrix)):
        for col in range(len(light_matrix[row])):
            # Bright white with slight glow effect when on, dark when off
            if matrix[row][col]:
                light_matrix[row][col].color = color.rgb(255, 255, 255)
                # Make lit LEDs slightly larger to simulate glow
                light_matrix[row][col].scale = (0.26, 0.26, 0.06)
            else:
                light_matrix[row][col].color = color.rgb(25, 25, 25)
                light_matrix[row][col].scale = (0.24, 0.24, 0.06)

app = Ursina()

# Add better lighting for more realistic appearance
sun = DirectionalLight(shadow_map_resolution=(2048, 2048))
sun.look_at(Vec3(1, -1, -1))

# Add ambient light
AmbientLight(color=color.rgba(255, 255, 255, 0.4))

# Additional fill light from the front
front_light = PointLight(position=(0, 1, -5), color=color.rgba(200, 200, 255, 0.3))

hub = create_hub()
logo, button = create_logo_and_button()
ports = create_ports()
motors = create_motors()
wheels_and_arm = create_wheels_and_arm()
create_connections(ports, motors, wheels_and_arm)
light_matrix = create_light_matrix()

# Example: turn on a diagonal
matrix = [[1 if i==j else 0 for j in range(5)] for i in range(5)]
set_light_matrix(light_matrix, matrix)

EditorCamera()
camera.position = (4, 3.5, -9)
camera.look_at(hub)

# Add a subtle background color
window.color = color.rgb(245, 245, 250)

app.run()
