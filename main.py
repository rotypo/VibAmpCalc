#!/usr/bin/env python

import PySimpleGUI as sg
from numpy import pi as PI

def calcUnitAmp(unit, freq, amp):
    ampls = [0,0,0]
    if unit == 'Acceleration':
        ampls = [amp, amp/(2*PI*freq), amp/(2*PI*freq)**2]
    elif unit == 'Velocity':
        ampls = [amp*2*PI*freq, amp, amp/(2*PI*freq)]
    elif unit == 'Displacement':
        ampls = [amp*(2*PI*freq)**2, amp*2*PI*freq, amp]
    return ampls

text_column_1 = [
    [
        sg.Text("Frequency [Hz]:")
    ],
    [
        sg.Text("    Convert from:")
    ],
    [
        sg.Text("        Amplitude:")
    ]
]

input_column = [
    [
        sg.In(size=(17,1), enable_events=True, key="-FREQUENCY-")
    ],
    [
        sg.Combo(
            ["Acceleration","Displacement","Velocity"],
            enable_events=True, size=(15,1), key="-UNIT-"
        )
    ],
    [
        sg.In(size=(17,1), enable_events=True, key="-AMPLITUDE-")
    ]
]

text_column_2 = [
    [
        sg.Text("  Acceleration:")
    ],
    [
        sg.Text("        Velocity:")
    ],
    [
        sg.Text("Displacement:")
    ]
]

output_column = [
    [
        sg.Text(size=(20,1), key="-ACC_OUT-")
    ],
    [
        sg.Text(size=(20,1), key="-VEL_OUT-")
    ],
    [
        sg.Text(size=(20,1), key="-DIS_OUT-")
    ]
]

layout = [
    [
        sg.Column(text_column_1),
        sg.Column(input_column),
        sg.VSeparator(),
        sg.Column(text_column_2),
        sg.Column(output_column)
    ]
]

window = sg.Window("VibAmpCalc", layout)

while True:
    event, values = window.read()

    if event == "-FREQUENCY-" or event == "-AMPLITUDE-" or event == "-UNIT-":
        try:
            freq = float(values["-FREQUENCY-"])
            unit = values["-UNIT-"]
            amp = float(values["-AMPLITUDE-"])
            amps = calcUnitAmp(unit,freq,amp)
        except:
            amps = [0, 0, 0]
        window["-ACC_OUT-"].update(amps[0])
        window["-VEL_OUT-"].update(amps[1])
        window["-DIS_OUT-"].update(amps[2])

    if event == sg.WIN_CLOSED:
        break

window.close()
