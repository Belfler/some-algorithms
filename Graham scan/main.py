from matplotlib import pyplot as plt
from random import randint
from math import atan2
from time import sleep


def generate_points(n=25, min_coord=-25, max_coord=25):
    return [[randint(min_coord, max_coord), randint(min_coord, max_coord)]
            for _ in range(n)]


def scatter_plot(points, convex_hull=None, highlight_last=False):
    xs, ys = zip(*points)
    plt.scatter(xs, ys)
    if convex_hull is not None:
        if highlight_last:
            plt.scatter(*convex_hull[-1], c='r')
        for i in range(1, len(convex_hull) + 1):
            if i == len(convex_hull):
                i = 0
            c0 = convex_hull[i - 1]
            c1 = convex_hull[i]
            plt.plot((c0[0], c1[0]), (c0[1], c1[1]), 'b')
    plt.show()


def polar_angle(p0, p1=None):
    if p1 is None:
        p1 = anchor
    x_span = p0[0] - p1[0]
    y_span = p0[1] - p1[1]
    return atan2(y_span, x_span)


# Compute squared distance between points because root is not necessary
def squared_distance(p0, p1=None):
    if p1 is None:
        p1 = anchor
    x_span = p0[0] - p1[0]
    y_span = p1[1] - p1[1]
    return x_span ** 2 + y_span ** 2


# If pseudoscalar production > 0 the curve p0-p1-p2 makes a left turn
# if < 0 it makes the right turn
# else points are on the straight
def pseudoscalar_production(p0, p1, p2):
    vector1 = [p1[0] - p0[0], p1[1] - p0[1]]
    vector2 = [p2[0] - p0[0], p2[1] - p0[1]]
    return vector1[0] * vector2[1] - vector1[1] * vector2[0]


def graham_scan(points, show_progress=False):
    global anchor  # the point with the smallest y coordinate
    min_idx = None
    for i, (x, y) in enumerate(points):
        if min_idx is None or y < points[min_idx][1] or (y == points[min_idx][1] and x < points[min_idx][0]):
            min_idx = i
    anchor = points[min_idx]
    sorted_points = sorted(points, key=lambda x: (polar_angle(x), squared_distance(x)))
    hull = [anchor, sorted_points[1]]
    for i_point in sorted_points[2:]:
        while len(hull) >= 2 and pseudoscalar_production(hull[-2], hull[-1], i_point) < 0:
            del hull[-1]
        hull.append(i_point)
        if show_progress:
            scatter_plot(points, hull, highlight_last=True)
            sleep(0.1)
    return hull


points = generate_points(25, 0, 100)
hull = graham_scan(points, show_progress=True)
