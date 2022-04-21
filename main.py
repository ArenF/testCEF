import ctypes
import sys
import platform
import minecraft_launcher_lib

from cefpython3 import cefpython as cef


def main():
    sys.excepthook = cef.ExceptHook
    cef.Initialize()

    browser = cef.CreateBrowserSync(url='file:///H:/PythonDevelopment/Learning/testCEF/html5up-aerial/index.html',
                                    window_title='aerial launcher')
    if platform.system() == "Windows":
        window_handle = browser.GetOuterWindowHandle()
        insert_after_handle = 0
        SWP_NOMOVE = 0x0002
        ctypes.windll.user32.SetWindowPos(window_handle, insert_after_handle, 0, 0, 1440, 810, SWP_NOMOVE)

    set_javascript_bindings(browser)
    cef.MessageLoop()
    cef.Shutdown()


class SecondWindow(object):

    def __init__(self, browser):
        self.browser = browser

    def newWindow(self):
        newBrowser = cef.CreateBrowserSync(url='https://www.youtube.com', window_title='aerial_window')
        



class External(object):
    target_dir_path = ''

    def __init__(self, browser):
        self.browser = browser

    def ask_dir_path(self):
        from tkinter.filedialog import askdirectory
        from tkinter import Tk

        Tk().withdraw()
        self.target_dir_path = askdirectory()
        self.browser.ExecuteFunction('updatePath', self.target_dir_path)


def py_confirm(path):
    print('success' + path)
    
def py_log(msg):
    print(msg)


def set_javascript_bindings(browser):
    external = External(browser)
    secondWindow = SecondWindow(browser)
    bindings = cef.JavascriptBindings(bindToFrames=False, bindToPopups=False)

    bindings.SetFunction('py_confirm', py_confirm)
    bindings.SetFunction('py_log', py_log)
    bindings.SetObject('external', external)
    bindings.SetObject('secondWindow', secondWindow)

    browser.SetJavascriptBindings(bindings)


if __name__ == "__main__":
    main()
