import datetime as dt
import tkinter as tk
import os

from DataGatherer import Gatherer


class App(tk.Frame):
    def __init__(self, window=None):
        # Inheriting, and initiating the Frame, using a standard font and pad.
        super().__init__(window)
        self.window = window
        self.grid(column=0, row=0, sticky="nwes")
        self.font = 'Arial 17 bold'
        self.pad = 10
        self.geometry = "800x600"
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


# Stopwatch class for keeping track of hours worked
class Stopwatch:
    def __init__(self):
        # Initiating with the buttons, each assigned a text, position, and function upon click.
        self.start_button = tk.Button(root, text="Start", command=on_click).grid(column=0, row=1, padx=app.pad,
                                                                                 pady=app.pad)
        self.reset_button = tk.Button(root, text="Reset", command=self.reset).grid(column=1, row=1, padx=app.pad,
                                                                                   pady=app.pad)
        self.stop_button = tk.Button(root, text="Stop", command=self.stop).grid(column=2, row=1, padx=app.pad,
                                                                                pady=app.pad)
        self.running = False

        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.new_time = ""
        self.worked = tk.Label(root, font=app.font, text="")
        self.worked.grid(column=2, row=0, pady=app.pad, padx=app.pad)
        self.final_time = ""

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

    # Passes the time recorded to TimeRecorder then resets the timer to 00:00:00 and the seconds, minutes,
    # and hours variables to 0
    def reset(self):
        # Passes on data

        err_msg = tk.Label(text="", font=app.font,
                           padx=app.pad, pady=app.pad)

        # Error message not disappearing after correct reset, unsure why.
        try:
            labeler.project_select()
            print(f"{labeler.selected_variable} is selected")
            datagatherer.recieve(dt.datetime.strftime(dt.datetime.now(), "%H:%M:%S, %d/%m/%Y"), self.final_time,
                                 labeler.selected_variable)  # Temporary string placeholder for test.
            datagatherer.split_datetime()

            datagatherer.write()
            # Resets timer and variables.
            self.seconds = 0
            self.minutes = 0
            self.hours = 0
            self.final_time = 0
            self.worked.config(text="Time worked: 00:00:00")

            # Should reset err_msg but doesn't.
            err_msg.config(text="")
        except PermissionError:
            err_msg.config(text="Make sure the excel file is closed before resetting.")
            err_msg.grid(column=2, row=5)

    # Keeps track of time since start and displays it.
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
        self.now = tk.Label(root, font=app.font,
                            text="")  # placeholder for the current time which will be shown by the curr_time method.
        self.now.grid(column=1, row=0, padx=app.pad, pady=app.pad)

        self.start_time = tk.Label(root, font=app.font,
                                   text="")  # placeholder for start time which will be saved when start is pressed.
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


class Labeler:
    def __init__(self):
        self.selected_variable = None
        self.project_file_name = "Projects.txt"
        self.lbl = tk.Label(text="Label", font=app.font, padx=app.pad, pady=app.pad)
        self.lbl.grid(column=1, row=4)

        self.entry = tk.Entry()
        self.entry.grid(column=2, row=4)

        self.add_button = tk.Button(text="Add Project", font=app.font, padx=app.pad, pady=app.pad,
                                    command=self.add_project)
        self.add_button.grid(column=3, row=4)

        self.remove_button = tk.Button(text="Remove", font=app.font, padx=app.pad, pady=app.pad,
                                       command=self.finish_project)
        self.remove_button.grid(column=3, row=5)

        self.clear_button = tk.Button(text="Clear", font=app.font, padx=app.pad, pady=app.pad, command=self.clear_lst)
        self.clear_button.grid(column=3, row=6)

        if os.path.isfile(self.project_file_name):
            with open(self.project_file_name, "r") as file:
                self.project_list = file.readlines()
        else:
            with open(self.project_file_name, "w") as file:
                pass
            self.project_list = []

        # Label list needs to populate from file project_list
        self.project_list_boxes = []
        if self.project_list is not None:
            if "\\n" in self.project_list:
                for p in self.project_list:
                    if p == "\\n":
                        self.project_list.remove(p)
            try:
                self.check_vars = {}
                print("Variables created")
                for p in self.project_list:
                    self.check_vars[p] = tk.StringVar()
                    print(f" Project from var dict: {self.check_vars[p]}")
                    print(self.check_vars)
                    c = tk.Checkbutton(text=p, font=app.font, pady=app.pad, padx=app.pad, variable=self.check_vars[p],
                                       onvalue="selected", offvalue="unselected")
                    self.project_list_boxes.append(c)
            except TypeError:
                print(type(self.project_list))

        # Calling display method to show any pre-existing projects.
        self.display()

    # Adds a project to a list including a tick box next to it in order to select labels for data.
    def add_project(self):
        name = self.entry.get()
        if not name:
            err_msg = tk.Label(text="Please enter a name for you project", font=app.font, padx=app.pad, pady=app.pad)
            err_msg.grid(column=1, row=4)
            print("No name entered.")
        else:
            # Add labels with tick boxes for project selection.
            if name in self.project_list:
                err_msg = tk.Label(text="There is already a project with that name.")
                print("Name is in project list.")
            # Label list needs to populate from file.
            else:
                self.check_vars[name] = tk.StringVar()
                self.project_list.append(name)
                self.project_list_boxes.append(
                    tk.Checkbutton(text=name, font=app.font, padx=app.pad, pady=app.pad, variable=self.check_vars[name],
                                   onvalue="selected", offvalue="unselected"))
                print("Project added.")
                with open(self.project_file_name, "r+") as file:
                    file.write(f"{name}\n")
        self.display()

    # Remove projects from the tickbox file.
    def finish_project(self):
        keys = list(self.check_vars.keys())
        values = [v if isinstance(v, str) else v.get() for v in self.check_vars.values()]
        print(f"Keys: {keys}")
        print(f"Values: {values}")

        for v in values:
            if v == "selected":
                i = values.index(v)
                self.project_list.remove(keys[i])
                del values[i]
                del keys[i]
                del self.project_list_boxes[i]
                self.check_vars = dict(zip(keys, values))

        with open(self.project_file_name, "w") as file:
            for p in self.project_list:
                file.write(f"{p}\n")

        self.display()

    def clear_lst(self):
        self.project_list = []
        self.project_list_boxes = []
        with open(self.project_file_name, "w") as file:
            pass

    def display(self):
        if self.project_list_boxes is not None:
            for project in self.project_list_boxes:
                project.grid(column=2, row=(self.project_list_boxes.index(project) + 5))

    # For some reason the selected variable is not changing - unsure whether the below function is being called
    # properly.
    def project_select(self):
        for p in self.check_vars:
            if self.check_vars[p].get() == "selected":
                self.selected_variable = p
                print(f"{self.check_vars[p]} is selected in project select")

    def change_variable(self, dict_key, value):
        self.check_vars[dict_key] = value


# Start stopwatch and save start time.
def on_click():
    clock.save_time()
    watch.start()


# Main loop.
root = tk.Tk()
root.title = "Timekeeper"
app = App(window=root)

# Object that takes data from the program and writes it to Excel.
datagatherer = Gatherer()


clock = Clock()
watch = Stopwatch()
labeler = Labeler()


app.mainloop()
