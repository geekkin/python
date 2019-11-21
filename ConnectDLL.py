from ctypes import *
from commctrl import *
import win32gui
from win32con import *
from autoit import *

print(win32gui.SendMessage(331834, NM_DBLCLK, 1, 1))