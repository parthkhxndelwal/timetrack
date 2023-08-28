import pygetwindow as gw
import time
import json

# Load existing dictionary from the JSON file
def load_dictionary(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save dictionary to the JSON file
def save_dictionary(file_name, window_dict):
    with open(file_name, 'w') as file:
        json.dump(window_dict, file, indent=4)

def main():
    file_name = "window_dict.json"
    window_dict = load_dictionary(file_name)

    while True:
        active_window = gw.getActiveWindow()
        if active_window:
            window_name = active_window.title
            if "-" in window_name:
                app_name = window_name.rsplit("-", 1)[-1].strip()
                if app_name in window_dict:
                    window_dict[app_name] += 1
                else:
                    window_dict[app_name] = 1

        save_dictionary(file_name, window_dict)
        time.sleep(1)

if __name__ == "__main__":
    main()
