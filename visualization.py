import tkinter as tk

class HubVisualizer:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("LEGO SPIKE Prime Hub Simulator")
        self.canvas = tk.Canvas(self.root, width=350, height=550)
        self.canvas.pack()

        hub_x0, hub_y0 = 75, 100
        hub_x1 = hub_x0 + 180
        hub_y1 = hub_y0 + 300

        self._draw_hub_body(hub_x0, hub_y0, hub_x1, hub_y1)
        self._draw_lego_icon(hub_x0, hub_y0)
        self._draw_ports(hub_x0, hub_y0, hub_x1)
        self._draw_motors_and_arm(hub_x0, hub_y0, hub_x1, hub_y1)
        self._draw_light_matrix(hub_x0, hub_y0)
        self.pending_matrix = [[0]*5 for _ in range(5)]
        self._draw_run_button()

    def drive(self, direction="forward", distance=20):
        """
        Move the robot forward or backward by shifting the wheels and hub.
        direction: 'forward' or 'backward'
        distance: pixels to move
        """
        if direction == "forward":
            dy = -distance
        else:
            dy = distance
        # Move hub, wheels, and arm
        self.canvas.move(self.hub, 0, dy)
        self.canvas.move(self.left_wheel, 0, dy)
        self.canvas.move(self.right_wheel, 0, dy)
        self.canvas.move(self.lego_icon, 0, dy)
        self.canvas.move(self.lego_text, 0, dy)
        for port in self.ports:
            self.canvas.move(port, 0, dy)
        for row in self.light_matrix:
            for cell in row:
                self.canvas.move(cell, 0, dy)
        self.canvas.move(self.run_button_circle, 0, dy)
        self.canvas.move(self.run_button_text, 0, dy)
        self.canvas.move(self.arm, 0, dy)
        # Update arm base position
        self.arm_base_y += dy

    def move_arm(self, action="raise"):
        """
        Raise or lower the robot arm.
        action: 'raise' or 'lower'
        """
        if action == "raise":
            self.arm_angle = max(0, self.arm_angle - 30)  # up
        else:
            self.arm_angle = min(90, self.arm_angle + 30)  # down
        # Redraw arm
        self.arm = self._draw_arm(self.arm_angle)

    

    def _draw_hub_body(self, hub_x0, hub_y0, hub_x1, hub_y1):
        self.hub = self.canvas.create_rectangle(hub_x0, hub_y0, hub_x1, hub_y1, fill="#cccccc", outline="#333333", width=3)

    def _draw_lego_icon(self, hub_x0, hub_y0):
        lego_icon_size = 40
        lego_icon_x0 = hub_x0 + 15
        lego_icon_y0 = hub_y0 + 15
        lego_icon_x1 = lego_icon_x0 + lego_icon_size
        lego_icon_y1 = lego_icon_y0 + lego_icon_size
        self.lego_icon = self.canvas.create_rectangle(lego_icon_x0, lego_icon_y0, lego_icon_x1, lego_icon_y1, fill="#ffcc00", outline="#eeba00", width=2)
        self.lego_text = self.canvas.create_text(
            lego_icon_x0 + lego_icon_size // 2, lego_icon_y0 + lego_icon_size // 2,
            text="LEGO", fill="#d00", font=("Arial", 10, "bold")
        )

    def _draw_ports(self, hub_x0, hub_y0, hub_x1):
        self.ports = []
        self.port_labels = []
        port_names = ['A', 'B', 'C', 'D', 'E', 'F']
        # Left side ports: A, B, C
        for i in range(3):
            y = hub_y0 + 60 + i * 60
            rect = self.canvas.create_rectangle(hub_x0 - 10, y, hub_x0, y + 20, fill="#8888ff", outline="#333333")
            self.ports.append(rect)
            label = self.canvas.create_text(hub_x0 - 25, y + 10, text=port_names[i], font=("Arial", 10, "bold"), fill="#333")
            self.port_labels.append(label)
        # Right side ports: D, E, F
        for i in range(3):
            y = hub_y0 + 60 + i * 60
            rect = self.canvas.create_rectangle(hub_x1, y, hub_x1 + 10, y + 20, fill="#8888ff", outline="#333333")
            self.ports.append(rect)
            label = self.canvas.create_text(hub_x1 + 25, y + 10, text=port_names[i+3], font=("Arial", 10, "bold"), fill="#333")
            self.port_labels.append(label)

    def _draw_motors_and_arm(self, hub_x0, hub_y0, hub_x1, hub_y1):
        wheel_radius = 22
        wheel_y = hub_y1 + 20
        # Motor positions
        motor_a_x = hub_x0 + 20
        motor_a_y = wheel_y - 40
        motor_b_x = hub_x0 + 60
        motor_b_y = wheel_y - 40
        motor_c_x = (hub_x0 + hub_x1) // 2
        motor_c_y = hub_y0 - 40
        motor_size = 24
        # Draw motors (rectangles)
        self.motor_a = self.canvas.create_rectangle(motor_a_x - motor_size//2, motor_a_y - motor_size//2,
                                                   motor_a_x + motor_size//2, motor_a_y + motor_size//2,
                                                   fill="#bbb", outline="#444", width=2)
        self.motor_b = self.canvas.create_rectangle(motor_b_x - motor_size//2, motor_b_y - motor_size//2,
                                                   motor_b_x + motor_size//2, motor_b_y + motor_size//2,
                                                   fill="#bbb", outline="#444", width=2)
        self.motor_c = self.canvas.create_rectangle(motor_c_x - motor_size//2, motor_c_y - motor_size//2,
                                                   motor_c_x + motor_size//2, motor_c_y + motor_size//2,
                                                   fill="#bbb", outline="#444", width=2)
        # Label motors
        self.canvas.create_text(motor_a_x, motor_a_y, text="Motor A", font=("Arial", 9, "bold"), fill="#222")
        self.canvas.create_text(motor_b_x, motor_b_y, text="Motor B", font=("Arial", 9, "bold"), fill="#222")
        self.canvas.create_text(motor_c_x, motor_c_y, text="Motor C", font=("Arial", 9, "bold"), fill="#222")

        # Wheels
        self.left_wheel = self.canvas.create_oval(hub_x0 + 20 - wheel_radius, wheel_y - wheel_radius,
                              hub_x0 + 20 + wheel_radius, wheel_y + wheel_radius,
                              fill="#444444", outline="#222222", width=3)
        self.right_wheel = self.canvas.create_oval(hub_x1 - 20 - wheel_radius, wheel_y - wheel_radius,
                               hub_x1 - 20 + wheel_radius, wheel_y + wheel_radius,
                               fill="#444444", outline="#222222", width=3)
        # Connect ports to motors
        port_a_y = hub_y0 + 60 + 0 * 60 + 10
        port_b_y = hub_y0 + 60 + 1 * 60 + 10
        port_c_y = hub_y0 + 60 + 2 * 60 + 10
        self.canvas.create_line(hub_x0 - 10, port_a_y, motor_a_x, motor_a_y, width=3, fill="#8888ff")
        self.canvas.create_line(hub_x0 - 10, port_b_y, motor_b_x, motor_b_y, width=3, fill="#8888ff")
        self.canvas.create_line(hub_x0 - 10, port_c_y, motor_c_x, motor_c_y, width=3, fill="#8888ff")
        # Connect motors to wheels/arm
        self.canvas.create_line(motor_a_x, motor_a_y + motor_size//2, hub_x0 + 20, wheel_y - wheel_radius, width=3, fill="#444")
        self.canvas.create_line(motor_b_x, motor_b_y + motor_size//2, hub_x1 - 20, wheel_y - wheel_radius, width=3, fill="#444")
        self.arm_base_x = (hub_x0 + hub_x1) // 2
        self.arm_base_y = hub_y0 - 10
        self.arm_length = 60
        self.arm_angle = 60
        self.arm = self._draw_arm(self.arm_angle)
        self.canvas.create_line(motor_c_x, motor_c_y + motor_size//2, self.arm_base_x, self.arm_base_y, width=3, fill="#444")

    def _draw_light_matrix(self, hub_x0, hub_y0):
        self.light_matrix = []
        matrix_start_x = hub_x0 + 40
        matrix_start_y = hub_y0 + 80
        cell_size = 24
        for row in range(5):
            row_items = []
            for col in range(5):
                x0 = matrix_start_x + col * cell_size
                y0 = matrix_start_y + row * cell_size
                item = self.canvas.create_rectangle(x0, y0, x0 + 16, y0 + 16, fill="#222222", outline="#666666")
                row_items.append(item)
            self.light_matrix.append(row_items)

    def _draw_run_button(self):
        # Use matrix_start_x and matrix_start_y from the first cell in light_matrix
        cell = self.light_matrix[0][0]
        coords = self.canvas.coords(cell)
        matrix_start_x = coords[0] - 0
        matrix_start_y = coords[1] - 80
        cell_size = 24
        self.run_btn_x = matrix_start_x + (cell_size * 2)
        self.run_btn_y = matrix_start_y + (cell_size * 5) + 30
        self.run_btn_radius = 20
        self.run_button_circle = self.canvas.create_oval(
            self.run_btn_x - self.run_btn_radius, self.run_btn_y - self.run_btn_radius,
            self.run_btn_x + self.run_btn_radius, self.run_btn_y + self.run_btn_radius,
            fill="#33cc33", outline="#228822", width=2
        )
        self.run_button_text = self.canvas.create_text(
            self.run_btn_x, self.run_btn_y, text="Run", fill="white", font=("Arial", 12, "bold")
        )
        self.canvas.tag_bind(self.run_button_circle, "<Button-1>", lambda e: self.on_run())
        self.canvas.tag_bind(self.run_button_text, "<Button-1>", lambda e: self.on_run())

    def update_light_matrix(self, matrix):
        """Store matrix, but don't display until Run is clicked."""
        self.pending_matrix = matrix

    def _draw_arm(self, angle):
        # Remove previous arm if exists
        if hasattr(self, 'arm') and self.arm:
            self.canvas.delete(self.arm)
        import math
        rad = math.radians(angle)
        x1 = self.arm_base_x + self.arm_length * math.cos(rad)
        y1 = self.arm_base_y - self.arm_length * math.sin(rad)
        return self.canvas.create_line(self.arm_base_x, self.arm_base_y, x1, y1, width=8, fill="#888888", capstyle=tk.ROUND)

    def on_run(self):
        """Display the stored matrix when Run is clicked."""
        for row in range(5):
            for col in range(5):
                color = "#ffff33" if self.pending_matrix[row][col] else "#222222"
                self.canvas.itemconfig(self.light_matrix[row][col], fill=color)

    def run(self):
        self.root.mainloop()

# Example usage:
if __name__ == "__main__":
    vis = HubVisualizer()
    # Example: turn on a diagonal
    matrix = [[1 if i==j else 0 for j in range(5)] for i in range(5)]
    vis.update_light_matrix(matrix)

    # Test motor controls
    import time
    def demo():
        vis.drive("forward", 40)
        vis.root.update()
        time.sleep(0.5)
        vis.drive("backward", 40)
        vis.root.update()
        time.sleep(0.5)
        vis.move_arm("raise")
        vis.root.update()
        time.sleep(0.5)
        vis.move_arm("lower")
        vis.root.update()

    vis.root.after(1000, demo)
    vis.run()