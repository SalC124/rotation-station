import math

from matplotlib import pyplot as plt

plt.gca().set_aspect("equal", adjustable="box")


class Shape:
    def __init__(self, center: list[float], points: list[list[float]]):
        self.center = center
        self.points = points
        self.vectorized_points: list[list[float]] = [None] * len(self.points)

    def draw(self, color):
        for i in range(len(self.points)):
            plt.scatter(self.points[i][0], self.points[i][1], s=5, c=color)
        plt.draw()

    def vectorize_points(self):
        for i in range(len(self.points)):
            angle = math.atan2(
                self.points[i][1] - self.center[1], self.points[i][0] - self.center[0]
            )
            magnitude = (
                ((self.points[i][0] - self.center[0]) ** 2)
                + (self.points[i][1] - self.center[1]) ** 2
            ) ** 0.5
            self.vectorized_points[i] = [angle, magnitude]

    def devectorize_points(self):
        for i in range(len(self.vectorized_points)):
            self.points[i][0] = self.center[0] + (
                self.vectorized_points[i][1] * math.cos(self.vectorized_points[i][0])
            )
            self.points[i][1] = self.center[1] + (
                self.vectorized_points[i][1] * math.sin(self.vectorized_points[i][0])
            )

    def rotate(self, angle):
        self.vectorize_points()
        for i in range(len(self.vectorized_points)):
            self.vectorized_points[i][0] += angle
        self.devectorize_points()


mungus = Shape([0, 0], [[1, -1], [1, 1], [-1, 1], [-1, -1], [2, 2]])
mungus.draw("r")
mungus.rotate(math.pi * (1 / 8))
mungus.rotate(math.pi * (1 / 8))
mungus.draw("b")

plt.show()
