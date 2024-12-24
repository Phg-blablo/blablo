import tkinter as tk
from tkinter import messagebox
import datetime

# Function to calculate and update the countdown
def update_countdown():
    try:
        target_date = datetime.datetime.strptime(entry_date.get(), "%Y-%m-%d").date()
        today = datetime.date.today()
        delta = target_date - today

        if delta.days > 0:
            label_countdown.config(text=f"{delta.days} days left until {target_date}.")
        elif delta.days == 0:
            label_countdown.config(text="Today is the day!")
        else:
            label_countdown.config(text=f"{-delta.days} days have passed since {target_date}.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid date in YYYY-MM-DD format.")

# Create the main window
root = tk.Tk()
root.title("Countdown Clock")

# Input label and entry for the target date
label_prompt = tk.Label(root, text="Enter the target date (YYYY-MM-DD):")
label_prompt.pack(pady=5)

entry_date = tk.Entry(root, width=20)
entry_date.pack(pady=5)

# Button to trigger the countdown calculation
button_calculate = tk.Button(root, text="Calculate Countdown", command=update_countdown)
button_calculate.pack(pady=10)

# Label to display the countdown result
label_countdown = tk.Label(root, text="", font=("Helvetica", 14))
label_countdown.pack(pady=20)

# Start the main event loop
root.mainloop()
