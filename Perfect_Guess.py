import random 
import tkinter as tk

Guesses = 1
def Perfect_Guess():
    n = random.randint(1 , 100)
    def show_input():
        a = entry.get()  # Get text from entry
        return a
        
    def Check(a):
        global Guesses  
        a = int(a)
        if a > n:   
            result = "Enter lower number Sir!"
            hint.config(text=result)
        elif a < n:
            result = "Enter higher number Sir!"
            hint.config(text=result)
        else:
            result = f"You Won!!\nYou guessed the correct number '{n}' in {Guesses} guesses."
            hint.config(text=result,fg="green")
            root.after(3000,root.destroy)
        Guesses += 1
            
    
    root = tk.Tk()
    root.title("Perfect Guessing Game")
    root.geometry("1400x500")
    root.config(bg="black")

    title_label = tk.Label(root, text="Perfect Guessing Game", font=("Arial Black", 36), bg="black", fg="white")
    title_label.pack(pady=20)

    entry_frame = tk.Frame(root, bg="lightblue")
    entry_frame.pack(pady=20)

    welcome_text = tk.Label(entry_frame,text="Enter any number from 1 - 100 please: ", font=("Arial Black", 32), bg="lightblue", fg="black")
    welcome_text.grid(row=0,column=0,padx=5)
    entry = tk.Entry(entry_frame,font=("Arial Black",32),fg="black",width=3)
    entry.grid(row=0,column=1,padx=10)

    submit_button = tk.Button(root,text="GUESS",font=("Arial Black",28),bg="black",fg="light green",command=lambda:Check(show_input()))
    submit_button.pack(pady=10)

    hint = tk.Label(root,text="",font=("Arial Black",28),bg="black",fg="red")
    hint.pack(pady=20)
    root.mainloop()

