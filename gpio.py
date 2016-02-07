from gpio_common import GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


def up():
    chan_list = [10]
    GPIO.setup(chan_list, GPIO.OUT)
    GPIO.output(chan_list, GPIO.HIGH)
