#!/usr/bin/python3

import urwid
import os
import time

# menu system - displays the menu
def mainmenu(title, dictMainmenu):

    #print out the menu (urwid)_
    body = [urwid.Text(title), urwid.Divider()]
    for choice in dictMainmenu:
        button = urwid.Button(choice)
        urwid.connect_signal(button, click, item_selected, choice)
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))


def item_chosen(button, choice):
    response = urwid.Text([u'You chose ', choice, u'\n'])
    done = urwid.Button(u'OK')
    urwid.connect_signal(done, 'click', exit_program)
    main.original_widget = urwwid.Filler(urwid.Pile([response,
        urwid.AttrMap(done, None,focus_map='reversed')]))


def exit_program(button):
    raise urwid.ExitMainLoop()
