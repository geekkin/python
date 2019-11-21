#coding = utf-8
# 导入 win32gui,win32con
from win32gui import GetMenu,GetSubMenu,GetMenuItemID,PostMessage 
from win32con import WM_COMMAND
from time import sleep


input_hwnd = input('please enter window hwnd number:')
# 查找到任务管理器窗口
#hwnd = win32gui.FindWindow(None, '任务管理器')
print(input_hwnd)
sleep(1)
# 获得任务管理器的菜单句柄
input_hwnd = int(input_hwnd)
menu_hwnd = GetMenu(input_hwnd)
# 获取菜单栏的第3项菜单（下标从0开始）
menu_1lv = GetSubMenu(menu_hwnd, 2)
# 获得下一级菜单的句柄
menu_2lv = GetSubMenu(menu_1lv, 1)
# 获得1级菜单的3项菜单的第4个子菜单 ID
cmd_id = GetMenuItemID(menu_1lv, 3)
# 获得2级菜单的第1个子菜单的 ID
cmd_id2 = GetMenuItemID(menu_2lv, 0)
# 给一个子菜单发送一个点击命令，PostMessage 函数没有返回值
PostMessage(input_hwnd, WM_COMMAND, cmd_id2, 0)
print(u'任务管理器句柄 ：', input_hwnd)
print(u'菜单句柄 ：', menu_hwnd)
print(u'1级菜单 [查看] 句柄 :', menu_1lv)
print(u'子菜单ID ：', cmd_id)
input('enythin key exit app!')
