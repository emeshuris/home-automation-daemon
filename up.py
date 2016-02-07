from gpio_common import GPIO
from gpio_common import chan_list

GPIO.setup(chan_list, GPIO.OUT)
GPIO.output(chan_list, GPIO.HIGH)