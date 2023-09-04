import pigpio
import time

pi = pigpio.pi()
pi.set_mode(18, pigpio.OUTPUT)

print ("mode: ", pi.get_mode(18))

# def pig_pio_detection():
#     for i in range(0,5):
#         print("setting to: ",pi.set_servo_pulsewidth(18, 1000))
#         print("set to: ",pi.get_servo_pulsewidth(18))
#
#         time.sleep(1)
#
#         print("setting to: ",pi.set_servo_pulsewidth(18, 2000))
#         print("set to: ",pi.get_servo_pulsewidth(18))
#
#         time.sleep(1)
#
#     #pi.stop()

for i in range(0, 5):
    print("setting to: ", pi.set_servo_pulsewidth(18, 1000))
    print("set to: ", pi.get_servo_pulsewidth(18))

    time.sleep(1)

    print("setting to: ", pi.set_servo_pulsewidth(18, 2000))
    print("set to: ", pi.get_servo_pulsewidth(18))

    time.sleep(1)

pi.stop()