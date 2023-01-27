"""
EmEditor という文字をタイトルに含むウィンドウを検索し、入力を行う
"""
from time import sleep

import pyautogui as pg
import pyperclip as pc

from utils import forground_app

pg.LOG_SCREENSHOTS = True
forground_app('EmEditor')

sleep(1)
for char in 'fuga':
    pg.press(char)
pc.copy('一括\n')
pg.hotkey('ctrl', 'v')
pg.hotkey('alt', 'b')
sleep(1)
pg.click()
