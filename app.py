from flask import Flask, render_template, redirect, url_for, request
import cv2
import pyautogui
from stack import *
import requests, json
import time
app = Flask(__name__)

STACK = make_empty_stack()
def site():
    return render_template('mobilesite.html')


@app.route('/')
def tvsite():
    while True:
        if is_empty(STACK):
            pass
        elif top(STACK) == 'cursed':
            try:
                pop(STACK)
            except IndexError:
                continue
            display_video('static/Cursed Images.mp4')
            print(STACK)
        elif top(STACK) == 'close':
            try:
                pop(STACK)
            except IndexError:
                continue
            time.sleep(3)
            pyautogui.typewrite('q')


@app.route("/command/<cmd>", methods=['POST', 'GET'])
def send_cmd(cmd):
    push(STACK, cmd)
    print(STACK)
    return redirect(url_for('site'))


def display_video(filename):
    name = 'cursed'
    framewait_ms = 30

    cap = cv2.VideoCapture(filename)

    if not cap.isOpened():
        print('yikes didnt work')
        exit()

    cv2.namedWindow(name, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while True:
        ret, frame = cap.read()
        if not ret:
            print('video over')
            break

        cv2.imshow(name, frame)
        if cv2.waitKey(framewait_ms) & 0x7F == ord('q'):
            print('exiting')
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
