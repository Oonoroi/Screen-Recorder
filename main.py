import cv2
import numpy as np
import pyautogui
import pathlib
import webbrowser


def open_downloads():
    dir_path = pathlib.Path(__file__).parent.resolve()
    webbrowser.open("file:///" + str(dir_path) + "\\recordings")


resolution = (1920, 1080)
codec = cv2.VideoWriter_fourcc(*"XVID")
path = pathlib.Path(__file__).parent.resolve()
filename = str(path) + "\\recordings\\screen_recording.avi"
fps = 30.0
out = cv2.VideoWriter(filename, codec, fps, resolution)

# live window
cv2.namedWindow("Window", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Window", 1920, 1080)

print("press the 's' key to start the recording and spam press the 'q' key to end it (idk why it doesn't work first try)")
key_pressed = False
# constantly screenshots and adds said screenshots to a video file
while True:
    screen = pyautogui.screenshot()
    frame = np.array(screen)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow("Window", frame)

    if cv2.waitKey(1) == ord("s"):
        key_pressed = True
        print("recording started")

    if key_pressed:
        out.write(frame)

    if cv2.waitKey(1) == ord("q"):
        print("recording ended")
        break


out.release()
cv2.destroyAllWindows()
open_downloads()
