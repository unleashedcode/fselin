#!/usr/bin/python3
import urwid
import menu
import menuchoices


title = 'FSELIN 0.01'
lst_mainmenu = ['Charter Data', 'Aircraft Sales', 'Airport Information',
                'Your Hanger', 'Exit']

lst_charter = ['Search for jobs at ICAO', 'Display VIP jobs at ICAO',
               'Main Menu', 'Exit']

lst_aircraft = ['Show aircraft world wide sales', 'Show aircraft by country',
                'Show aircraft in price range', 'Show aircraft by model',
                'Main Menu', 'Exit']



nextmenu = lst_mainmenu

screentitle = 'FSE-LIN version 0.1a'
foreground = 'yellow'
background = 'dark cyan'
pallete = [(screentitle, foreground, background)]


def menu(title, menuchoices):
    body = [urwid.Text(title), urwid.Divider()]
    for choice in menuchoices:
        button = urwid.Button(choice)
        urwid.connect_signal(button, 'click', item_chosen, choice)
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))


def exit_program(button):
    raise urwid.ExitMainLoop()


def item_chosen(button, choice):
    # this calls the menu selection and it adds a screen on top
    menuchoices.menuchoice_sel(main, button, choice)


main = urwid.Padding(menu(title, lst_mainmenu), left=2, right=2)
'''
maybe making this run in a while loop with a flag system to change the
loading menus is the only way to make this work'''

top = urwid.Overlay(main,urwid.SolidFill(u'\N{MEDIUM SHADE}'),
                    align='center', width=('relative',60),
                    valign='middle', height=('relative',60),
                    min_width=20, min_height=9)

urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()

