from microbit import *
PIR_PIN = pin2
LED_PIN = pin13
pir = pin2.write_digital.DigitalInOut(PIR_PIN)
pir.direction = pin2.write_digital.Direction.INPUT


led = pin2.write_digital.DigitalInOut(LED_PIN)



old_value = pir.value
while True:
    pir_value = pir.value
    if pir_value:
        
        led.value = True
        if not old_value:
            print('Motion detected!')
    else:
        led.value = False
        if old_value:
            print('Motion ended!')
    old_value = pir_value
    