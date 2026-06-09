import tkinter as tk

def good():
    result.config(text="That's great to hear!", fg="green")

def not_at_all():
    result.config(text="Hope you feel better soon!", fg="red")

root = tk.Tk()
root.title("Question")
root.geometry("500x350")

Question = tk.Label(root, text=" How are you?", font=("Arial", 30))
Question.pack(pady=20)

but_frame = tk.Frame(root)
but_frame.pack(pady=10)

button1 = tk.Button(but_frame, text="I'm Good", font=("Arial", 12), command=good)
button2 = tk.Button(but_frame, text="Not at all", font=("Arial", 12), command=not_at_all)
button1.pack(side=tk.LEFT, padx=10)
button2.pack(side=tk.LEFT, padx=10)

result = tk.Label(root, text="", font=("Arial", 30))
result.pack(pady=30)

root.mainloop()