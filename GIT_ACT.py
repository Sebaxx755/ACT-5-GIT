import numpy as np
import matplotlib.pyplot as plt

# Parámetros del fractal
width, height = 800, 800
x_min, x_max = -2.0, 1.0
y_min, y_max = -1.5, 1.5
max_iter = 100

# Crear una matriz para almacenar los valores
mandelbrot = np.zeros((height, width))

# Algoritmo del conjunto de Mandelbrot (Benoît Mandelbrot, 1975)
for y in range(height):
    for x in range(width):
        zx, zy = 0, 0
        cx = x_min + (x / width) * (x_max - x_min)
        cy = y_min + (y / height) * (y_max - y_min)
        i = 0
        while zx**2 + zy**2 <= 4 and i < max_iter:
            tmp = zx**2 - zy**2 + cx
            zy = 2*zx*zy + cy
            zx = tmp
            i += 1
        mandelbrot[y, x] = i

# Generar la imagen
plt.imshow(mandelbrot, cmap="hot", extent=(x_min, x_max, y_min, y_max))
plt.title("Conjunto de Mandelbrot (Benoît Mandelbrot, 1975)")
plt.xlabel("Re")
plt.ylabel("Im")
plt.savefig("mandelbrot.png")
plt.show()
