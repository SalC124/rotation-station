from matplotlib import pyplot as plt
import math

plt.gca().set_aspect("equal", adjustable="box")

# base cube
center = [0, 0, 0]
# +x is right, +y is up, and +z is forward toward the viewpoint
vertices = [
    [1.0, 1.0, 1.0],
    [-1.0, 1.0, 1.0],
    [-1.0, -1.0, 1.0],
    [1.0, -1.0, 1.0],
    [1.0, 1.0, -1.0],
    [-1.0, 1.0, -1.0],
    [-1.0, -1.0, -1.0],
    [1.0, -1.0, -1.0],
]

# to vector
vectors = []  # [direction,magnitude,quadrant,coords]
print("\nvectors:")
for i in range(len(vertices)):
    x = vertices[i][0] - center[0]
    y = vertices[i][1] - center[1]
    z = vertices[i][2] - center[2]
    z_neg = vertices[i][2] - center[2] < 0

    magnitude = ((x**2) + (y**2) + (z**2)) ** (1 / 3)

    # makes sure no error bc of asymptote
    for j in range(len(vertices[i])):
        if vertices[i][j] == center[j]:
            vertices[i][j] -= 0.001

    if x > 0 and y > 0:
        xy_quadrant = 1
        xz_quadrant = 1 + (
            z_neg * 3
        )  # abs(z_neg - 1) * 1 + (z_neg * ((base_xz_q - 3) * -1) + 2)
        yz_quadrant = 1 + z_neg
    elif x < 0 and y > 0:
        xy_quadrant = 2
        xz_quadrant = 2 + (z_neg)
        yz_quadrant = 1 + z_neg
    elif x < 0 and y < 0:
        xy_quadrant = 3
        xz_quadrant = 2 + (z_neg)
        yz_quadrant = 4 - z_neg

    elif x > 0 and y < 0:
        xy_quadrant = 4
        xz_quadrant = 1 + (z_neg * 3)
        yz_quadrant = 4 - z_neg
    else:
        print("wtf did you do? 😭")
        xy_quadrant = 0
        xz_quadrant = 0
        yz_quadrant = 0

    xy_angle = abs(
        math.atan((vertices[i][1] - center[1]) / (vertices[i][0] - center[0]))
    )
    xy_angle = xy_angle + ((math.pi / 2) * (xy_quadrant - 1))
    xz_angle = abs(
        math.atan((vertices[i][0] - center[0]) / (vertices[i][2] - center[2]))
    )
    xz_angle = xz_angle + ((math.pi / 2) * (xz_quadrant - 1))
    yz_angle = abs(
        math.atan((vertices[i][2] - center[2]) / (vertices[i][0] - center[0]))
    )
    yz_angle = yz_angle + ((math.pi / 2) * (yz_quadrant - 1))

    vectors.append(
        [
            [xy_angle, xz_angle, yz_angle],
            magnitude,
            [xy_quadrant, xz_quadrant, yz_quadrant],
            [vertices[i][0], vertices[i][1], vertices[i][2]],
        ]
    )
    print(vectors[i])

# test initial values
fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.set_xlabel("X Label")
ax.set_ylabel("Y Label")

# rotate
# TODO: when rotating, angles schmoove too much (ie: vector i:2 goes from x=-1 to x=1)
print("\nnew vectors:")
# ccw btw
xy_rot = math.pi / 8
xz_rot = math.pi / 8
yz_rot = 0  # math.pi / 8
ax.scatter(center[0], center[1], center[2], c="m")

# apply rotation and plot vectors
for i in range(len(vectors)):
    vectors[i][0][0] = vectors[i][0][0] + xy_rot
    vectors[i][0][1] = vectors[i][0][1] + xz_rot
    vectors[i][0][2] = vectors[i][0][2] + yz_rot
    magnitude = vectors[i][1]

    vectors[i][3][0] = magnitude * math.cos(vectors[i][0][0])
    vectors[i][3][1] = magnitude * math.sin(vectors[i][0][0])

    # vectors[i][3][0] = magnitude * math.cos(vectors[i][0][1])
    vectors[i][3][2] = magnitude * math.cos(vectors[i][0][1])
    vectors[i][3][0] = magnitude * math.sin(vectors[i][0][1])

    # vectors[i][3][1] = magnitude * math.cos(vectors[i][0][2])
    # vectors[i][3][2] = magnitude * math.sin(vectors[i][0][2])

    # vectors[i][0][1] = vectors[i][0][1] + xz_rot
    # vectors[i][3][1] = vectors[i][1] * math.cos(vectors[i][0][1])
    # vectors[i][3][1] = vectors[i][1] * math.sin(vectors[i][0][1])
    #
    #     vectors[i][0][2] = vectors[i][0][2] + yz_rot
    #     vectors[i][3][2] = vectors[i][1] * math.cos(vectors[i][0][2])
    #     vectors[i][3][2] = vectors[i][1] * math.sin(vectors[i][0][2])
    #
    ax.scatter(vectors[i][3][0], vectors[i][3][1], vectors[i][3][2], c="b")
    print(vectors[i])
plt.show()
