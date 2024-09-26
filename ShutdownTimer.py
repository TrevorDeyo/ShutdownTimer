import os
import re
import time

def schedule_shutdown():
    while True:
        # Take input from the user
        time_input = input("Enter the time to shutdown your PC (e.g., 30m for 30 minutes, 1.5h for 1 hour 30 minutes): ").strip()

        # Check if the input is valid (matches the format XXm or XXh, including decimal numbers)
        match = re.match(r"^(\d+(\.\d+)?)([mh])$", time_input)
        if not match:
            print("Invalid input! Please enter time in the format 'XXm' (minutes) or 'XXh' (hours), including decimals like '1.5h'.")
            continue  # Ask again if the input is invalid

        # Extract the time and unit
        value, unit = match.groups()[0], match.groups()[2]
        value = float(value)  # Convert to float to handle decimals

        # Calculate time in seconds
        if unit == 'm':
            seconds = int(value * 60)  # Convert minutes to seconds
        elif unit == 'h':
            seconds = int(value * 3600)  # Convert hours to seconds

        # Schedule the shutdown
        print(f"Shutting down in {value} {'minutes' if unit == 'm' else 'hours'}...")
        os.system(f"shutdown /s /t {seconds}")

        # Keep the program open for 10 seconds so the user can see the message
        time.sleep(10)
        break  # Exit the loop after scheduling the shutdown

if __name__ == "__main__":
    schedule_shutdown()
