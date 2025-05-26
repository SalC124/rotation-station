from matplotlib import pyplot as plt
import math

plt.gca().set_aspect("equal", adjustable="box")

# base square
center_x = 0
center_y = 0
xs = [2.0, 0.0, -1.0, 1.0]
ys = [1.0, 1.0, -1.0, -1.0]  # tr tl bl br
plt.scatter(xs, ys, s=5, c="r")
plt.scatter(center_x, center_y, s=5, c="m")
print("initial x values:", xs)
print("initial y values:", ys)


# to vector
vectors = []  # [direction,magnitude,quadrant,coords]
print("\nvectors:")
for i in range(len(xs)):
    if xs[i] == center_x:
        xs[i] -= 0.01
    angle = math.atan((ys[i] - center_y) / (xs[i] - center_x))
    magnitude = ((xs[i] ** 2) + ys[i] ** 2) ** 0.5

    # get quadrant
    if angle >= 0:
        if xs[i] - center_x >= 0:
            quadrant = 1
        else:
            quadrant = 3
    else:
        if xs[i] - center_x >= 0:
            quadrant = 4
        else:
            quadrant = 2

    angle = abs(angle)
    if quadrant % 2 == 0:
        angle = (math.pi / 2) - angle

    angle = angle + ((math.pi / 2) * (quadrant - 1))
    vectors.append(
        [
            angle,
            magnitude,
            quadrant,
            [xs[i], ys[i]],
        ]
    )
    print(vectors[i])

# rotate
print("\nnew vectors:")
rot = math.pi / 8  # ccw rotation
for i in range(len(vectors)):
    vectors[i][0] = vectors[i][0] + rot
    vectors[i][3][0] = vectors[i][1] * math.cos(vectors[i][0])
    vectors[i][3][1] = vectors[i][1] * math.sin(vectors[i][0])
    plt.scatter(vectors[i][3][0], vectors[i][3][1], s=5, c="b")
    print(vectors[i])
plt.show()
