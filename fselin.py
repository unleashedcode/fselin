#!/usr/bin/python3

import urwid
import menu

title = 'FSELIN 0.01'
lst_mainmenu = ['Charter Data','Aircraft Sales', 'Airport Information', 'Your
        Hanger', 'Main Menu', 'Exit']
lst_charters = ['Search for jobs at ICAO']

def mainmenu(title, menuchoices):
    #print out the menu (urwid)
    body = [urwid.Text(title), urwid.Divider()]
    for choice in menuchoices:
        button = urwid.Button(choice)
        urwid.connect_signal(button, 'click', item_chosen, choice)
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def chartermenu(title, menuchoices):
    #print out the charter menu (urwid)
    body = [urwid.Text(title), urwid.Divider()]
    for choice in menuchoices:
        button = urwid.Button(choice)
        urwid.connect_signal(button, 'click', item_chosen, choice)
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def choicechecker(choice):

    if (choice = 'Main Menu'):
        main = urwid.Padding(mainmenu('Main Menu', lst_mainmenu),
                left=2, right=2)
    return main

    if (choice = 'Charter Data'):
        main = urwid.Padding(chartermenu('Charters', lst_charters),
                left=2, right=2)
    return main

    if (choice = 'Exit'):
        urwid.connect_signal(done, 'click', exit_program)

def item_chosen(button, choice):
    # with item chosen check to get relevant menu to pass in
    selected = choicechecker(choice)
    if (choice == 'Charter Data'):

    response = urwid.Text([u'You chose ', choice, u'\n'])
    done = urwid.Button(u'OK')
    urwid.connect_signal(done, 'click', exit_program)
    main.original_widget = urwid.Filler(urwid.Pile([response,
        urwid.AttrMap(done, None, focus_map='reversed')]))

def exit_program(button):
    raise urwid.ExitMainLoop()



# load the menu (main menu)

main = urwid.Padding(mainmenu(title, lst_mainmenu), left=2, right=2)
top = urwid.Overlay(main, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
        align='center', width=('relative', 60),
        valign='middle', height=('relative', 60),
        min_width=20, min_height=9)
urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()
