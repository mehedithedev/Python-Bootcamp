import FreeSimpleGUI as sg

left_colum_content = [
    [sg.Text("Left 1")],
    [sg.Text("Left 2")]
]

right_colum_content = [
    [sg.Text("Right 1")],
    [sg.Text("Right 2")]
]

left_column = sg.Column(left_colum_content)
right_column = sg.Column(right_colum_content)

layout = [left_column, right_column]

window = sg.Window('Columns', layout=layout)

window.read()
window.close()