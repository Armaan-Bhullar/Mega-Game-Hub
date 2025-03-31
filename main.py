import tkinter as tk
import random
import os
import Snake_Water_Gun
import Perfect_Guess

root = tk.Tk()
root.title("Mega Game Hub")
root.geometry("400x500")
root.config(bg="dark blue")

Welcome_text = tk.Label(root,text="Welcome to the Armaan's",bg="dark blue",fg="green",font=("Arial Black",18))
Welcome_text.pack(pady=5)

Welcome_text_Continuation = tk.Label(root,text="Mega Game Hub",bg="dark blue",fg="green",font=("Arial Black",18))
Welcome_text_Continuation.pack(pady=5)

Select_Game = tk.Label(root,text=" Which Game would you like \n to play?",bg="black",fg="yellow",font=("Arial Black",18))
Select_Game.pack(pady=10)

perfectguess_button = tk.Button(root,text="Perfect Guess",bg="light blue",fg="black",font=("Arial Black",14),command=lambda:Perfect_Guess.Perfect_Guess())
perfectguess_button.pack(pady=20)

SnakeGame_button = tk.Button(root,text="Snake_Water_Gun",bg="cyan",fg="black",font=("Arial Black",14),command=lambda:Snake_Water_Gun.Snake_Water_Gun())
SnakeGame_button.pack(pady=20)

root.mainloop()


    



