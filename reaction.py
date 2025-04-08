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
# 游戏主循环
max_round=int(input("要进行几轮游戏"))

current_round = 0

while current_round < max_rounds:
    current_round += 1
    print(f"第 {current_round} 轮开始！")
    # 绑定按钮事件并执行游戏逻辑...
    # 重新绑定按钮事件，确保每轮游戏开始时启用
    left_button.when_pressed = pressed
    right_button.when_pressed = pressed
    
    # 开始一轮游戏
    led.on()
    delay = uniform(5, 10)
    sleep(delay)
    led.off()
    
    # 允许3秒的反应时间
    start_time = time.time()
    while time.time() - start_time < 3:
        sleep(0.1)  # 避免CPU占用
    
    # 无论是否按下按钮，进入下一轮前解除事件绑定
    left_button.when_pressed = None
    right_button.when_pressed = None
