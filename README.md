# servoPrivodDetection
find the parameters for sending into servo for correction moving

На екрані виділений квадрат з лицем, за допомогою нейр мережі, має свої координати центру, також має координати центр екрану. Різниця в пікселях передається в файл або який працює з пінами росбері і той передає різницю в функцію set_servo_position; або в файл, де працює функція set_servo_pulsewidth бібліотеки pigpio для росбері чи інших плат. Ці дані змінюють кут нахилу серви за допомогою 1) лінійної інтерполяції, 2) спосіб пропорційної навігації. Але перед сервою у нас стоїть контролер, тому далі трансформуються дані з радіан в зручну форму для передачі через протокол SBUS в UART інтрерфейс на контролер для керування уже сервами руля.
