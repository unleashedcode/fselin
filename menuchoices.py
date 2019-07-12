#!/usr/bin/pyhon3

import urwid

def menuchoice_sel(main, button, chosen):
    if (chosen == 'Aircraft Sales'):
        response = urwid.Text([chosen, '\n'])
        
    elif (chosen == 'Charter Data'):
        response = urwid.Text([chosen, '\n'])

    done = urwid.Button('Shit fuck')
    urwid.connect_signal(done, 'click', exit_program)
    main.original_widget = urwid.Filler(urwid.Pile([response, urwid.AttrMap
        (done, None, focus_map='reversed')]))


def exit_program(button):
    raise urwid.ExitMainLoop()


# working on implementing secondary menu system and then their choices
# thereafter



