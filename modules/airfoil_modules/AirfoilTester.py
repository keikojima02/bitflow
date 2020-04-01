from .AirfoilEdgeRegressor import AirfoilEdgeRegressor
from ..utils.module        import Module

import pickle
import matplotlib.pyplot as plt

DPI = 400

def smooth(array, amount):
    new = []
    running = 0
    for i, x in enumerate(array):
        running += x
        if i % amount == 0:
            new.append(running/amount)
            running = 0
    return new

class AirfoilTester(AirfoilEdgeRegressor):
    def __init__(self):
        AirfoilEdgeRegressor.__init__(self)
        Module.__init__(self, in_label=None, out_label='FitAirfoil:Airfoil')
        self.load() # Load trained weights

    def plot(self, coordinates):
        figsize  = (800/DPI, 200/DPI)
        plt.figure(figsize=figsize, dpi=DPI)
        fx = coordinates[:40]
        fy = coordinates[40:80]
        sy = coordinates[80:120]
        fx = smooth(fx, 2)
        fy = smooth(fy, 2)
        sy = smooth(sy, 2)
        plt.plot(fx, fy, color='red')
        plt.plot(fx, sy, color='blue')
        plt.plot([fx[0], fx[0]], [sy[0], fy[0]], color='black') # Connect front
        plt.plot([fx[-1], fx[-1]], [sy[-1], fy[-1]], color='black') # Connect back

        # with open(base, 'rb') as infile:
        #     base_coords = pickle.load(infile)
        # fx, fy, sx, sy, camber = base_coords
        # plt.plot(fx, fy, color='black')
        # plt.plot(sx, sy, color='black')
        # plt.plot([sx[0], fx[0]], [sy[0], fy[0]], color='black') # Connect front
        # plt.plot([sx[-1], fx[-1]], [sy[-1], fy[-1]], color='black') # Connect back
        plt.axis('off')
        plt.show()

    def process(self, driver=None):
        # location = 'data/images/c141e-il - LOCKHEED C-141 BL761.11 AIRFOILfcafb389-f948-4050-a7cf-a1c23df4056d.png'
        location = 'data/whale_flipper_cross_section.png'
        # base = 'data/airfoil_data/wb140-il - WB-140_35_FB 14%_coords.pkl'
        # base = 'data/airfoil_data/2032c-il - 20-32C AIRFOIL_coords.pkl'
        # base = 'data/airfoil_data/c141e-il - LOCKHEED C-141 BL761.11 AIRFOIL_coords.pkl'
        
        image = self.load_image(location)
        coordinates = self.model(image).detach().numpy()[0]
        self.plot(coordinates)
        return []

        
