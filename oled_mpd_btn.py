#!/usr/bin/env python
# -*- encoding:utf8 -*-

import time
import subprocess
import RPi.GPIO as GPIO

btn_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def get_secret_command():
    # HIGHがスイッチが押されていない状態
    # LOWがスイッチが押されている状態
    pressed_time = now()
    released_time = now()
    now_state = GPIO.LOW
    last_state = GPIO.HIGH
    input_text = ""
    press_flag = False

    while (not press_flag or now() - released_time < 1000):
        now_state = GPIO.input(btn_pin)
        if (last_state == GPIO.HIGH and now_state == GPIO.LOW):
            pressed_time = now()
        elif (last_state == GPIO.LOW and now_state == GPIO.HIGH):
            press_flag = True
            released_time = now()
            if (released_time - pressed_time < 300):
                input_text += "." 
            elif (released_time - pressed_time > 2000):
                input_text += "*" 
            else:
                input_text += "-" 
        last_state = now_state
        time.sleep(0.05)

    print("input_text: " + input_text)
    return input_text


def now():
    return int(time.time() * 1000)


while True:
    command = get_secret_command()
    if (command == "*"):
        subprocess.call(['shutdown', '-h', 'now'], shell=False)
    elif (command == "."):
        subprocess.call(['mpc', 'next'], shell=False)
    elif (command == ".."):
        subprocess.call(['mpc', 'toggle'], shell=False)
    elif (command == "..."):
        subprocess.call(['mpc', 'prev'], shell=False)
