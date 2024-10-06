import numpy as np
import matplotlib.pyplot as plt

N = 100

image = np.zeros((N, N))

border_thickness = 5
image[:border_thickness, :] = 0.5  # Top border
image[-border_thickness:, :] = 0.5  # Bottom border
image[:, :border_thickness] = 0.5  # Left border
image[:, -border_thickness:] = 0.5  # Right border

# Define the position and size of the white figure (two concentric circles)
center = (N // 2, N // 2)
outer_radius = 30
inner_radius = 15

# Draw the outer white circle (outer_radius)
for y in range(N):
    for x in range(N):
        distance_to_center = np.sqrt((x - center[0])**2 + (y - center[1])**2)
        if outer_radius - 1 <= distance_to_center <= outer_radius + 1:
            image[y, x] = 1  # White

# Draw the inner circle (inner_radius)
for y in range(N):
    for x in range(N):
        distance_to_center = np.sqrt((x - center[0])**2 + (y - center[1])**2)
        if inner_radius - 1 <= distance_to_center <= inner_radius + 1:
            image[y, x] = 1  # White for inner circle

ext = [-1, 1, -1, 1]
plt.imshow(image, cmap='gray', extent=ext)
plt.savefig("imageWithExtent.png")
plt.imsave("imageWithoutExtent.png", image, cmap='gray')
plt.show()


