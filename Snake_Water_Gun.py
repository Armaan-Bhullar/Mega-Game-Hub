import tkinter as tk
import random

# Function to determine the winner
def Snake_Water_Gun():
    def play_game(user_choice):
        choices = ["Snake", "Water", "Gun"]
        computer_choice = random.choice(choices)
        result = ""

        if user_choice == computer_choice:
            result = "It's a Tie!"
            result_label.config(fg="Yellow")
        elif (user_choice == "Snake" and computer_choice == "Water") or \
            (user_choice == "Water" and computer_choice == "Gun") or \
            (user_choice == "Gun" and computer_choice == "Snake"):
            result = "You Win!"
            result_label.config(fg="Green")
        else:
            result = "Computer Wins!"
            result_label.config(fg="Red")

        # Update the labels with the choices and result
        user_choice_label.config(text=f"You chose: {user_choice}")
        computer_choice_label.config(text=f"Computer chose: {computer_choice}")
        result_label.config(text=result)

    # Create main window
    root = tk.Tk()
    root.title("Snake Water Gun Game")
    root.geometry("800x600")
    root.config(bg="black")

    # Title Label
    title_label = tk.Label(root, text="Snake Water Gun Game", font=("Arial Black", 36), bg="black", fg="yellow")
    title_label.pack(pady=20)

    # Labels to show choices
    user_choice_label = tk.Label(root, text="Your Choice: ", font=("Arial Black", 28,"bold"), bg="black",fg="white")
    user_choice_label.pack(pady=10)

    computer_choice_label = tk.Label(root, text="Computer's Choice: ", font=("Arial Black", 28,"bold"), bg="black",fg="white")
    computer_choice_label.pack(pady=10)

    # Result Label
    result_label = tk.Label(root, text="", font=("Arial Black", 32, "bold"), bg="black", fg="green")
    result_label.pack(pady=20)

    # Buttons for user to make a choice
    button_frame = tk.Frame(root, bg="lightblue")
    button_frame.pack(pady=20)

    snake_button = tk.Button(button_frame, text="Snake", font=("Arial", 24), bg="yellow", fg="black", width=10,
                            command=lambda:play_game("Snake"))
    snake_button.grid(row=0, column=0, padx=10)

    water_button = tk.Button(button_frame, text="Water", font=("Arial", 24), bg="cyan", fg="black", width=10,
                            command=lambda:play_game("Water"))
    water_button.grid(row=0, column=1,padx=10)

    gun_button = tk.Button(button_frame, text="Gun", font=("Arial", 24), bg="orange", fg="black", width=10,
                        command=lambda:play_game("Gun"))
    gun_button.grid(row=0, column=2, padx=10)

    # Run the application
    root.mainloop()
