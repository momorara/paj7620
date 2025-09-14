
#!/usr/bin/python

"""
###########################################################################
# LEDを on off

#Filename      :test_LED.py
#Description   :blink LED

LEDを点滅させます。

#Update        :2019/11/02

2025/01/07  pi5のためgpiozeroに置き換え
2025/08/31  paj7620評価用


############################################################################
"""

from gpiozero import LED
import time

LED1 = LED(27) # 左
LED2 = LED(17) # 下
LED3 = LED(22) # 右
LED4 = LED(10) # 上
LED5 = LED(9)  # 中心


#print message at the begining ---custom function
def print_message():
    print ('|********************************|')
    print ('|   blink LED                    |')
    print ('|********************************|\n')
    print ('Program is running...')
    print ('Please press Ctrl+C to end the program...')

def LED(i):
    if i == 1:
        LED1.blink(on_time = 0.2, off_time = 0.1, n = 1, background = False)
    if i == 2:
        LED2.blink(on_time = 0.2, off_time = 0.1, n = 1, background = False)
    if i == 3:
        LED3.blink(on_time = 0.2, off_time = 0.1, n = 1, background = False)
    if i == 4:
        LED4.blink(on_time = 0.2, off_time = 0.1, n = 1, background = False)
    if i == 5:
        LED5.blink(on_time = 0.2, off_time = 0.1, n = 1, background = False)

def LED_forward(i):
    for _ in range(i):
        LED1.on(),LED2.on(),LED3.on(),LED4.on()
        time.sleep(0.2)
        LED1.off(),LED2.off(),LED3.off(),LED4.off()
        time.sleep(0.1)
    LED1.on(),LED2.on(),LED3.on(),LED4.on()
    time.sleep(1)
    LED1.off(),LED2.off(),LED3.off(),LED4.off()

def LED_gesture(i):
    if i == 1:
        for i in [1,5,3,1,5,3]: # 右
            LED(i)
    if i == 2:
        for i in [3,5,1,3,5,1]: # 左
            LED(i)
    if i == 4:
        for i in [2,5,4,2,5,4]: # 上
            LED(i) 
    if i == 8:
        for i in [4,5,2,4,5,2]: # 下
            LED(i) 
    if i == 16:
            LED_forward(3) # 前進
    if i == 32:
        for i in [5,5,5]: # 後退
            LED(i)
    if i == 64:
        for i in [4,3,2,1,4,3,2,1]: # 時計回り
            LED(i)
    if i == 128:
        for i in [1,2,3,4,1,2,3,4]: # 反時計回り
            LED(i)   
    if i == 256:
        for i in [1,5,3,3,5,1,1,5,3,3,5,1]: # 手振り
            LED(i)

#main function
def main():
    #print info
    print_message()

    for i in [4,3,2,1,4,3,2,1]: # 時計回り
        LED(i)

    for i in [1,2,3,4,1,2,3,4]: # 反時計回り
        LED(i)

    for i in [1,5,3,1,5,3]: # 右
        LED(i)

    for i in [3,5,1,3,5,1]: # 左
        LED(i)

    for i in [2,5,4,2,5,4]: # 上
        LED(i)

    for i in [4,5,2,4,5,2]: # 下
        LED(i)

    for i in [5,5,5]: # 後退
        LED(i)

    LED_forward(3) # 前進

    for i in [1,5,3,3,5,1,1,5,3,3,5,1]: # 手振り
        LED(i)

if __name__ == '__main__':
    try:
        main()
    #when 'Ctrl+C' is pressed,child program destroy() will be executed.
    except KeyboardInterrupt:
        pass
    except ValueError as e:
        print(e)