import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define variables
x, y = sp.symbols('x y')
x0, y0 = 0.5, 0.7

# Define the function
z = sp.asin(sp.sqrt(x ** 4 + y ** 4) / sp.sqrt(x ** 2 + y ** 2))

# Compute partial derivatives
dz_dx = sp.diff(z, x).simplify()
dz_dy = sp.diff(z, y).simplify()

# Evaluate partial derivatives at the given point (x0, y0)
dz_dx_val = dz_dx.subs({x: x0, y: y0})
dz_dy_val = dz_dy.subs({x: x0, y: y0})

print(" dz_dx ", dz_dx, "\n",  "dz_dy ", dz_dy)


# Define the function z(x, y)
def z_func(x, y):
    return np.arcsin(np.sqrt(x ** 4 + y ** 4) / np.sqrt(x ** 2 + y ** 2))


# Generate grid for plotting
x_vals = np.linspace(-1, 1, 50)
y_vals = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(x_vals, y_vals)

# Calculate Z values for the surface plot
Z = z_func(X, Y)

# Define the point (x0, y0, z0) and normal vector components
z0 = z_func(x0, y0)
normal_vector = np.array([float(dz_dx_val), float(dz_dy_val), -1])  # Normal is (dz/dx, dz/dy, -1)
normal_vector /= np.linalg.norm(normal_vector)  # Normalize the vector

# Plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Surface plot
ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1, alpha=0.4)

# Point (x0, y0, z0)
ax.scatter(x0, y0, z0, color='red', s=50)

# Normal vector
ax.quiver(x0, y0, z0, normal_vector[0], normal_vector[1], normal_vector[2], color='blue', length=0.5)

t = np.linspace(-1, 1, 50)
xc = t
yc = y0*np.ones(xc.shape)
zc = z_func(xc, yc)
ax.plot(xc, yc, zc, color='orange')

yc = t
xc = x0*np.ones(yc.shape)
zc = z_func(xc, yc)
ax.plot(xc, yc, zc, color='green')

# Tangent vectors at the point (x0, y0, z0)
tangent_x = np.array([1, 0, float(dz_dx_val)])
tangent_y = np.array([0, 1, float(dz_dy_val)])
ax.quiver(x0, y0, z0, *tangent_x, color='purple', length=0.5)
ax.quiver(x0, y0, z0, *tangent_y, color='cyan', length=0.5)

# Labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_aspect('equal')
plt.show()
