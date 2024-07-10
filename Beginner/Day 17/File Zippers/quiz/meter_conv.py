import FreeSimpleGUI as sg

feet = sg.Text("Enter feet: ")
feetInput = sg.Input(key="feet")

inches = sg.Text("Enter inches: ")
inchesInput = sg.Input(key="inches")

convert_Button = sg.Button("Convert")
result = sg.Text(key="result")

window = sg.Window("Convertor", layout=[
    [feet, feetInput],
    [inches, inchesInput],
    [convert_Button, result]
])

while True:
    event, values = window.read()
    # print(event, values)
    feetValue = float(values['feet'])
    inchValue = float(values['inches'])
    # print(feetValue, inchValue)
    meterValue = f"{feetValue*0.3048 + inchValue*0.0254} m"
    window["result"].update(value=meterValue)