import time

x = 0      # Начальное значение x
y = 0      # Начальное значение y
z = 0      # Начальное значение z

target_x = 100  # Целевое значение x
target_y = 50   # Целевое значение y
target_z = 20   # Целевое значение z

t = 0.0    # Параметр времени

while t < 1.0:
    new_x = x + t * (target_x - x)
    new_y = y + t * (target_y - y)
    new_z = z + t * (target_z - z)
    
    print(f"Current position: ({new_x}, {new_y}, {new_z})")
    
    # Увеличиваем параметр времени на 0.1 каждую секунду
    t += 0.1
    time.sleep(1)

print(f"Final position: ({target_x}, {target_y}, {target_z})")
