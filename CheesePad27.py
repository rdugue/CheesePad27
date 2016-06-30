from Tkinter import *
import win32api
import win32con
import time

VK_CODE = {
    'left_arrow': 0x25,
    'up_arrow': 0x26,
    'right_arrow': 0x27,
    'down_arrow': 0x28,
}

TK_KEY_CODE = {
    37: 'left_arrow',
    38: 'up_arrow',
    39: 'right_arrow',
    40: 'down_arrow',
}


def press(*args):
    """
    one press, one release.
    accepts as many arguments as you want. e.g. press('left_arrow', 'a','b').
    """
    for i in args:
        win32api.keybd_event(VK_CODE[i], 0, 0, 0)
        time.sleep(.05)
        win32api.keybd_event(VK_CODE[i], 0, win32con.KEYEVENTF_KEYUP, 0)


def release(*args):
    """
    release depressed keys
    accepts as many arguments as you want.
    e.g. release('left_arrow', 'a','b').
    """
    for i in args:
        win32api.keybd_event(VK_CODE[i], 0, win32con.KEYEVENTF_KEYUP, 0)


class App:
    up_string = u'\u21D1'
    down_string = u'\u21D3'
    left_string = u'\u21D0'
    right_string = u'\u21D2'
    up_right_string = u'\u21D7'
    up_left_string = u'\u21D6'
    down_right_string = u'\u21D8'
    down_left_string = u'\u21D9'

    keyPressed = False
    hoverEvent = None

    def __init__(self, master):
        frame = Frame(master)
        frame.bind('<Key>', self.repeat)
        frame.focus_set()
        frame.pack()

        self.up = Button(frame, text=self.up_string, command=self.key_press, height='5', width='10')
        self.up.grid(row=0, column=1)
        self.left = Button(frame, text=self.left_string, command=self.key_press, height='5', width='10')
        self.left.grid(row=1, column=0)
        self.right = Button(frame, text=self.right_string, command=self.key_press, height='5', width='10')
        self.right.grid(row=1, column=2)
        self.down = Button(frame, text=self.down_string, command=self.key_press, height='5', width='10')
        self.down.grid(row=2, column=1)
        self.top_left = Button(frame, text=self.up_left_string, command=self.key_press, height='5', width='10')
        self.top_left.grid(row=0, column=0)
        self.down_left = Button(frame, text=self.down_left_string, command=self.key_press, height='5', width='10')
        self.down_left.grid(row=2, column=0)
        self.top_right = Button(frame, text=self.up_right_string, command=self.key_press, height='5', width='10')
        self.top_right.grid(row=0, column=2)
        self.down_right = Button(frame, text=self.down_right_string, command=self.key_press, height='5', width='10')
        self.down_right.grid(row=2, column=2)

        self.up.bind('<Enter>', self.key_hover)
        self.up.bind('<Leave>', self.key_leave_hover)

        self.left.bind('<Enter>', self.key_hover)
        self.left.bind('<Leave>', self.key_leave_hover)

        self.right.bind('<Enter>', self.key_hover)
        self.right.bind('<Leave>', self.key_leave_hover)

        self.down.bind('<Enter>', self.key_hover)
        self.down.bind('<Leave>', self.key_leave_hover)

        self.top_left.bind('<Enter>', self.key_hover)
        self.top_left.bind('<Leave>', self.key_leave_hover)

        self.down_left.bind('<Enter>', self.key_hover)
        self.down_left.bind('<Leave>', self.key_leave_hover)

        self.top_right.bind('<Enter>', self.key_hover)
        self.top_right.bind('<Leave>', self.key_leave_hover)

        self.down_right.bind('<Enter>', self.key_hover)
        self.down_right.bind('<Leave>', self.key_leave_hover)

    def parse_keys_down(self, widget):
        if widget.cget('text') == self.up_string:
            press('up_arrow')
        elif widget.cget('text') == self.down_string:
            press('down_arrow')
        elif widget.cget('text') == self.left_string:
            press('left_arrow')
        elif widget.cget('text') == self.right_string:
            press('right_arrow')
        elif widget.cget('text') == self.up_left_string:
            press('up_arrow', 'left_arrow')
        elif widget.cget('text') == self.up_right_string:
            press('up_arrow', 'right_arrow')
        elif widget.cget('text') == self.down_left_string:
            press('down_arrow', 'left_arrow')
        elif widget.cget('text') == self.down_right_string:
            press('down_arrow', 'right_arrow')

    def repeat(self, event):
        if self.keyPressed:
            time.sleep(.05)
            press(TK_KEY_CODE[event.keycode])
            print "test repeat: ", TK_KEY_CODE[event.keycode]

    def key_press(self):
        print "Test"

    def key_hover(self, event):
        event.widget.config(bg='green')
        self.parse_keys_down(event.widget)
        self.keyPressed = True
        self.hoverEvent = event

    def key_leave_hover(self, event):
        event.widget.config(bg='gray')
        self.keyPressed = False

    def key_double_press(self, event):
        print "Double Click Test"


root = Tk()
root.title("CheesePad")
app = App(root)
root.attributes('-alpha', 0.3)
root.wm_attributes('-topmost', 1)
root.resizable(width=FALSE, height=FALSE)
root.mainloop()
root.destroy()
