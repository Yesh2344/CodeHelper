# main.py
import tkinter as tk
from tkinter import scrolledtext
from single import Logger

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Logger UI")

        # Create the logger instance
        self.logger = Logger("app.log")

        # Create a frame for the log input
        input_frame = tk.Frame(root)
        input_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        # Entry widget for message input
        self.entry = tk.Entry(input_frame, width=50)
        self.entry.pack(side=tk.LEFT, padx=(0,10))
        self.entry.bind("<Return>", self.log_message)

        # Button to log the message
        self.log_button = tk.Button(input_frame, text="Log Message", command=self.log_message)
        self.log_button.pack(side=tk.LEFT)

        # Scrolled text widget for displaying logs
        self.log_display = scrolledtext.ScrolledText(root, state='disabled', width=80, height=20)
        self.log_display.pack(padx=10, pady=10)

        # Button to refresh the log display
        self.refresh_button = tk.Button(root, text="Refresh Log", command=self.refresh_log)
        self.refresh_button.pack(pady=(0,10))

        # Load initial log file contents
        self.refresh_log()

    def log_message(self, event=None):
        message = self.entry.get().strip()
        if message:
            # Log the message using the logger
            self.logger.log(message)
            # Clear the entry field
            self.entry.delete(0, tk.END)
            # Refresh the log display
            self.refresh_log()

    def refresh_log(self):
        try:
            with open(self.logger.log_file, "r") as f:
                contents = f.read()
            self.log_display.config(state='normal')
            self.log_display.delete(1.0, tk.END)
            self.log_display.insert(tk.END, contents)
            self.log_display.config(state='disabled')
        except Exception as e:
            print("Error reading log file:", e)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
