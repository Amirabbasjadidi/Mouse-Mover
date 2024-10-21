import tkinter as tk
import pyautogui
import os
from threading import Thread
from datetime import datetime
import time
from pynput import mouse
from PIL import Image, ImageDraw
import pystray
from pystray import MenuItem as item


def save_coordinates(x, y):
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    folder_path = os.path.join(desktop_path, 'Timeclick')
    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, 'Coordinates.txt')

    try:
        with open(file_path, 'w') as file:
            file.write(f"{x}, {y}")
        print(f"Coordinates saved: {x}, {y}")
    except Exception as e:
        print(f"Error saving file: {e}")


def on_click(x, y, button, pressed):
    if pressed:
        save_coordinates(x, y)
        return False


def move_mouse():
    try:
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "Timeclick", "Coordinates.txt")

        with open(desktop_path, 'r') as file:
            line = file.readline().strip()
            x, y = map(int, line.split(','))

            pyautogui.moveTo(x, y)
            pyautogui.click()
    except FileNotFoundError:
        print("Coordinates file not found.")
    except ValueError:
        print("The file content is not formatted correctly.")


def check_time():
    start_time = start_entry.get()
    end_time = end_entry.get()

    def monitor_time():
        while True:
            current_time = datetime.now().strftime("%H:%M")

            if start_time:
                while current_time != start_time:
                    current_time = datetime.now().strftime("%H:%M")
                    time.sleep(1)

                move_mouse()

                while current_time == start_time:
                    current_time = datetime.now().strftime("%H:%M")
                    time.sleep(1)

            if end_time:
                while current_time != end_time:
                    current_time = datetime.now().strftime("%H:%M")
                    time.sleep(1)

                move_mouse()


                while current_time == end_time:
                    current_time = datetime.now().strftime("%H:%M")
                    time.sleep(1)

    Thread(target=monitor_time).start()

def change_coordinate():
    message_label.config(text="Double-click anywhere on the screen to set new coordinates...")

    def run_tracker():
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        message_label.config(text="")

    Thread(target=run_tracker).start()


from PIL import Image, ImageDraw


def create_mouse_icon(size=64):

    image = Image.new('RGBA', (size, size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)


    ear_radius = size // 4
    left_ear_center = (size // 4, size // 3)
    right_ear_center = (3 * size // 4, size // 3)

    draw.ellipse((left_ear_center[0] - ear_radius, left_ear_center[1] - ear_radius,
                  left_ear_center[0] + ear_radius, left_ear_center[1] + ear_radius),
                 fill=(200, 200, 200))

    draw.ellipse((right_ear_center[0] - ear_radius, right_ear_center[1] - ear_radius,
                  right_ear_center[0] + ear_radius, right_ear_center[1] + ear_radius),
                 fill=(200, 200, 200))


    face_radius = size // 3
    face_center = (size // 2, 2 * size // 3)
    draw.ellipse((face_center[0] - face_radius, face_center[1] - face_radius,
                  face_center[0] + face_radius, face_center[1] + face_radius),
                 fill=(150, 150, 150))


    eye_radius = size // 12
    left_eye_center = (size // 2 - size // 8, 2 * size // 3 - size // 8)
    right_eye_center = (size // 2 + size // 8, 2 * size // 3 - size // 8)

    draw.ellipse((left_eye_center[0] - eye_radius, left_eye_center[1] - eye_radius,
                  left_eye_center[0] + eye_radius, left_eye_center[1] + eye_radius),
                 fill=(0, 0, 0))

    draw.ellipse((right_eye_center[0] - eye_radius, right_eye_center[1] - eye_radius,
                  right_eye_center[0] + eye_radius, right_eye_center[1] + eye_radius),
                 fill=(0, 0, 0))


    nose_radius = size // 20
    nose_center = (size // 2, 2 * size // 3 + size // 10)
    draw.ellipse((nose_center[0] - nose_radius, nose_center[1] - nose_radius,
                  nose_center[0] + nose_radius, nose_center[1] + nose_radius),
                 fill=(255, 105, 180))


    whisker_length = size // 4
    draw.line([(size // 2 - whisker_length, 2 * size // 3 + size // 10),
               (size // 2 - 2 * whisker_length, 2 * size // 3 + size // 15)],
              fill=(0, 0, 0), width=2)

    draw.line([(size // 2 - whisker_length, 2 * size // 3 + size // 10),
               (size // 2 - 2 * whisker_length, 2 * size // 3 + size // 5)],
              fill=(0, 0, 0), width=2)

    draw.line([(size // 2 + whisker_length, 2 * size // 3 + size // 10),
               (size // 2 + 2 * whisker_length, 2 * size // 3 + size // 15)],
              fill=(0, 0, 0), width=2)

    draw.line([(size // 2 + whisker_length, 2 * size // 3 + size // 10),
               (size // 2 + 2 * whisker_length, 2 * size // 3 + size // 5)],
              fill=(0, 0, 0), width=2)
    return image


def quit_app(icon, item):
    icon.stop()
    window.quit()
    window.destroy()
    os._exit(0)


def show_window(icon, item):
    window.deiconify()


def hide_window():
    window.withdraw()


def setup_tray():
    icon_image = create_mouse_icon(size=64)

    menu = (item('Show', show_window), item('Quit', quit_app))
    icon = pystray.Icon("test", icon_image, "Mouse Mover", menu)

    Thread(target=icon.run).start()


window = tk.Tk()
window.title('Mouse Mover')

tk.Label(window, text="Start Time (HH:MM):").pack(pady=5)
start_entry = tk.Entry(window)
start_entry.pack(pady=5)

tk.Label(window, text="End Time (optional) (HH:MM):").pack(pady=5)
end_entry = tk.Entry(window)
end_entry.pack(pady=5)

start_button = tk.Button(window, text='Set Times', command=check_time)
start_button.pack(pady=10)

change_button = tk.Button(window, text='Change Coordinate', command=change_coordinate)
change_button.pack(pady=10)

message_label = tk.Label(window, text="")
message_label.pack(pady=10)

window.protocol("WM_DELETE_WINDOW", hide_window)

setup_tray()

window.mainloop()
