from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(4)
right_button = Button(15)
left_button = Button(14)

left_name = input('left player name is ')
right_name = input('right player name is ')

def pressed(button):
    if button.pin.number == 14:
        print(left_name + ' won the game')
    else:
        print(right_name + ' won the game')

    left_button.when_pressed = None
    right_button.when_pressed = None

max_round=int(input("How many rounds of the game do you want to play?"))

current_round = 0

while current_round < max_rounds:
    current_round += 1
    print(f" {current_round} round begin")
    
    left_button.when_pressed = pressed
    right_button.when_pressed = pressed
    
    led.on()
    delay = uniform(5, 10)
    sleep(delay)
    led.off()
    
    start_time = time.time()
    while time.time() - start_time < 3:
        sleep(0.1)  
    
    left_button.when_pressed = None
    right_button.when_pressed = None
