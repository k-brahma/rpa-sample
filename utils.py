import win32gui
import ctypes


def _execute_forground(hwnd, title):
    name = win32gui.GetWindowText(hwnd)
    if name.find(title) >= 0:
        # 最小化を戻す
        if win32gui.IsIconic(hwnd):
            win32gui.ShowWindow(hwnd, 1)  # SW_SHOWNORMAL
        win32gui.ShowWindow(hwnd, 3)  # SW_MAXIMIZE
        ctypes.windll.user32.SetForegroundWindow(hwnd)


def forground_app(app_title):
    """
    指定したアプリケーションをフォアグラウンドにして最大化する。
    :param app_title:
    """
    win32gui.EnumWindows(_execute_forground, app_title)