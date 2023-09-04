import RPi.GPIO as GPIO
import time

# Установка пинов для сервопривода
servo_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Создание объекта PWM для управления сервоприводом
pwm = GPIO.PWM(servo_pin, 50)  # 50 Гц частота

# Нормализованные значения для сервопривода
normalized_x = 90  # Пример: 90 градусов для центра
normalized_y = 45  # Пример: 45 градусов для вертикальной середины

# Функция для установки положения сервопривода
def set_servo_position(x, y):
    pwm.start(x)
    time.sleep(1)  # Может потребоваться настроить время для вашего сервопривода
    pwm.stop()

# Установка положения сервопривода
set_servo_position(normalized_x, normalized_y)

# Очистка ресурсов GPIO
GPIO.cleanup()
