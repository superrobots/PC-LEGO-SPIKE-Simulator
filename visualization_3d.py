from ursina import *

def create_hub():
    # Light gray hub body matching real LEGO Spike Hub color
    return Entity(model='cube', color=color.rgb(200, 200, 200), scale=(2.5, 1.2, 3.5), position=(0,0,0))

def create_logo_and_button():
    # Yellow square LEGO logo on the front (matching real hub)
    logo = Entity(model='cube', color=color.rgb(255, 204, 0), scale=(0.7, 0.05, 0.7), position=(0, 0.7, -1.8))
    Text(text='LEGO', position=(0, 0.75, -1.8), origin=(0, 0), scale=2, color=color.rgb(200, 0, 0))
    # Circular Bluetooth/power button (light blue/cyan color)
    button = Entity(model='sphere', color=color.rgb(100, 200, 240), scale=(0.25, 0.08, 0.25), position=(0.85, 0.7, -1.5))
    return logo, button

def create_ports():
    port_labels = ['A','B','C','D','E','F']
    # Place ports on left and right sides of hub, matching real LEGO Spike Hub layout
    y_pos = 0.1  # Middle height of the hub
    x_left = -1.35
    x_right = 1.35
    z_positions = [-1.0, -0.3, 0.4, 1.1]  # Spread vertically
    ports = []
    for i, z in enumerate(z_positions[:3]):
        # Left side ports (A, B, C) - black rectangular ports
        port = Entity(model='cube', color=color.rgb(40, 40, 40), scale=(0.15, 0.25, 0.35), position=(x_left, y_pos, z))
        ports.append(port)
        Text(text=port_labels[i], position=(x_left-0.22, y_pos+0.15, z), origin=(0,0), scale=1.8, color=color.white)
    for i, z in enumerate(z_positions[:3]):
        # Right side ports (D, E, F) - black rectangular ports
        port = Entity(model='cube', color=color.rgb(40, 40, 40), scale=(0.15, 0.25, 0.35), position=(x_right, y_pos, z))
        ports.append(port)
        Text(text=port_labels[i+3], position=(x_right+0.22, y_pos+0.15, z), origin=(0,0), scale=1.8, color=color.white)
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
    led_size = 0.22
    # Place LED matrix on the front face of hub (Z is forward/back, front is negative Z)
    hub_front_z = -1.75  # Front face of the hub
    matrix_start_x = -0.44 * (light_matrix_size-1)/2
    matrix_start_y = -0.44 * (light_matrix_size-1)/2
    for row in range(light_matrix_size):
        row_items = []
        for col in range(light_matrix_size):
            # LEDs are slightly recessed into the front face
            led = Entity(model='cube', color=color.rgb(20, 20, 20), scale=(led_size, led_size, 0.08), 
                        position=(matrix_start_x+col*0.44, matrix_start_y+row*0.44, hub_front_z))
            row_items.append(led)
        light_matrix.append(row_items)
    return light_matrix

def set_light_matrix(light_matrix, matrix):
    for row in range(len(light_matrix)):
        for col in range(len(light_matrix[row])):
            # White/bright color when on, dark when off
            light_matrix[row][col].color = color.rgb(255, 255, 255) if matrix[row][col] else color.rgb(20, 20, 20)

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
camera.position = (3, 3, -10)
camera.look_at(hub)

app.run()
