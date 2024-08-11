import tkinter as tk
from tkinter import Scrollbar, Frame, Text, Button, Entry, Menu

class ChatApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat-X")
        self.root.maxsize(1550, 900)

        # Create a frame for the chat interface
        self.chat_frame = Frame(self.root, bg="white")
        self.chat_frame.pack(fill="both", expand=True)

        # Create a text widget for the chat messages
        self.chat_text = Text(self.chat_frame, width=60, height=20, bg="white", fg="black")
        self.chat_text.pack(side="left", fill="both", expand=True)

        # Create a scrollbar for the text widget
        self.chat_scrollbar = Scrollbar(self.chat_frame)
        self.chat_scrollbar.pack(side="right", fill="y")
        self.chat_text.config(yscrollcommand=self.chat_scrollbar.set)
        self.chat_scrollbar.config(command=self.chat_text.yview)

        # Create a frame for the input field
        self.input_frame = Frame(self.root, bg="white")
        self.input_frame.pack(fill="x")

        # Create an entry field for the user to type messages
        self.input_field = Entry(self.input_frame, width=40)
        self.input_field.pack(side="left", fill="x", padx=5, pady=5)

        # Create a send button
        self.send_button = Button(self.input_frame, text="Send", command=self.send_message)
        self.send_button.pack(side="right", padx=5, pady=5)

        # Bind the Enter key to the send_message method
        self.input_field.bind("<Return>", lambda event: self.send_message())

        # Add menu-bar below title
        self.filemenu = Menu(self.root)
        self.f1 = Menu(self.filemenu, tearoff=0)
        self.f1.add_radiobutton(label="BG-Color", command=self.bgcolor)
        self.filemenu.add_cascade(label="Themes", menu=self.f1)
        self.root.config(menu=self.filemenu)

        # Create a new window
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Chat-X - New Window")

        # Create a text widget for the new window
        self.new_text = Text(self.new_window, width=60, height=20, bg="white", fg="black")
        self.new_text.pack(fill="both", expand=True)

        # Create a frame for the input field
        self.new_input_frame = Frame(self.new_window, bg="white")
        self.new_input_frame.pack(fill="x")

        # Create an entry field for the new window
        self.new_input_field = Entry(self.new_input_frame, width=40)
        self.new_input_field.pack(side="left", fill="x", padx=5, pady=5)

        # Create a send button for the new window
        self.new_send_button = Button(self.new_input_frame, text="Send", command=self.send_message_new_window)
        self.new_send_button.pack(side="right", padx=5, pady=5)

        # Bind the Enter key to the send_message_new_window method
        self.new_input_field.bind("<Return>", lambda event: self.send_message_new_window())
    def send_message(self):
        message = self.input_field.get()
        self.input_field.delete(0, tk.END)
        self.chat_text.tag_config('sender', background="black", foreground="white", justify="right")
        self.chat_text.insert(tk.END, "You: " + message + "\n", 'sender')
        self.new_text.tag_config('receiver', background="white", foreground="black", justify="left")
        self.new_text.insert(tk.END, "Receiver: " + message + "\n", 'receiver')

    def send_message_new_window(self):
        message = self.new_input_field.get()
        self.new_input_field.delete(0, tk.END)
        self.new_text.tag_config('sender', background="black", foreground="white", justify="right")
        self.new_text.insert(tk.END, "You: " + message + "\n", 'sender')
        self.chat_text.tag_config('receiver', background="white", foreground="black", justify="left")
        self.chat_text.insert(tk.END, "Receiver: " + message + "\n", 'receiver')

    def bgcolor(self):
        print("hello")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApplication(root)
    root.mainloop()