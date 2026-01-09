import tkinter as tk
from tkinter import scrolledtext
import json
import random

# Load questions and answers from JSON
with open("questions.json", "r") as file:
    questions_data = json.load(file)

# Function to get answer based on user input
def get_answer(user_msg):
    user_msg = user_msg.lower()
    for item in questions_data:
        if item["question"].lower() == user_msg:
            return random.choice(item["answers"])
    return "Keep going! Stay motivated!"

# Function to handle sending messages
def send_message(event=None):
    user_msg = user_input.get()
    if not user_msg.strip():
        return
    chat_area.config(state='normal')
    chat_area.insert(tk.END, f"You: {user_msg}\n")
    if user_msg.lower() == "bye":
        chat_area.insert(tk.END, "Motivational Chatbot: Bye! Stay motivated!\n")
        chat_area.config(state='disabled')
        window.after(1000, window.destroy)
    else:
        bot_reply = get_answer(user_msg)
        chat_area.insert(tk.END, f"Motivational Chatbot: {bot_reply}\n\n")
    chat_area.config(state='disabled')
    chat_area.yview(tk.END)
    user_input.delete(0, tk.END)

# GUI setup
window = tk.Tk()
window.title("Motivational Chatbot ")
window.geometry("500x500")

chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, state='disabled')
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

user_input = tk.Entry(window, font=("Arial", 14))
user_input.pack(padx=10, pady=10, fill=tk.X)
user_input.bind("<Return>", send_message)

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(padx=10, pady=5)

# Welcome message
chat_area.config(state='normal')
chat_area.insert(tk.END, "🤖 Motivational Chatbot: Hi! I'm here to motivate you. Type 'bye' to exit.\n")
chat_area.insert(tk.END, "✨ Motivational Chatbot ✨\n\n")
chat_area.config(state='disabled')

window.mainloop()
