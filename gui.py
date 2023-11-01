import tkinter as tk
import datetime as dt


class App(tk.Frame):
    def __init__(self, window=None):
        # Inheriting, and initiating the Frame, using a standard font and pad.
        super().__init__(window)
        self.window = window
        self.grid(column=0, row=0, sticky=("nwes"))
        self.font = 'Arial 17 bold'
        self.pad = 10
        self.geometry = "800x600"
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.final_time = ""

# Stopwatch class for keeping track of hours worked
class Stopwatch:
    
    def __init__(self):

        # Initiating with the buttons, each assigned a text, position, and function upon click.
        self.start_button = tk.Button(root, text="Start", command=on_click).grid(column=0, row=1, padx=app.pad, pady=app.pad)
        self.pause_button = tk.Button(root, text="Reset", command= self.reset).grid(column=1, row=1, padx=app.pad, pady=app.pad)
        self.stop_button = tk.Button(root, text="Stop", command= self.stop).grid(column=2, row=1, padx=app.pad, pady=app.pad) 
        self.running = False

        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.new_time = ""
        self.worked = tk.Label(root, font=app.font, text="")
        self.worked.grid(column=2, row=0, pady=app.pad, padx=app.pad)
    # Start the watch from 00:00:00, and initiate the time_spent method.
    def start(self):
        if not self.running:
            self.worked.after(1000)
            self.time_spent()
            self.running = True

    # Stop the watch at whatever time it is currently on, continuing to display that time.
    def stop(self):
        if self.running:
            self.worked.after_cancel(self.new_time)
            self.running = False

    # Passes the time recorded to TimeRecorder then resets the timer to 00:00:00 and the seconds, minutes, and hours variables to 0
    def reset(self):
        # Passes on data
        pass
        # Resets timer and variables.
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.worked.config(text="Time worked: 00:00:00")
        print(self.final_time)

    # Keeps track of time since start and displays it.
    # Struggling to make it work without crashing.
    def time_spent(self):
        self.seconds += 1
        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0
        if self.minutes == 60:
            self.hours += 1
            self.minutes = 0
       

        total_hours_string = f"{self.hours}" if self.hours > 9 else f"0{self.hours}"
        total_minutes_string = f"{self.minutes}" if self.minutes > 9 else f"0{self.minutes}"
        total_seconds_string = f"{self.seconds}" if self.seconds > 9 else f"0{self.seconds}"
        total_time_string = f"Time worked: {total_hours_string}:{total_minutes_string}:{total_seconds_string}"
        self.final_time = f"{total_hours_string}:{total_minutes_string}:{total_seconds_string}"

        self.worked.config(text=total_time_string)
        self.new_time = self.worked.after(1000, self.time_spent)

# Clock class which will display both the current time and the time when the shift started.
class Clock:
    def __init__(self):
        self.now = tk.Label(root, font=app.font, text="") # Place holder for the current time which will be shown by the curr_time method.
        self.now.grid(column=1, row=0, padx=app.pad, pady=app.pad)

        self.start_time = tk.Label(root, font=app.font, text="") # Place holder for start time which will be saved when start is pressed.
        self.start_time.grid(column=0, row=0, padx=app.pad, pady=app.pad)
        self.curr_time()

    # Saves and displays the current time in real time. Called in initiation.
    def curr_time(self):
        time = dt.datetime.strftime(dt.datetime.now(), "%H:%M:%S, %d/%m/%Y")
        self.now.config(text=time)
        self.now.after(1000, self.curr_time)
    # Saves and displays the time when "Start" was pressed.
    def save_time(self):
        time = dt.datetime.strftime(dt.datetime.now(), "%H:%M:%S, %d/%m/%Y") 
        self.start_time.config(text=f"Start time: {time}")
    # Resets the save_time to 0, will be called when the "Reset" button is pressed.
    def reset(self):
        pass

    
# Start stopwatch and save start time.
def on_click():
    clock.save_time()
    watch.start()    # Currently causing crashes.

# Main loop.
root = tk.Tk()
root.title = "Timekeeper"
app = App(window=root)

# Window created]
clock = Clock()
watch = Stopwatch()

# Watch and Clock initiated

app.mainloop()




