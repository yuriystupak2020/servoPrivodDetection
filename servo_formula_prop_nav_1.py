import math
import time

x = 0      # Начальное значение x
y = 0      # Начальное значение y

target_x = 100  # Целевое значение x
target_y = 50   # Целевое значение y

K = 1.0    # Коэффициент PN (настраивается)

while True:
    dx = target_x - x
    dy = target_y - y
    
    angle_to_target = math.atan2(dy, dx)
    angular_rate = K * angle_to_target
    
    delta_dx = math.cos(angle_to_target) * angular_rate
    delta_dy = math.sin(angle_to_target) * angular_rate
    
    x += delta_dx
    y += delta_dy
    
    print(f"Current position: ({x}, {y})")
    
    # Завершение, когда мы близко к цели (вы можете задать критерий завершения)
    if abs(dx) < 1 and abs(dy) < 1:
        break
    
    # Добавьте задержку для управления скоростью движения
    time.sleep(0.1)

print(f"Final position: ({target_x}, {target_y})")
