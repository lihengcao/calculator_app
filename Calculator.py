import tkinter as tk
import tkinter.font as font
from functools import partial


def eval_expression(arg1: str, operation: str, arg2: str):
    if operation == '+':
        return str(int(r)) if int(r := float(arg1) + float(arg2)) == int(r) else str(r)
    if operation == '-':
        return str(int(r)) if int(r := float(arg1) - float(arg2)) == int(r) else str(r)
    if operation == '*':
        return str(int(r)) if int(r := float(arg1) * float(arg2)) == int(r) else str(r)
    if operation == '/':
        if arg2 == '0':
            return 'Error'
        return str(int(r)) if int(r := float(arg1) / float(arg2)) == int(r) else str(r)


class Calculator:
    def button_command(self, key: str):  # handler for calculator button presses
        if key.isdigit():
            if self.replace or ((self.display['text']) == '0' and key != 0):
                # replace number if there's a 0 or an operation button was clicked last, otherwise concat
                self.display['text'] = str(key)
                self.clicked_op = False
            else:
                self.display['text'] += str(key)
        elif key == '.':
            if '.' not in self.display['text']:
                self.display['text'] += '.'
        elif key == 'C':
            self.display['text'] = '0'
            self.arg = None
            self.prev_op = None
            self.clicked_op = False
        elif key in '+-*/':
            if self.arg:
                self.arg = eval_expression(self.arg, key, self.display['text'])
                self.display['text'] = self.arg
            else:
                self.arg = self.display['text']
                self.replace = True
            self.prev_op = key
        elif key == '=':
            if self.arg:
                self.arg = eval_expression(self.arg, self.prev_op, self.display['text'])
                self.display['text'] = self.arg
        elif key == 'sign':
            self.display['text'] = str(-1 * int(self.display['text']))
        elif key == '%':
            self.display['text'] = str(float(self.display['text']) / 100.0)

        print('arg: {}, op/key: {}, last_op: {}, replace: {}'.format(self.arg, key, self.prev_op, self.replace))

    def __init__(self, font_size=10):
        self.arg = None
        self.prev_op = None
        self.prev_arg = None
        self.replace = False

        self.font = (None, font_size)

        self.app_window = tk.Tk()  # main app window
        self.app_window.title('Calculator')  # name the window
        self.app_window.resizable(False, False)  # don't allow resize in either dimension

        self.display = tk.Label(text='0', height=2, anchor='e', font=self.font)  # display for the numbers
        self.display.config(relief=tk.SUNKEN)  # make display have a sunken border
        self.display.grid(row=0, columnspan=5, sticky='news')  # make display go across the entire first row

        self.buttons = {}
        b = [  # configurations of the buttons
            ('C', 'C', '#D3D3D3', 1, 0),
            ('sign', '+/-', '#D3D3D3', 1, 1),
            ('%', '%', '#D3D3D3', 1, 2),
            ('/', '÷', 'orange', 1, 3),
            ('7', 7, 'gray', 2, 0),
            ('8', 8, 'gray', 2, 1),
            ('9', 9, 'gray', 2, 2),
            ('*', '×', 'orange', 2, 3),
            ('4', 4, 'gray', 3, 0),
            ('5', 5, 'gray', 3, 1),
            ('6', 6, 'gray', 3, 2),
            ('-', '-', 'orange', 3, 3),
            ('1', 1, 'gray', 4, 0),
            ('2', 2, 'gray', 4, 1),
            ('3', 3, 'gray', 4, 2),
            ('+', '+', 'orange', 4, 3),
            ('0', 0, 'gray', 5, 0),
            ('.', '.', 'gray', 5, 2),
            ('=', '=', 'orange', 5, 3)
        ]

        for key, text, bg, r, c in b:
            self.buttons[key] = tk.Button(text=text, height=3, width=5, padx=0, pady=0, bg=bg, font=self.font,
                                          command=partial(self.button_command, key))
            if key == '0':  # 0 button takes up 2 spaces
                self.buttons['0'].grid(row=r, column=c, columnspan=2, sticky='news')
            else:
                self.buttons[key].grid(row=r, column=c)

        # self.debug = tk.Label(height=2, anchor='e')  # display for the numbers
        # self.debug.config(relief=tk.SUNKEN)  # make display have a sunken border
        # self.debug.grid(row=6, columnspan=5, sticky='news')  # make display go across the entire first row
