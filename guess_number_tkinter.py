import tkinter as tk
from random import randint

window = tk.Tk()
window.title("Guess Number Game")
window.geometry('700x500')
window.resizable(False, False)

#random number between 1 and 100
target = randint(1, 100)

def check_number():
    """getting guessing number of user and checking it"""
    result = entry.get()

    try:
        number = int(result)

        if (number>100) or (number<1):
            message.config(text="Please just enter number between 1 and 100!", fg='red')
            message.place(x=150, y=100)
            window.after(3000, message.place_forget)

        elif number < target:
            message.config(text="⬇️ Too low. Guess again.", fg='orange')
            message.place(x=210, y=95)
            window.after(3000, message.place_forget)

        elif number > target:
            message.config(text="⬆️ Too high. Guess again.", fg='orange')
            message.place(x=210, y=95)
            window.after(3000, message.place_forget)
        
        else:
            message.config(text=f"\n🎉 {number} is correct! You got it!", fg='green')
            message.place(x=210, y=95)
            window.after(5000, message.place_forget)

            #change botton1 to continue program
            button1.config(text="Replay", command=continue_program)
    
    except ValueError:
        message.config(text="🔢Please just enter valid number!", fg='red')
        message.place(x=210, y=95)
        window.after(3000, message.place_forget)

def continue_program():
    """Reset game with new number"""
    global target
    target = randint(1, 100)

    #reset button
    button1.config(text="Send", command=check_number)

    #clear entry and message
    entry.delete(0, tk.END)
    message.place_forget()

def quit_program():
    """quit the program"""
    window.destroy()

#create first label
label1 = tk.Label(window, 
    text="🤔 I'm thinking of a number between 1 and 100. Try to guess number.\n I'm thinking of: ", 
    font=('Arial', 15))
label1.pack()

#create entery for getting guessing number of user
entry = tk.Entry(window, width=5, font=('Arial', 15))
entry.pack(pady=10)
entry.focus()

#create second label for send message for user
message = tk.Label(window, font=('Arial', 15))   #at first it doesn't have any text for send message

#create button for send guessing number
button1 = tk.Button(window, text='Send',font=('Arial', 15), command=check_number)
button1.pack(pady=60)

#create button to quit of program
button2 = tk.Button(window, text='Quit', font=('Arial', 15), bg='red', command=quit_program)
button2.pack(pady=100)

window.mainloop()
    