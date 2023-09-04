import time

x = 0  # Начальное значение x
y = 0  # Начальное значение y

target_x = 100  # Целевое значение x
target_y = 50   # Целевое значение y

t = 0.0  # Параметр времени

while t < 1.0:
    new_x = x + t * (target_x - x)
    new_y = y + t * (target_y - y)
    
    print(f"Current position: ({new_x}, {new_y})")
    
    # Увеличиваем параметр времени на 0.1 каждую секунду
    t += 0.1
    time.sleep(1)

print(f"Final position: ({target_x}, {target_y})")
