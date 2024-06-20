import FreeSimpleGUI as sg
sg.theme("Black")

feet = sg.Text("Enter feet: ")
feetInput = sg.Input(key="feet")

inches = sg.Text("Enter inches: ")
inchesInput = sg.Input(key="inches")

convert_Button = sg.Button("Convert")
exit = sg.Button("Exit", key="exit",)
result = sg.Text(key="result")

window = sg.Window("Convertor", layout=[
    [feet, feetInput],
    [inches, inchesInput],
    [convert_Button, exit,  result]
])

while True:
    event, values = window.read()

    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

    try:
        feetValue = float(values['feet'])
        inchValue = float(values['inches'])

        meterValue = f"{feetValue * 0.3048 + inchValue * 0.0254} m"
        window["result"].update(value=meterValue)

    except ValueError:
        sg.popup("Please provide tow numbers.", font=("Helvetica", 20))
window.close()


