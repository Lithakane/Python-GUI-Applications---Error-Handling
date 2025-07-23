import tkinter as tk
from tkinter import messagebox
from CheckingLog import QualificationChecker


class LoginSystem:
    """GUI application for user authentication."""

    VALID_CREDENTIALS = {
        "litha": "0000",
        "mawande": "1234",
        "odwa": "4321"
    }

    def __init__(self, master):
        self.master = master
        self.master.title("LOGIN PAGE")
        self.master.geometry("400x200")
        self.master.config(background='#7F6A7F')

        self.setup_ui()

    def setup_ui(self):
        """Initialize all UI components."""
        # Username field
        tk.Label(
            self.master,
            text="Username",
            background='#7F6A7F'
        ).pack(pady=5)

        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack(pady=5)

        # Password field
        tk.Label(
            self.master,
            text="Password",
            background='#7F6A7F'
        ).pack(pady=5)

        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack(pady=5)

        # Login button
        tk.Button(
            self.master,
            text="Login",
            bg="#f9bbf9",
            command=self.authenticate
        ).pack(pady=10)

    def authenticate(self):
        """Verify user credentials."""
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.VALID_CREDENTIALS.get(username) == password:
            messagebox.showinfo("Success", "Login successful!")
            self.master.withdraw()
            self.open_qualification_checker()
        else:
            messagebox.showerror("Error", "Invalid username or password")
            self.clear_entries()

    def open_qualification_checker(self):
        """Open the qualification checker window."""
        checker_window = tk.Toplevel()
        QualificationChecker(checker_window)

    def clear_entries(self):
        """Clear login fields."""
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginSystem(root)
    root.mainloop()
# This code implements a simple login system using Tkinter.
# It allows users to enter their username and password, checks the credentials against a predefined set,
# and opens a qualification checker window if the login is successful.
# If the login fails, it shows an error message and clears the input fields.
# The qualification checker is a separate class that checks if the user qualifies for a trip based on their account balance.
# The application uses a dictionary to store valid usernames and passwords for authentication.
# The GUI is styled with a consistent background color and button styles.
# The login system is designed to be user-friendly and provides feedback for both successful and failed login attempts.
# The application is structured to separate concerns, with the login logic and qualification checking handled in different classes.
# This modular approach makes the code easier to maintain and extend in the future.
# The main function initializes the application window and starts the event loop.
# The code is ready to be run as a standalone application, providing a basic user authentication system
# and a subsequent qualification checking feature.
# The login system can be easily modified to include more users or different authentication methods in the future.
# The use of message boxes for feedback enhances user experience by providing clear and immediate responses to user actions.
# The application is designed to be intuitive, guiding users through the login process and subsequent qualification
