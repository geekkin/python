import win32con
import win32gui
import win32api
import commctrl

# ==================================================================
print(
    win32gui.SendMessage(592626, win32con.WM_SETTEXT, 0,
                         'hello world!1\n你好世界！'))
bufSize = win32api.SendMessage(592626, win32con.WM_GETTEXTLENGTH, 0, 0) + 1
# 利用api生成Buffer
strBuf = win32gui.PyMakeBuffer(bufSize)
print(strBuf)
# 发送消息获取文本内容
# 参数：窗口句柄； 消息类型；文本大小； 存储位置
length = win32gui.SendMessage(592626, win32con.WM_GETTEXT, bufSize, strBuf)
# 反向内容，转为字符串
# text = str(strBuf[:-1])
address, length = win32gui.PyGetBufferAddressAndLen(strBuf)
text = win32gui.PyGetString(address, length)
# ===============================================================
print(text)
title = set()

if win32api.SendMessage(135096, win32con.CB_SETCURSEL, 1, 0):
    win32api.SendMessage(135128, win32con.WM_COMMAND, 0x90000, 135096)
    win32api.SendMessage(135128, win32con.WM_COMMAND, 0x10000, 135096)

win32gui.SetActiveWindow(134958)

print(win32gui.GetWindowRect(134958))
win32gui.PostMessage(134958, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON,
                     win32api.MAKELONG(150, 15))
win32gui.PostMessage(134958, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON,
                     win32api.MAKELONG(150, 15))
win32api.Sleep(1111)
win32gui.PostMessage(134958, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON,
                     win32api.MAKELONG(150, 455))
win32gui.PostMessage(134958, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON,
                     win32api.MAKELONG(150, 455))

print(win32gui.SendMessage(2164210, commctrl.LVM_GETITEMCOUNT))
