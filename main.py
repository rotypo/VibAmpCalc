#!/usr/bin/env python

import PySimpleGUI as sg

input_column = [
        [
            sg.Text("Frequency [Hz]"),
            sg.In(size=(15,1), enable_events=True, key="-FREQUENCY-")
        ],
        [
            sg.Text("Convert from: "),
            sg.Listbox(
                values=["A","D","V"], enable_events=True, size=(15,1), key="-UNIT-"
            )
        ],
]

layout = [
        [
            sg.Column(input_column),
        ]
]

window = sg.Window("VibAmpCalc", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
