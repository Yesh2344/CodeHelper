# Code Helper with UI

This project demonstrates the Singleton design pattern using a simple Logger utility in Python—now with a graphical user interface (GUI) built with Tkinter.

## Project Structure

- **single.py**: Contains the Singleton metaclass and the Logger class.
- **main.py**: Contains the Tkinter-based UI that lets you log messages and view log file contents.
- **README.md**: Project description and instructions.

## How to Run

1. **Ensure Python is Installed:**  
   Make sure you have Python 3.6 or higher installed.

2. **Navigate to the Project Directory:**  
   Open a terminal or command prompt and change the directory to where your project files are located:
   ```bash
   cd path/to/code_helper
   ```
3. Run the Application:
   Execute the main file using Python:
   ```bash
   python main.py
   ```
4. Using the UI:

 - Type a log message into the input field.
 - Press Enter or click the Log Message button.
 - The message will be logged to app.log and displayed in the text area.
 - Click Refresh Log to update the displayed log contents.


---

### How It Works

- **Logger (Singleton):**  
  The `Logger` class in `single.py` ensures only one instance exists, so every log entry (whether from the command line or the UI) goes to the same file (`app.log`).

- **User Interface (UI):**  
  The Tkinter-based UI in `main.py` provides an input field for messages and a scrollable area that displays the contents of the log file. This makes it easier for software engineers to interactively log messages and verify log output.

Now you have a project that not only demonstrates the Singleton pattern for logging but also provides a simple UI to interact with it. Enjoy experimenting with and expanding this project to fit your needs!

Email:

