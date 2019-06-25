#!/usr/bin/python3

import urwid
import os
import time

# main menu - ()
def load_main_menu()
    menulist = {1: "Aircraft Sales", 2: "Airport Information", 3: "Your
    Hanger", 4: "Exit"}

    #print out the menu (urwid)_
    body = [urwid.Text(title), urwid.Divider()]
    for c in menulist:
        button = urwid.Button(c)
        urwid.connect_signal(button, click, item_selected, c)
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))
        choice(mainM
