# servoPrivodDetection
find the parameters for sending in servo for correction moving

Квадрат з лицем, виявленим за допомогою нейр мережі, має свої координати центру, також має координати центр екрану. Різниця в пікселях передається в файл або який працює з пінами росбері і той передає різницю в функцію set_servo_position, або в файл де працює функція set_servo_pulsewidth бібліотеки pigpio для росбері чи інших плат
