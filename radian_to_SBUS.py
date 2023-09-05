import math
import serial
import time

# Определение минимального и максимального значения для интервала SBUS
sbus_min = 1000
sbus_max = 2000

# Параметры UART (замените на свои)
serial_port = '/dev/ttyUSB0'  # Порт UART
baud_rate = 115200  # Скорость передачи данных

# Инициализация соединения с UART
ser = serial.Serial(serial_port, baud_rate)

# Функция для преобразования радианов в интервал SBUS
def radians_to_sbus(angle_radians):
    return int((angle_radians + math.pi) / (2 * math.pi) * (sbus_max - sbus_min) + sbus_min)

try:
    while True:
        # Симулируем значения углов для двух стикеров
        roll_angle = math.sin(time.time())  # Пример для руля (крена)
        pitch_angle = math.cos(time.time())  # Пример для элеватора (тангажа)

        # Преобразуем углы в значения SBUS
        roll_sbus = radians_to_sbus(roll_angle)
        pitch_sbus = radians_to_sbus(pitch_angle)

        # Отправляем значения на контроллер через UART
        data = bytearray([0x0F, 0x00, (roll_sbus & 0x07FF), ((roll_sbus >> 8) & 0x07FF), ((pitch_sbus & 0x07FF)), ((pitch_sbus >> 8) & 0x07FF), 0x00])
        ser.write(data)

        time.sleep(0.02)  # Задержка для симуляции частоты обновления SBUS (обычно около 50 Гц)

except KeyboardInterrupt:
    # Обработка прерывания с клавиатуры для остановки симуляции
    ser.close()
    print("Симуляция завершена.")
