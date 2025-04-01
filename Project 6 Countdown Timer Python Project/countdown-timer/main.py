
from tkinter import Tk, Label, Entry, Button
import time

def start_timer():
    """Start the countdown timer."""
    try:
        # Get the user input in seconds
        total_seconds = int(entry.get())
        while total_seconds >= 0:
            # Calculate minutes and seconds
            minutes, seconds = divmod(total_seconds, 60)
            time_display = f"{minutes:02}:{seconds:02}"
            label.config(text=time_display)  # Update the label with the time
            root.update()  # Refresh the GUI
            time.sleep(1)  # Wait for 1 second
            total_seconds -= 1
        label.config(text="Time's up!")  # Display when the timer ends
    except ValueError:
        label.config(text="Invalid input! Enter a number.")

# Create the main Tkinter window
root = Tk()
root.title("Countdown Timer")

# Create and place widgets
label = Label(root, text="00:00", font=("Helvetica", 48))
label.pack(pady=20)

entry = Entry(root, font=("Helvetica", 24), justify="center")
entry.pack(pady=10)
entry.insert(0, "Enter seconds")

start_button = Button(root, text="Start Timer", command=start_timer, font=("Helvetica", 16))
start_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
