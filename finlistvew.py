# 这段代码 只支持32bit 的其他程序 syslistview32 控件 需要32位的pyhon
from win32con import *
from commctrl import *
import win32con
import win32gui
import win32api
import ctypes
import struct
import os



win32api.LoadLibrary
GetWindowThreadProcessId = ctypes.windll.user32.GetWindowThreadProcessId
VirtualAllocEx = ctypes.windll.kernel32.VirtualAllocEx
VirtualFreeEx = ctypes.windll.kernel32.VirtualFreeEx
OpenProcess = ctypes.windll.kernel32.OpenProcess
WriteProcessMemory = ctypes.windll.kernel32.WriteProcessMemory
ReadProcessMemory = ctypes.windll.kernel32.ReadProcessMemory
memcpy = ctypes.cdll.msvcrt.memcpy


def rereadListViewItems(hwnd, column_index=0):
    # Allocate virtual memory inside target process
    pid = ctypes.create_string_buffer(4)
    print('pid-', pid)
    p_pid = ctypes.addressof(pid)
    print('p_pid-', p_pid)
    GetWindowThreadProcessId(hwnd, p_pid)

    #  process owning the given hwnd
    hProcHnd = OpenProcess(PROCESS_ALL_ACCESS, False,
                           struct.unpack("i", pid)[0])
    print(hProcHnd)
    pLVI = VirtualAllocEx(hProcHnd, 0, 4096, MEM_RESERVE |
                          MEM_COMMIT, PAGE_READWRITE)
    pBuffer = VirtualAllocEx(
        hProcHnd, 0, 4096, MEM_RESERVE | MEM_COMMIT, PAGE_READWRITE)
    print('pBuffer', pBuffer)

    # Prepare an LVITEM record and write it to target process memory
    lvitem_str = struct.pack(
        'iiiiiiiii', *[0, 0, column_index, 0, 0, pBuffer, 4096, 0, 0])
    print('lvitem_str', lvitem_str)
    lvitem_buffer = ctypes.create_string_buffer(lvitem_str)
    print('lvitem_buffer', lvitem_buffer)
    copied = ctypes.create_string_buffer(4)
    print('copied', copied)
    p_copied = ctypes.addressof(copied)
    print('p_copied', p_copied)
    WriteProcessMemory(hProcHnd, pLVI, ctypes.addressof(
        lvitem_buffer), ctypes.sizeof(lvitem_buffer), p_copied)
    print('pLVI', pLVI)

    # iterate items in the SysListView32 control

    num_items = win32gui.SendMessage(hwnd, LVM_GETITEMCOUNT)
    print('num_items', num_items)
    item_texts = []
    for item_index in range(num_items):
        win32gui.SendMessage(hwnd, LVM_GETITEMTEXT, item_index, pLVI)
        
        win32api.Sleep(111)
        print(win32gui.SendMessage(hwnd,NM_KEYDOWN, item_index, pLVI))
        # print(win32gui.SendMessage(hwnd, LVM_GETITEMTEXT, item_index, pLVI))
        target_buff = ctypes.create_string_buffer(4096)
        # print('target_buff',target_buff)
        ReadProcessMemory(hProcHnd, pBuffer, ctypes.addressof(
            target_buff), 4096, p_copied)
        # print('target_buff',target_buff)
        item_texts.append(target_buff.value)
        # print(target_buff.value)

    VirtualFreeEx(hProcHnd, pBuffer, 0, MEM_RELEASE)
    VirtualFreeEx(hProcHnd, pLVI, 0, MEM_RELEASE)
    win32api.CloseHandle(hProcHnd)
    return item_texts


tex1 = rereadListViewItems(462910)
print(len(tex1))
print(tex1)
# print(os.name)
