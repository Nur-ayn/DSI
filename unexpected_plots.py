# QUESTION 1 - Unexpected Plot
# The unexpected plot turns out to be a fractal pattern known as the Sierpinski hexagon

import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Polygon, Point
import random

def random_point_within(polygon):
    min_x, min_y, max_x, max_y = polygon.bounds

    while True:
        random_pt = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
        if random_pt.within(polygon):
            return random_pt


def get_triangle_centroid(vertices):
    vertices = np.array(vertices)
    xs, ys = vertices[:,0], vertices[:,1]

    centroid = [np.sum(xs)/3, np.sum(ys)/3]
    return centroid

def unexpected_plot():
    hexagon_vertices = [ (-3,0), (-1.5, 1.5), (1.5, 1.5), (3, 0), (1.5, -1.5), (-1.5, -1.5)]
    hexagon = Polygon(hexagon_vertices)
    plt.plot(*hexagon.exterior.xy)

    P = random_point_within(hexagon)

    for _ in range(10_000):
        plt.plot(P.x, P.y, marker='o', markersize=1)
        random_vertex_index = random.randint(0,5)
        next_vertex_index = (random_vertex_index + random.choice([-1,1])) % 6
        adjacent_vertices = [hexagon_vertices[random_vertex_index], hexagon_vertices[next_vertex_index]]

        triangle_vertices = adjacent_vertices + [(P.x, P.y)]
        P = Point(get_triangle_centroid(triangle_vertices))


if __name__ == '__main__':
    unexpected_plot()
    plt.show()
   
    
