import tkinter as tk
from tkinter import messagebox


class QualificationChecker:
    """GUI application to check trip qualification based on account balance."""

    MINIMUM_BALANCE = 3000

    def __init__(self, master):
        self.master = master
        self.master.title('ERROR CHECKS')
        self.master.geometry('400x200')
        self.master.config(background='#7F6A7F')

        self.setup_ui()

    def setup_ui(self):
        """Initialize all UI components."""
        tk.Label(
            self.master,
            text="Please enter amount in your account",
            bg='#7F6A7F'
        ).pack(pady=10)

        self.balance_entry = tk.Entry(self.master)
        self.balance_entry.pack(pady=5)

        tk.Button(
            self.master,
            text="Check qualification",
            bg="magenta",
            command=self.check_qualification
        ).pack(pady=10)

    def check_qualification(self):
        """Validate input and check if user qualifies for the trip."""
        try:
            balance = float(self.balance_entry.get())

            if balance >= self.MINIMUM_BALANCE:
                message = "You qualify for the Malaysia trip. Congratulations!"
            else:
                needed = self.MINIMUM_BALANCE - balance
                message = f"You need R{needed:.2f} more to qualify"

            messagebox.showinfo("Qualification Status", message)
            self.balance_entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number")
            self.balance_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = QualificationChecker(root)
    root.mainloop()
# This code defines a GUI application that checks if a user qualifies for a trip based on their account balance.
# It prompts the user to enter their balance and informs them if they qualify or how much more they need to qualify.
# The application uses tkinter for the GUI and includes error handling for invalid inputs.
# The minimum balance required to qualify for the trip is set to 3000.
# The application is designed to be user-friendly, providing clear messages and input validation.
# The main function initializes the application window and starts the event loop.
# The code is structured to be easily extendable for future features or modifications.
# The class QualificationChecker encapsulates all functionality related to checking trip qualifications.
# The setup_ui method initializes the user interface components, including labels, entry fields, and buttons.
# The check_qualification method validates the user's input and checks if they meet the qualification criteria.
# The application is ready to be run as a standalone program, providing a simple and effective way
# for users to check their trip qualification status based on their account balance.
# The code is well-commented to explain the purpose of each section and method.
# The application can be easily integrated into a larger system or used independently for trip qualification checks.
# The GUI is designed to be intuitive, with clear instructions and feedback for the user.
