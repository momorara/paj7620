#-*- coding: utf-8 -*-
"""
ジェスチャーによりセキュリティを解除
解除コードは　前->右->上 です。

ジェスチャーで解除してください。
"""


'''!
  @file GestureRecognize_HighRate.ino
  @brief Present the 9 built-in gestures data the sensor supports. 
  @n Wave your hand above the sensor (within 0~20cm), it can recognize 9 kinds of gestures: move up, down, left, right, forward,
  @n backward, clockwise, anti-clockwise, wave.
  @n For more usages of the sensor, refer to the description about setGestureHighRate in function setup.
  @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @licence     The MIT License (MIT)
  @author      Alexander(ouki.wang@dfrobot.com)
  @maintainer  [fary](feng.yang@dfrobot.com)
  @version  V1.0
  @date  2019-07-16
  @url https://github.com/DFRobot/DFRobot_PAJ7620U2
'''
import sys
sys.path.append('../../')
import time
from DFRobot_PAJ7620U2 import *
import test_LED

paj = DFRobot_PAJ7620U2(bus=1)


print("Gesture recognition system base on PAJ7620U2")
try:# 電源投入時最初の起動でエラーになるのをリトライする
    time.sleep(1)
    while(paj.begin() != 0):
        print("initial PAJ7620U2 failure! Please check if all the connections are fine, or if the wire sequence is correct?")
        time.sleep(0.5)
except:
    time.sleep(1)
    while(paj.begin() != 0):
        print("initial PAJ7620U2 failure! Please check if all the connections are fine, or if the wire sequence is correct?")
        time.sleep(0.5)

print("PAJ7620U2 init finished, start to test the gesture recognition function.")
print ('Please press Ctrl+C to end the program...')

'''Set to fast detection mode 
 # If the parameter is set to false, the module enters slow detection mode, and it detects one gesture every 2s. We have integrated
 # some gestures inside the module to make it convenient for beginners.   
 # The slow mode can recognize 9  basic gestures and 4 expanded gestures: move left, right, up, down, forward, backward, clockwise,
 # counter-clockwise, wave. slowly move left and right, slowly move up and down, slowly move forward and backward, wave slowly and 
 # randomly.
 #
 # If the parameter is set to true, the module enters fast detection mode. 
 # The fast mode can recognize 9 gestures: move left, right, up, down, forward, backward, clockwise, counter-clockwise, wave
 # To detect the combination of these gestures, like wave left, right and left quickly, users needs to design their own algorithms logic.
 # Since users only use limited gestures in this mode, we are not going to integrate too much expanded gestures in the library.
 # If necessary, you can complete the algorithm logic in the ino file by yourself.
 '''
paj.set_gesture_highrate(True)


def gesture_no():
    return paj.get_gesture()


def unlock_step(Unlock_code):
    get_code = gesture_no()
    # print(get_code)
    if get_code == Unlock_code:
       print('解除コード受付中',get_code)
       test_LED.LED_gesture(Unlock_code)
    else:
       #  print('エラー')
       pass
    return get_code

# 解除コードは　16,1,4
def main():
    print()
    print('解除コードは　前->右->上 です。')
    print()
    print('今は鍵がかかっています。')

    for _ in range(4):
        gesture_no()

    while True:
      code = unlock_step(16)
      if code == 16:
          break
      else:
         if code != 0:
            print('ロック解除失敗1',code)
            exit(0)

    while True:
      code = unlock_step(1)
      if code == 1:
          break
      else:
         if code != 0:
            print('ロック解除失敗2',code)
            exit(0)
            
    while True:
      code = unlock_step(4)
      if code == 4:
          break
      else:
         if code != 0:
            print('ロック解除失敗3',code)
            exit(0)

    print()
    print('解除成功')


if __name__ == "__main__":
    try:
      main()
    #when 'Ctrl+C' is pressed,child program destroy() will be executed.
    except KeyboardInterrupt:
        exit(0)
    except ValueError as e:
        print(e)