import tkinter as tk
from random import randint

window = tk.Tk()
window.title("Guess Number Game")
window.geometry('700x500')

#random number between 1 and 100
target = randint(1, 100)

def check_number():
    """getting guessing number of user and checking it"""
    result = entry.get()

    try:
        number = int(result)

        if (number>100) or (number<1):
            label2.config(text="Please just enter number between 1 and 100!", fg='red')
            label2.pack(pady=15)

        elif number < target:
            label2.config(text="⬇️ Too low. Guess again.", fg='orange')
            label2.pack(pady=15)

        elif number > target:
            label2.config(text="⬆️ Too high. Guess again.", fg='orange')
            label2.pack(pady=15)
        
        else:
            label2.config(text=f"\n🎉 {number} is correct! You got it!", fg='green')
            label2.pack(pady=15)
    
    except ValueError:
        label2.config(text="🔢Please just enter valid number!", fg='red')
        label2.pack(pady=15)

def quit_program():
    """quit the program"""
    window.destroy()

#create first label
label1 = tk.Label(window, text="🤔 I'm thinking of a number between 1 and 100. Try to guess number.\n I'm thinking of: ", font=('Arial', 15))
label1.pack()

#create entery for getting guessing number of user
entry = tk.Entry(window, width=5, font=('Arial', 15))
entry.pack(pady=10)

#create second label for send message for user
label2 = tk.Label(window, font=('Arial', 15))   #at first it doesn't have any text for send message
label2.pack()
    
#create button for send guessing number
button1 = tk.Button(window, text='Send',font=('Arial', 15), command=check_number)
button1.pack(pady=10)

#create button to quit of program
button2 = tk.Button(window, text='Quit', font=('Arial', 15), fg='red', command=quit_program)
button2.pack(pady=100)

window.mainloop()
    