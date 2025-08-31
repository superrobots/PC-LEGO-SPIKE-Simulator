import tkinter as tk

class HubVisualizer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("LEGO SPIKE Prime Hub Simulator")
        self.canvas = tk.Canvas(self.root, width=350, height=550)
        self.canvas.pack()

        # Hub body: length:width ratio 3:5 (vertical rectangle)
        hub_x0, hub_y0 = 75, 100
        hub_x1 = hub_x0 + 180  # length (horizontal)
        hub_y1 = hub_y0 + 300  # width (vertical) (180:300 ≈ 3:5)
        self.hub = self.canvas.create_rectangle(hub_x0, hub_y0, hub_x1, hub_y1, fill="#cccccc", outline="#333333", width=3)

        # LEGO icon (square)
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

        # 6 port interfaces (3 on each side)
        self.ports = []
        for i in range(3):
            y = hub_y0 + 60 + i * 60
            self.ports.append(self.canvas.create_rectangle(hub_x0 - 10, y, hub_x0, y + 20, fill="#8888ff", outline="#333333"))
        for i in range(3):
            y = hub_y0 + 60 + i * 60
            self.ports.append(self.canvas.create_rectangle(hub_x1, y, hub_x1 + 10, y + 20, fill="#8888ff", outline="#333333"))

        # 5x5 light matrix (grid of squares)
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

        # Store matrix to display
        self.pending_matrix = [[0]*5 for _ in range(5)]

        # Run button under the matrix
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
    vis.run()