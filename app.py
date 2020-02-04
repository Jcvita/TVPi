from flask import Flask, render_template, redirect, url_for, request
import cv2
import pyautogui
# import time
from stack import *

app = Flask(__name__)

STACK = make_empty_stack()


@app.route('/')
def site():
    return render_template('mobilesite.html')


@app.route('/tv/')
def tvsite():
    while True:
        if is_empty(STACK):
            pass
        elif top(STACK) == 'cursed':
            display_video('static/Cursed Images.mp4')


@app.route("/cursed/", methods=['POST', 'GET'])
def cursed():
    push(STACK, 'cursed')
    print(STACK)
    return redirect(url_for('site'))


@app.route("/close/", methods=['POST', 'GET'])
def close():
    pyautogui.typewrite('q')
    return redirect(url_for('site'))


def display_video(filename):
    pop(STACK)

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
