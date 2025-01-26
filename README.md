# Mouse Mover Application

**I doubt this will be useful for you**, but I needed this for myself, so I made it. I figured someone else might need it too, so here it is!

This is a simple Python application that moves the mouse to a pre-defined coordinate on the screen at specific times.

## Features

- **Time-based mouse movement**: Automatically move the mouse to a specified location at given start and end times.
- **Coordinate customization**: Double-click anywhere on the screen to change the mouse movement target coordinates.
- **System tray integration**: Hide the main window and control the app from the system tray, including the options to show the app or quit.
- **Simple UI**: Easily set start and end times, and change coordinates through a graphical interface.

## Download the Executable

If you don't want to deal with Python setup and dependencies, you can download the **executable file (exe)** from the [Releases](https://github.com/Amirabbasjadidi/Mouse-Mover/releases/) section.

## Requirements

To run this program from the source code, you need the following Python libraries:

- `tkinter` (comes with Python standard library)
- `pyautogui`
- `pynput`
- `Pillow` (for image drawing and system tray icon)
- `pystray`
  
You can install the required libraries using pip:

```bash
pip install -r requirements.txt
```

## How to Use

1. **Set Times**: Enter the start time (required) and an optional end time in the format `HH:MM` (24-hour clock).
2. **Change Mouse Coordinates**: To change the coordinates where the mouse will move, click the "Change Coordinate" button and double-click anywhere on your screen. The new coordinates will be saved to your desktop.
3. **System Tray**: The application can be minimized to the system tray. You can reopen the app or quit it from the tray icon menu.

## How It Works

- The program listens for mouse clicks and saves the coordinates of the click to a file on the desktop.
- It monitors the system time and moves the mouse to the saved coordinates at the defined times, simulating a click.
- The user interface allows setting the times and changing the target coordinates through a simple GUI.

## Running the App

To run the application, simply execute the Python script:

```bash
python Main.py
```

Alternatively, you can download the ready-to-use `.exe` from the [Releases](https://github.com/Amirabbasjadidi/Mouse-Mover/releases/) page.

## License

This project is licensed under the GPL-V3 License. See the [LICENSE](LICENSE) file for more details.
