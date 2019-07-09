
#!/usr/bin/python3 
import urwid
import menu

title = 'FSELIN 0.01'
lst_mainmenu = ['Charter Data','Aircraft Sales', 'Airport Information',
                'Your Hanger', 'Exit']
lst_charters = ['Search for jobs at ICAO', 'Display VIP jobs at ICAO', 'Main Menu', 'Exit']


screentitle = 'FSE-LIN version 0.1a'
foreground = 'yellow'
background = 'dark cyan'
pallete = [(screentitle, foreground, background),]

def menu(title, menuchoices):
    body = [urwid.Text(title), urwid.Divider()]
    for choice in menuchoices:
        button = urwid.Button(choice)
        urwid.connect_signal(button, 'click', item_chosen, choice)
        body.append(urwid.AttrMap(button, None, focusJ_map='reversed'))
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def exit_program(button):
    raise urwid.ExitMainLoop()

def item_chosen(button, choice):
    response = urwid.Text(['You chose......', choice, u'\n'])
    pass

main = urwid.Padding(menu(title, menuselection), left=2, right=2)

top = urwid.Overlay(main,urwid.SolidFill(u'\N{MEDIUM SHADE}'),
        align='center', width=('relative',60),
        valign='middle', height=('relative',60),
        min_width=20, min_height=9)

urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()


