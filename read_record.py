def load_dictionary(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            window_dict = {}
            for line in lines:
                window_name = line.strip()
                window_dict[window_name] = window_dict.get(window_name, 0) + 1
            return window_dict
    except FileNotFoundError:
        return {}


def display_menu():
    print("1. Display total time spent on all programs")
    print("2. Display time spent on a specific program")
    print("3. Display the most used program")
    print("4. Display programs used for more than a certain time")
    print("5. Exit")

def total_time_spent(window_dict):
    total_time = display_time_in_minutes(sum(window_dict.values()))
    print(f"Total time spent on all programs: {total_time}")

def time_spent_on_program(window_dict, program_name):
    if program_name in window_dict:
        time_spent = display_time_in_minutes(window_dict[program_name])
        print(f"Time spent on {program_name}: {time_spent}")
    else:
        print(f"{program_name} not found in the data")

def most_used_program(window_dict):
    if window_dict:
        most_used_program = max(window_dict, key=window_dict.get)
        time_spent = window_dict[most_used_program]
        print(f"Most used program: {most_used_program} (Time spent: {time_spent} seconds)")
    else:
        print("No program data available")

def programs_above_threshold(window_dict, threshold):
    print(f"Programs used for more than {threshold} seconds:")
    for program, time_spent in window_dict.items():
        if time_spent > threshold:
            print(f"{program}: {time_spent} seconds")

def display_time_in_minutes(seconds):
    minutes = seconds//60
    if (seconds%60)<30:
        if minutes == 0:
            return f"< 1 minutes"
        else:
            return f"> {minutes} minutes"
    else:
        return f"< {minutes+1} minutes"  

if __name__ == "__main__":
    file_name = "window_dict.txt"  
    window_dict = load_dictionary(file_name)

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            total_time_spent(window_dict)
        elif choice == "2":
            program_name = input("Enter the program name: ")
            time_spent_on_program(window_dict, program_name)
        elif choice == "3":
            most_used_program(window_dict)
        elif choice == "4":
            threshold = int(input("Enter the time threshold (in seconds): "))
            programs_above_threshold(window_dict, threshold)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")
