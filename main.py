#!/usr/bin/env python

import PySimpleGUI as sg

PI = 3.1415

def calcUnitAmp(unit, freq, amp):
    if unit == "Acceleration":
        print(unit)
        ampls = [amp, amp/(2*PI*freq), amp/(2*PI*freq)**2]
    elif unit == "Velocity":
        ampls = [amp*2*PI*freq, amp, amp/(2*PI*freq)]
    elif unit == "Displacement":
        ampls = [amp*(2*PI*freq)**2, amp*2*PI*freq, amp]
    else:
        ampls = [0, 0, 0]
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
    print(values)
    if event == sg.WIN_CLOSED:
        break

    if event == "-FREQUENCY-":
        freq = values["-FREQUENCY-"]
        unit = values["-UNIT-"]
        try:
            amp = values["-AMPLITUDE-"]
            amps = calcUnitAmp(unit,freq,amp)
        except:
            amps = [0, 0, 0]

        window["-ACC_OUT-"].update(amps[0])
        window["-VEL_OUT-"].update(amps[1])
        window["-DIS_OUT-"].update(amps[2])

    if event == "-AMPLITUDE-":
        amp = values["-AMPLITUDE-"]
        unit = values["-UNIT-"]
        try:
            freq = values["-FREQUENCY-"]
            amps = calcUnitAmp(unit,freq,amp)
        except:
            amps = [0, 0, 0]

        window["-ACC_OUT-"].update(amps[0])
        window["-VEL_OUT-"].update(amps[1])
        window["-DIS_OUT-"].update(amps[2])

    if event == "-UNIT-":
        unit = values["-UNIT-"]
        try:
            freq = values["-FREQUENCY-"]
            amp = values["-AMPLITUDE-"]
            amps = calcUnitAmp(unit,freq,amp)
        except:
            amps = [0, 0, 0]

        window["-ACC_OUT-"].update(amps[0])
        window["-VEL_OUT-"].update(amps[1])
        window["-DIS_OUT-"].update(amps[2])

window.close()
