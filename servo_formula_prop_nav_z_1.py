# расчет для изменения координат по всем трем осям X, Y и Z с 
# использованием пропорциональной навигации.
import math
import time

x = 0      # Начальное значение x
y = 0      # Начальное значение y
z = 0      # Начальное значение z

target_x = 100  # Целевое значение x
target_y = 50   # Целевое значение y
target_z = 20   # Целевое значение z

Kx = 1.0    # Коэффициент PN для оси X (настраивается)
Ky = 1.0    # Коэффициент PN для оси Y (настраивается)
Kz = 1.0    # Коэффициент PN для оси Z (настраивается)

while True:
    dx = target_x - x
    dy = target_y - y
    dz = target_z - z
    
    angle_to_target_x = math.atan2(dy, dx)
    angle_to_target_y = math.atan2(dz, math.sqrt(dx**2 + dy**2))
    
    angular_rate_x = Kx * angle_to_target_x
    angular_rate_y = Ky * angle_to_target_y
    
    # Вычисление угла для оси Z
    angle_to_target_z = math.atan2(dz, math.sqrt(dx**2 + dy**2))
    angular_rate_z = Kz * angle_to_target_z
    
    delta_dx = math.cos(angle_to_target_x) * angular_rate_x
    delta_dy = math.sin(angle_to_target_x) * angular_rate_x
    delta_dz = math.sin(angle_to_target_y) * angular_rate_y
    
    x += delta_dx
    y += delta_dy
    z += delta_dz
    
    print(f"Current position: ({x}, {y}, {z})")
    
    # Завершение, когда мы близко к цели (вы можете задать критерий завершения)
    if abs(dx) < 1 and abs(dy) < 1 and abs(dz) < 1:
        break
    
    # Добавьте задержку для управления скоростью движения
    time.sleep(0.1)

print(f"Final position: ({target_x}, {target_y}, {target_z})")
