from ursina import *

def create_hub():
    # White/light gray hub, slightly rounded by scaling
    return Entity(model='cube', color=color.yellow, scale=(2,1,3), position=(0,0,0))

def create_logo_and_button():
    # Yellow LEGO logo block on top
    logo = Entity(model='sphere', color=color.green, scale=(0.5,0.1,0.5), position=(0,0.6,-1.2))
    Text(text='LEGO', position=(0,0.7,-1.2), origin=(0,0), scale=2, color=color.red)
    # Green circular button near logo
    button = Entity(model='cube', color=color.green, scale=(0.18,0.05,0.18), position=(0.5,0.6,-1.2))
    return logo, button

def create_ports():
    port_labels = ['A','B','C','D','E','F']
    # Place ports on left and right sides of top surface, spaced to avoid overlap
    y_pos = 0.6  # Slightly above hub top
    x_left = -1.15
    x_right = 1.15
    z_positions = [-0.7, -0.25, 0.25, 0.7]  # Spread out more
    ports = []
    for i, z in enumerate(z_positions[:3]):
        # Left side ports (A, B, C)
        port = Entity(model='cube', color=color.azure, scale=(0.2,0.2,0.2), position=(x_left, y_pos, z))
        ports.append(port)
        Text(text=port_labels[i], position=(x_left-0.18, y_pos+0.08, z), origin=(0,0), scale=2, color=color.black)
    for i, z in enumerate(z_positions[:3]):
        # Right side ports (D, E, F)
        port = Entity(model='cube', color=color.azure, scale=(0.2,0.2,0.2), position=(x_right, y_pos, z))
        ports.append(port)
        Text(text=port_labels[i+3], position=(x_right+0.18, y_pos+0.08, z), origin=(0,0), scale=2, color=color.black)
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
    led_size = 0.18
    # Place on top surface of hub (Y is up)
    hub_top_y = 0.5  # hub center y=0, scale_y=1, so top is at y=+0.5
    matrix_start_x = -0.36 * (light_matrix_size-1)/2
    matrix_start_z = -0.36 * (light_matrix_size-1)/2
    y_pos = hub_top_y + led_size/2 + 0.01  # Slightly above hub
    for row in range(light_matrix_size):
        row_items = []
        for col in range(light_matrix_size):
            led = Entity(model='cube', color=color.black, scale=(led_size,led_size,led_size), position=(matrix_start_x+col*0.36, y_pos, matrix_start_z+row*0.36))
            row_items.append(led)
        light_matrix.append(row_items)
    return light_matrix

def set_light_matrix(light_matrix, matrix):
    for row in range(len(light_matrix)):
        for col in range(len(light_matrix[row])):
            light_matrix[row][col].color = color.yellow if matrix[row][col] else color.black

app = Ursina()

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
camera.position = (0,2,-8)
camera.look_at(hub)

app.run()
