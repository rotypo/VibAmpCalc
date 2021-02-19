#!/usr/bin/env python

import PySimpleGUI as sg

PI = 3.1415

def calcUnitAmp(unit, freq, amp):
    ampls = [0,0,0]
    if unit[0] == 'Acceleration':
        ampls = [amp, amp/(2*3.14*freq), amp/(2*3.14*freq)**2]
    elif unit[0] == 'Velocity':
        ampls = [amp*2*PI*freq, amp, amp/(2*PI*freq)]
    elif unit[0] == 'Displacement':
        ampls = [amp*(2*PI*freq)**2, amp*2*PI*freq, amp]
    return ampls

input_column = [
    [
        sg.Text("Frequency [Hz]"),
        sg.In(size=(15,1), enable_events=True, key="-FREQUENCY-")
    ],
    [
        sg.Text("Convert from: "),
        sg.Listbox(
            values=["Acceleration","Displacement","Velocity"],
            enable_events=True, size=(15,1), key="-UNIT-"
        )
    ],
    [
        sg.Text("Amplitude: "),
        sg.In(size=(15,1), enable_events=True, key="-AMPLITUDE-")
    ]
]

output_column = [
    [
        sg.Text("Acceleration"),
        sg.Text(size=(20,1), key="-ACC_OUT-")
    ],
    [
        sg.Text("Velocity"),
        sg.Text(size=(20,1), key="-VEL_OUT-")
    ],
    [
        sg.Text("Displacement"),
        sg.Text(size=(20,1), key="-DIS_OUT-")
    ]
]

layout = [
    [
        sg.Column(input_column),
        sg.VSeparator(),
        sg.Column(output_column)
    ]
]

window = sg.Window("VibAmpCalc", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "-FREQUENCY-":
        try:
            freq = float(values["-FREQUENCY-"])
            unit = values["-UNIT-"]
            amp = float(values["-AMPLITUDE-"])
            amps = calcUnitAmp(unit,freq,amp)
        except:
            amps = [0, 1, 0]
        window["-ACC_OUT-"].update(amps[0])
        window["-VEL_OUT-"].update(amps[1])
        window["-DIS_OUT-"].update(amps[2])

    if event == "-AMPLITUDE-":
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

    if event == "-UNIT-":
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

window.close()
