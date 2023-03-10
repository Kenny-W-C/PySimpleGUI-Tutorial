import PySimpleGUI as sg


def second_window():
    layout = [[sg.Text(
            'The second form is small \nHere to show that opening a window '
            'using '
            'a window works')],
        [sg.OK()]]
    window = sg.Window('Second Form', layout)
    event, values = window.read()
    window.close()


def test_menus():
    sg.theme('LightGreen')
    sg.set_options(element_padding = (0, 0))
    menu_def = [
        ['&File', ['!&Open', '&Save::savekey', '---', '&Properties', 'E&xit']],
        ['&Edit', ['&Paste', ['Special', 'Normal', ], 'Undo'], ],
        ['&Debugger', ['Popout', 'Launch Debugger']],
        ['&Toolbar', ['Command &1', 'Command &2', 'Command &3', 'Command &4']],
        ['&Help', '&About...'], ]
    right_click_menu = ['Unused',
                        ['Right', '&Click', '&Menu', 'E&xit', 'Properties']]

    layout = [
        [sg.MenubarCustom(menu_def, tearoff = False)],
        [sg.Text('Click right on me to see right click menu')],
        [sg.Output(size = (60, 20))],
        [sg.ButtonMenu('ButtonMenu', key = '-BMENU-', menu_def = menu_def[0])],
        [sg.Text('Enter something:'), sg.Input(key = '-IN-')],
        [sg.Text('Our output will go here', size = (30, 1), key = '-OUT-')],
        [sg.Button('OK'), sg.Button('Exit')]]

    window = sg.Window("Windows-like program",
                       layout,
                       default_element_size = (12, 1),
                       grab_anywhere = True,
                       right_click_menu = right_click_menu,
                       default_button_element_size = (12, 1))

    while True:
        event, values = window.read()
        if event is None or event == 'Exit':
            return
        print('Event = ', event)
        # ------ Process menu choices ------ #
        if event == 'About...':
            window.disappear()
            sg.popup('About this program', 'Version 1.0',
                     'PySimpleGUI rocks...', grab_anywhere = True)
            window.reappear()
        elif event == 'Open':
            filename = sg.popup_get_file('file to open', no_window = True)
            print(filename)
        elif event == 'Properties':
            second_window()
        elif event == '-BMENU-':
            print('You selected from the button menu:', values['-BMENU-'])
        window['-OUT-'].update(values['-IN-'])


# window.close()
test_menus()
