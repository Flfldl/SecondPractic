import math
import matplotlib.pyplot as plt
cx, cy = map(float, input('Введите координаты xc, yc через пробел: ').split())
r = float(input('Введите радиус: '))
px, py = map(float, input('Введите координаты точки: ').split())
if r <= 0:
    print("Бро, радиус не может быть отрицательным")
d = math.sqrt((px - cx) ** 2 + (py - cy) ** 2)
if d == r:
    print("Точка лежит на окружности")
elif d < r:
    print("Точка находится внутри окружности")
else:
    print("Точка находится за пределами окружности")

fig, ax = plt.subplots()

circle = plt.Circle((cx, cy), r, fill=False, color="blue", linewidth=2)
ax.add_patch(circle)

ax.plot(cx, cy, "bo", markersize=4, label="Центр")
ax.plot(px, py, "ro", markersize=8, label="Точка")


ax.set_aspect("equal")
margin = max(r, d) + 1
ax.set_xlim(cx - margin, cx + margin)
ax.set_ylim(cy - margin, cy + margin)
ax.grid(True)
ax.legend()

plt.show()