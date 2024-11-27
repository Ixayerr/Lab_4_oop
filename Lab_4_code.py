import math
import matplotlib.pyplot as plt

class Point_10:
    """Клас для представлення точки на площині."""
    instance_count = 0

    def __init__(self, x=0, y=0):
        self.x = x if -100 <= x <= 100 else 0
        self.y = y if -100 <= y <= 100 else 0
        Point_10.instance_count += 1

    def __del__(self):
        Point_10.instance_count -= 1

    def move(self, dx, dy):
        self.x = self.x + dx if -100 <= self.x + dx <= 100 else 0
        self.y = self.y + dy if -100 <= self.y + dy <= 100 else 0

#точки
points = [Point_10(10, 20), Point_10(30, 40), Point_10(50, 60), Point_10(70, 80)]

# Відстань між третьою і четвертою точками
distance = math.sqrt((points[2].x - points[3].x) ** 2 + (points[2].y - points[3].y) ** 2)
print(f"Відстань між третьою і четвертою точками: {distance}")

# Зміщення першої точки
points[0].move(29, 0)

# Графік точок
def plot_points(points, title, color):
    x, y = [p.x for p in points], [p.y for p in points]
    plt.scatter(x, y, color=color)
    for i, (xi, yi) in enumerate(zip(x, y), 1):
        plt.text(xi, yi, f"{i}")
    plt.title(title)
    plt.grid()

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plot_points([Point_10(10, 20), Point_10(30, 40), Point_10(50, 60), Point_10(70, 80)], "До змін", "blue")
plt.subplot(1, 2, 2)
plot_points(points, "Після змін", "red")
plt.show()

# Збереження координат у файл
with open("points_data.txt", "w") as file:
    file.writelines([f"({i}) {p.x}:{p.y}\n" for i, p in enumerate(points, 1)])

print("Координати точок збережено у файл 'points_data.txt'.")
