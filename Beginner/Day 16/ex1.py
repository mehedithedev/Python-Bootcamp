import FreeSimpleGUI as sg
label1 = sg.Text("Enter Feet: ")
input1 = sg.Input()

label2 = sg.Text("Enter inches: ")
input2 = sg.Input()

button = sg.Button("Convert")

window = sg.Window("Convertor", layout=[
    [label1, input1],
    [label2, input2],
    [button]
])

window.read()
window.close()