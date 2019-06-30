#!/usr/bin/python3

import urwid
import menu


def mainmenu(title, menuchoices):
    #print out the menu (urwid)
    body = [urwid.Text(title), urwid.Divider()]
    for choice in menuchoices:
        button = urwid.Button(choice)
        urwid.connect_signal(button, 'click', item_chosen, choice)
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def item_chosen(button, choice):
    response = urwid.Text([u'You chose ', choice, u'\n'])
    done = urwid.Button(u'OK')
    urwid.connect_signal(done, 'click', exit_program)
    main.original_widget = urwid.Filler(urwid.Pile([response,
        urwid.AttrMap(done, None, focus_map='reversed')]))

def exit_program(button):
    raise urwid.ExitMainLoop()



# load the menu (main menu)
title = 'FSELIN 0.01'
dictMainmenu = {1: 'Aircraft Sales', 2: 'Airport Information', 3: 'Your Hanger',
        4: 'Exit'}
menuOptions = ['Aircraft Sales', 'Airport Information', 'Your Hanger', 'Exit']

main = urwid.Padding(mainmenu(title, menuOptions), left=2, right=2)
top = urwid.Overlay(main, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
        align='center', width=('relative', 60),
        valign='middle', height=('relative', 60),
        min_width=20, min_height=9)
urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()
