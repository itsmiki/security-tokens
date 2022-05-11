from importlib.resources import path
from time import sleep
import subprocess
import os
import ctypes

def start_server(console: bool, port: int, ip: str = None) -> int:
    if console == 1:
        if ip is None:
            path = os.path.dirname(os.path.abspath(__file__)) + "\server.exe " + str(port)
        else:
            path = os.path.dirname(os.path.abspath(__file__)) + "\server.exe " + str(ip) + " " + str(port)
        proc = subprocess.Popen(str(path), creationflags=subprocess.CREATE_NEW_CONSOLE)
    else:
        if ip is None:
            path = os.path.dirname(os.path.abspath(__file__)) + "\server.exe " + str(port)
        else:
            path = os.path.dirname(os.path.abspath(__file__)) + "\server.exe " + str(ip) + " " + str(port)
        proc = subprocess.Popen(str(path)) # +str(port)

    return proc.pid

def stop_server(pid: int) -> int:
    import psutil

    parent = psutil.Process(pid)
    for child in parent.children(recursive=True):  # or parent.children() for recursive=False
        child.kill()
    parent.kill()
    

# pid = start_server(1, 5000)
# sleep(5)
# stop_server(pid)
# pid = start_server(0, 8080)
# sleep(5)
# stop_server(pid)

# import ctypes

# def raise_console(console_toggle):
#     """Brings up the Console Window."""
#     if console_toggle:
#         # Show console
#         ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 4)
#     else:
#         # Hide console
#         ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
#     console_toggle = not console_toggle

# console_toggle = False