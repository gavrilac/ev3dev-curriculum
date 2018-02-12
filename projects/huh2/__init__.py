#!/usr/bin/env python3


"""
Authors:  Hao Hu.
"""


import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com


def main():
    while True:
        if
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3("mosquitto.csse.rose-hulman.edu", 8)



    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    left_speed_label = ttk.Label(main_frame, text="Left")
    left_speed_label.grid(row=0, column=0)
    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.insert(0, "600")
    left_speed_entry.grid(row=1, column=0)

    right_speed_label = ttk.Label(main_frame, text="Right")
    right_speed_label.grid(row=0, column=2)
    right_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "600")
    right_speed_entry.grid(row=1, column=2)

    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=2, column=1)
    # forward_button and '<Up>' key is done for your here...
    forward_button['command'] = lambda: handle_forward_button(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Up>', lambda event: handle_forward_button(mqtt_client, left_speed_entry, right_speed_entry))

    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid(row=3, column=0)
    # left_button and '<Left>' key
    left_button['command'] = lambda: handle_left_button(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Down>'), lambda event: handle_left_button(mqtt_client, left_speed_entry, right_speed_entry)
    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=3, column=1)
    stop_button['command'] = lambda: handle_stop_button(mqtt_client)
    root.bind('<space>'), lambda event: handle_stop_button(mqtt_client)
    # stop_button and '<space>' key (note, does not need left_speed_entry, right_speed_entry)

    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid(row=3, column=2)
    # right_button and '<Right>' key
    right_button['command'] = lambda : handle_right_button(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Right>'), lambda event: handle_right_button(mqtt_client, left_speed_entry, right_speed_entry)
    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=4, column=1)
    back_button['command'] = lambda: handle_back_button(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Down>'), lambda event: handle_back_button(mqtt_client, left_speed_entry, right_speed_entry)
    # back_button and '<Down>' key

    up_button = ttk.Button(main_frame, text="Up")
    up_button.grid(row=5, column=0)
    up_button['command'] = lambda: send_up(mqtt_client)
    root.bind('<u>', lambda event: send_up(mqtt_client))

    down_button = ttk.Button(main_frame, text="Down")
    down_button.grid(row=6, column=0)
    down_button['command'] = lambda: send_down(mqtt_client)
    root.bind('<j>', lambda event: send_down(mqtt_client))

    # Buttons for quit and exit
    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=5, column=2)
    q_button['command'] = (lambda: quit_program(mqtt_client, False))

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=6, column=2)
    e_button['command'] = (lambda: quit_program(mqtt_client, True))
    root.bind_all('<KeyPress>', lambda event: pressed(event, mqtt_client, left_speed_entry, right_speed_entry))
    root.bind_all('<KeyRelease>', lambda event: handle_stop_button(mqtt_client))
    root.mainloop()

def handle_forward_button(mqtt_client, left_speed_entry, right_speed_entry):
    print("foward button")
    mqtt_client.send_message("forward", [left_speed_entry.get(), right_speed_entry.get()])

def handle_left_button(mqtt_client, left_speed_entry, right_speed_entry):
    print("left button")
    mqtt_client.send_message("left", [int(left_speed_entry.get()), int(right_speed_entry.get())])

def handle_right_button(mqtt_client, left_speed_entry, right_speed_entry):
    print("right button")
    mqtt_client.send_message("right",[int(left_speed_entry.get()), int(right_speed_entry.get())])

def handle_back_button(mqtt_client, left_speed_entry, right_speed_entry):
    print("back button")
    mqtt_client.send_message("backward", [int(left_speed_entry.get()), int(right_speed_entry.get())])

def handle_stop_button(mqtt_client):
    print("stop button")
    mqtt_client.send_message("stop")

def send_up(mqtt_client):
    print("arm_up")
    mqtt_client.send_message("arm_up")

def send_down(mqtt_client):
    print("arm_down")
    mqtt_client.send_message("arm_down")

def pressed(event, mqtt_client, left_speed_entry, right_speed_entry):
    print("Pressed")
    if event.keysym == "Up":
        mqtt_client.send_message("forward", [left_speed_entry.get(), right_speed_entry.get()])
    elif event.keysym == "Down":
        mqtt_client.send_message("backward", [int(left_speed_entry.get()), int(right_speed_entry.get())])
    elif event.keysym == "Right":
        mqtt_client.send_message("right_move", [int(left_speed_entry.get()), int(right_speed_entry.get())])
    elif event.keysym == "Left":
        mqtt_client.send_message("left_move", [int(left_speed_entry.get()), int(right_speed_entry.get())])
    elif event.keysym == 'q':
        mqtt_client.send_message("shutdown")
        mqtt_client.close()
        exit()
    elif event.keysym == 'u':
        print("arm_up")
        mqtt_client.send_message("arm_up")
    elif event.keysym == 'j':
        print("arm_down")
        mqtt_client.send_message("arm_down")

def quit_program(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("shutdown")
        mqtt_client.send_message("shutdown")
    mqtt_client.close()
    exit()

main()