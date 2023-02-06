import PySimpleGUI as sg

NewTheme = {
    'BACKGROUND'    : '#97cba9',
    'TEXT'          : '#feffdf',
    'INPUT'         : '#dde0ab',
    'TEXT_INPUT'    : '#000000',
    'SCROLL'        : '#dde0ab',
    'BUTTON'        : ('white', '#668ba4'),
    'PROGRESS'      : ('#283b5b', '#f0f3f7'),
    'BORDER'        : 1,
    'SLIDER_DEPTH'  : 0,
    'PROGRESS_DEPTH': 0,
    'COLOR_LIST'    : ['#668ba4', '#97cba9', '#dde0ab', '#feffdf'],
    'DESCRIPTION'   : ['Yellow', 'Green', 'Turquoise', 'Blue', 'Wedding']}

NewTheme2 = {
    'BACKGROUND'    : '#6c5b7c',
    'TEXT'          : '#f8b595',
    'INPUT'         : '#f67280',
    'TEXT_INPUT'    : '#000000',
    'SCROLL'        : '#f67280',
    'BUTTON'        : ('black', '#f8b595'),
    'PROGRESS'      : ('#283b5b', '#f0f3f7'),
    'BORDER'        : 1,
    'SLIDER_DEPTH'  : 0,
    'PROGRESS_DEPTH': 0,
    'COLOR_LIST'    : ['#6c5b7c', '#c06c84', '#f67280', '#f8b595'],
    'DESCRIPTION'   : ['Orange', 'Red', 'Purple', 'Pastel', 'Halloween',
                       'Skin']}

NewTheme3 = {
    'BACKGROUND'    : '#74b49b',
    'TEXT'          : '#1c1124',
    'INPUT'         : '#693e52',
    'TEXT_INPUT'    : '#000000',
    'SCROLL'        : '#1c1124',
    'BUTTON'        : ('#a7d7c5', '#693e52'),
    'PROGRESS'      : ('#283b5b', '#f0f3f7'),
    'BORDER'        : 1,
    'SLIDER_DEPTH'  : 0,
    'PROGRESS_DEPTH': 0,
    'COLOR_LIST'    : ['#1c1124', '#693e52', '#74b49b', '#a7d7c5'],
    'DESCRIPTION'   : ['Black', 'Green', 'Vintage', 'Wedding']}

NewTheme4 = {
    'BACKGROUND'    : '#292725',
    'TEXT'          : '#ff6107',
    'INPUT'         : '#e9290f',
    'TEXT_INPUT'    : '#000000',
    'SCROLL'        : '#e9290f',
    'BUTTON'        : ('black', '#ff6107'),
    'PROGRESS'      : ('#283b5b', '#f0f3f7'),
    'BORDER'        : 1,
    'SLIDER_DEPTH'  : 0,
    'PROGRESS_DEPTH': 0,
    'COLOR_LIST'    : ['#292725', '#c40018', '#e9290f', '#ff6107'],
    'DESCRIPTION'   : ['Orange', 'Red', 'Black', 'Warm']}

sg.theme_add_new('MyNewTheme', NewTheme)
sg.theme_add_new('MyNewTheme2', NewTheme2)
sg.theme_add_new('MyNewTheme3', NewTheme3)
sg.theme_add_new('MyNewTheme4', NewTheme4)

layout = [[sg.Text('My one-shot window.')],
          [sg.InputText()],  # Or [sg.InputText(key='-IN-')],
          [sg.Submit(), sg.Cancel()]]

sg.theme('MyNewTheme2')
window = sg.Window('Window Title',
                   layout,
                   no_titlebar=True,
                   alpha_channel=.8,
                   grab_anywhere=True)

event, values = window.read()
window.close()

text_input = values[0]  # Or text_input = values['-IN-']
sg.popup('You entered', text_input)