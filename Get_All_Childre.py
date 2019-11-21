import win32gui
import win32con

childre_hwnd_list = []
win32gui.EnumChildWindows(460588,  lambda hWnd, param: param.append(hWnd), childre_hwnd_list)

print(childre_hwnd_list)
for i in childre_hwnd_list:
    print(win32gui.GetClassName(i))
