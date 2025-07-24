import random
import pyautogui as pg
import time

message = ('fuck', 'you', 'niger', 'chingchangchong', 'donotspam', 'gay')

time.sleep(5)

for i in range(1000):
    a = random.choice(message)
    pg.write("i hate you" + a)
    pg.press('enter')