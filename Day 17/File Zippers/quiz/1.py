import FreeSimpleGUI as sg
button_labels = ("Add", "Edit", "Apply", "End", "Cancel")
layout = []
for label in button_labels:
    layout.append([sg.Button(label)])

window = sg.Window('My To-Do App', layout= layout)
window.read()
window.close()