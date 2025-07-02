import math

from matplotlib import pyplot as plt

plt.gca().set_aspect("equal", adjustable="box")


class Shape3d:
    def __init__(self, center: list[float], points: list[list[float]]):
        self.center = center
        self.points = points

    def show(self, color):
        fig = plt.figure()
        ax = fig.add_subplot(projection="3d")
        ax.set_xlabel("X Label")
        ax.set_ylabel("Y Label")
        for point in self.points:
            ax.scatter(point[0], point[1], point[2], c=color)
        plt.show()

    def rotate(self, angle: float, plane: str):
        sin_a, cos_a = math.sin(angle), math.cos(angle)

        for i, point in enumerate(self.points):
            x = point[0]
            y = point[1]
            z = point[2]

            center_x = self.center[0]
            center_y = self.center[1]
            center_z = self.center[2]

            distance_x = x - center_x
            distance_y = y - center_y
            distance_z = z - center_z

            if plane == "xy":
                new_x = distance_x * cos_a - distance_y * sin_a
                new_y = distance_x * sin_a + distance_y * cos_a
                self.points[i][0] = center_x + new_x
                self.points[i][1] = center_y + new_y
            elif plane == "xz":
                new_x = distance_x * cos_a - distance_z * sin_a
                new_z = distance_x * sin_a + distance_z * cos_a
                self.points[i][0] = center_x + new_x
                self.points[i][2] = center_z + new_z
            elif plane == "yz":
                new_y = distance_y * cos_a - distance_z * sin_a
                new_z = distance_y * sin_a + distance_z * cos_a
                self.points[i][1] = center_y + new_y
                self.points[i][2] = center_z + new_z


cube = Shape3d(
    [0.0, 0.0, 0.0],
    [
        [1.0, -1.0, 1.0],
        [1.0, 1.0, 1.0],
        [-1.0, 1.0, 1.0],
        [-1.0, -1.0, 1.0],
        [1.0, -1.0, -1.0],
        [1.0, 1.0, -1.0],
        [-1.0, 1.0, -1.0],
        [-1.0, -1.0, -1.0],
    ],
)

cube.show("c")
cube.rotate(math.pi * (1 / 8), "xy")
cube.show("b")
cube.rotate(math.pi * (1 / 8), "xy")
cube.show("m")

qube = Shape3d(
    [0.0, 0.0, 0.0],
    [
        [1.0, -1.0, 1.0],
        [1.0, 1.0, 1.0],
        [-1.0, 1.0, 1.0],
        [-1.0, -1.0, 1.0],
        [1.0, -1.0, -1.0],
        [1.0, 1.0, -1.0],
        [-1.0, 1.0, -1.0],
        [-1.0, -1.0, -1.0],
    ],
)

qube.rotate(math.pi * (2 / 8), "xy")
qube.show("r")


cube.rotate(math.pi * -(2 / 8), "xy")
cube.show("b")
