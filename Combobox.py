def save_to_image(self, filePath, format="jpg"):
        format_dict = {
            "bmp": 0,  # Facegen的Bug导致无法保存bmp
            "jpg": 1,
            "tga": 2,
            "tif": 3,
        }
        Mhandle, confirmBTN_handle = self.menu_command('save_to_image')
        mhandle = find_subHandle(Mhandle, [("DUIViewWndClassName", 0), ("DirectUIHWND", 0)])
        EDIT_handle = find_subHandle(mhandle, [("FloatNotifySink", 0), ("ComboBox", 0), ("Edit", 0)])  # 定位保存地址句柄
        PCB_handle = find_subHandle(mhandle, [("FloatNotifySink", 1)])  # 定位下拉菜单父窗体句柄
        CB_handle = find_subHandle(PCB_handle, [("ComboBox", 0)])  # 定位下拉菜单窗体句柄
        wait_and_assert(EDIT_handle, find_subHandle(mhandle, [("FloatNotifySink", 0), ("ComboBox", 0), ("Edit", 0)]))
        # 以下3行皆为ComboBox的list中选择格式必要的Message操作
        if win32api.SendMessage(CB_handle, win32con.CB_SETCURSEL, format_dict[format], 0) == format_dict[format]:
            win32api.SendMessage(PCB_handle, win32con.WM_COMMAND, 0x90000, CB_handle)
            win32api.SendMessage(PCB_handle, win32con.WM_COMMAND, 0x10000, CB_handle)
        else:
            raise Exception("Change saving type failed")
        # 填入保存地址，确认
        if win32api.SendMessage(EDIT_handle, win32con.WM_SETTEXT, 0, os.path.abspath(filePath).encode('gbk')) == 1:
            return win32api.SendMessage(Mhandle, win32con.WM_COMMAND, 1, confirmBTN_handle)
        raise Exception("Set file opening path failed")
# ————————————————
# 版权声明：本文为CSDN博主「橘子一方」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/seele52/article/details/17723121