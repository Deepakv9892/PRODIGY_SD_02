import tkinter as tk
from tkinter import messagebox
import random

secret_number = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts
    try:
        guess = int(entry_guess.get())
        attempts += 1

        if guess < secret_number:
            label_feedback.config(text="Too low! Try again.")
        elif guess > secret_number:
            label_feedback.config(text="Too high! Try again.")
        else:
            messagebox.showinfo("Correct!", f"Congratulations! You guessed it in {attempts} attempts.")
            reset_game()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def reset_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    entry_guess.delete(0, tk.END)
    label_feedback.config(text="")

app = tk.Tk()
app.title("Guess the Number Game")
app.geometry("400x300")
app.config(padx=20, pady=20)

tk.Label(app, text="🎯 Guess the Number!", font=("Arial", 18, "bold")).pack(pady=10)
tk.Label(app, text="Guess a number between 1 and 100").pack()

entry_guess = tk.Entry(app, font=("Arial", 14), width=10)
entry_guess.pack(pady=10)

tk.Button(app, text="Submit Guess", command=check_guess, bg="green", fg="white", font=("Arial", 12)).pack(pady=5)

label_feedback = tk.Label(app, text="", font=("Arial", 14), fg="blue")
label_feedback.pack(pady=10)

app.mainloop()
