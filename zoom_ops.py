import single_template_matching
import pyautogui as pg
import win32gui
import re
import time

def window_enum_callback(hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            win32gui.SetForegroundWindow(hwnd)

def open_zoom_window(): 
    win32gui.EnumWindows(window_enum_callback, "Zoom Meeting")

def is_chat_open(): 
    return single_template_matching.findMatch("chatTemplate.PNG")

def is_video_on(): 
    return single_template_matching.findMatch("videoTemplate.PNG", is_screen_share())

def is_video(): 
    return single_template_matching.findMatch("videooffTemplate.PNG", is_screen_share()) or is_video_on()

def is_screen_share(): 
    return single_template_matching.findMatch("screenshareTemplate.PNG")

def open_and_type():
    open_zoom_window()
    pg.hotkey("alt", "h")
    if not is_chat_open() or is_screen_share():
        pg.hotkey("alt", "h")
    time.sleep(1)
    pg.typewrite("I'm here")
    pg.typewrite(["enter"])

def show_camera():
    if not is_video(): 
        pg.hotkey("esc")

    this = is_video_on()
    if not this:
        pg.hotkey("alt", "v")

def do_all(): 
    open_and_type() 
    show_camera() 