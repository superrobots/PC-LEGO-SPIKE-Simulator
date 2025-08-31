from spike.light_matrix import Light_matrix
from visualization import HubVisualizer

if __name__ == "__main__":
    vis = HubVisualizer()
    lm = Light_matrix(visualizer=vis)
    lm.show_image("HEART")
    vis.run()