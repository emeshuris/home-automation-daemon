from gpio_common import GPIO

def up():
    chan_list = [10]
    GPIO.setup(chan_list, GPIO.OUT)
    GPIO.output(chan_list, GPIO.HIGH)
