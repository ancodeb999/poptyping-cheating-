# ============================================
# Module: Typing Game Assistant Tool
# Author: Anocdeb999
# Version: 0.0.1
# License: GPL-3.0
# Purpose: For technical research and learning only
# ============================================
import pyautogui
import time
import pytesseract
from PIL import Image
from pynput.keyboard import Controller, Listener, Key
"""
This software is provided "as is" without any express or implied warranties.
The author is not liable for any direct or indirect losses arising from the use of this software, 
including but not limited to account bans, legal disputes, and financial losses.
"""
# a cheating script for poptyping
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
OCR_CONFIG = r'--oem 3 --psm 7 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz-?!、'

keyboard = Controller()
running = False
exit_flag = False
last_text = ""

def on_press(key):
    global running, exit_flag
    if key == Key.left:
        running = not running
        print(f"{'start' if running else 'stop'}")
    elif key == Key.esc:
        exit_flag = True
        return False  # Stop listener

def main():
    global exit_flag, running, last_text
    print("Typing Game Assistant / タイピングゲーム補助ツール\n=================================================\n"
    "WARNING / 警告:\n"
    "For technical research only / 技術研究専用\n"
    "Do not use for cheating / チート行為には使用しないでください")
    print("左矢印キーで開始/停止、Escキーで終了")
    
    # Start listener
    listener = Listener(on_press=on_press)
    listener.start()
    
    try:
        while not exit_flag:
            if running:
                # Capture screenshot around mouse
                x, y = pyautogui.position()
                img = pyautogui.screenshot(region=(x-400, y-30, 800, 60))
                
                # OCR
                text = pytesseract.image_to_string(img, config=OCR_CONFIG)
                
                # clean text
                text = ''.join(c for c in text.lower() if c in 'abcdefghijklmnopqrstuvwxyz-?!')
                
                # input text if changed
                if text and text != last_text:
                    print(f"入力: {text}")
                    keyboard.type(text)
                    last_text = text
                
                time.sleep(0.05)
            else:
                time.sleep(0.1)
                
    except Exception as e:
        print(f"エラー: {e}")
    finally:
        listener.stop()

    print("終了しました")
if __name__ == "__main__":
    main()