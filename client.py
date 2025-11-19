import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

class ChatClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Messenger")
        self.root.geometry("500x550")
        self.root.resizable(False, False)

        self.client_socket = None
        self.connected = False

        self.build_gui()

    def build_gui(self):
        
        title = tk.Label(self.root, text="Socket Messenger",
                         font=("Arial", 16, "bold"))
        title.pack(pady=10)

        
        frame_conn = tk.Frame(self.root)
        frame_conn.pack()

        tk.Label(frame_conn, text="Server IP:").grid(row=0, column=0)
        self.ip_entry = tk.Entry(frame_conn, width=18)
        self.ip_entry.grid(row=0, column=1)
        self.ip_entry.insert(0, "YOUR_AZURE_VM_PUBLIC_IP")

        tk.Label(frame_conn, text="Port:").grid(row=0, column=2)
        self.port_entry = tk.Entry(frame_conn, width=10)
        self.port_entry.grid(row=0, column=3)
        self.port_entry.insert(0, "5000")

        self.connect_btn = tk.Button(frame_conn, text="Connect",
                                     command=self.connect_to_server,
                                     bg="#4CAF50", fg="white",
                                     width=10)
        self.connect_btn.grid(row=0, column=4, padx=5)

        self.chat_window = scrolledtext.ScrolledText(self.root,
                                                     width=60,
                                                     height=20,
                                                     state="disabled",
                                                     font=("Arial", 10))
        self.chat_window.pack(pady=10)

        frame_msg = tk.Frame(self.root)
        frame_msg.pack()

        self.msg_entry = tk.Entry(frame_msg, width=40, font=("Arial", 12))
        self.msg_entry.grid(row=0, column=0, padx=5)
        self.msg_entry.bind("<Return>", lambda event: self.send_message())

        send_btn = tk.Button(frame_msg, text="Send",
                             command=self.send_message,
                             bg="#2196F3", fg="white",
                             width=10)
        send_btn.grid(row=0, column=1)

        
    def connect_to_server(self):
        if self.connected:
            messagebox.showinfo("Already Connected", "You are already connected!")
            return

        ip = self.ip_entry.get()
        port = int(self.port_entry.get())

        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((ip, port))
            self.connected = True

            self.chat_window.config(state="normal")
            self.chat_window.insert(tk.END, f"[Connected to {ip}:{port}]\n")
            self.chat_window.config(state="disabled")

            self.connect_btn.config(text="Connected", bg="gray")

            threading.Thread(target=self.receive_messages,
                             daemon=True).start()

        except Exception as e:
            messagebox.showerror("Connection Error", str(e))

    def receive_messages(self):
        while True:
            try:
                msg = self.client_socket.recv(1024).decode()
                if not msg:
                    break

                self.chat_window.config(state="normal")
                self.chat_window.insert(tk.END, msg + "\n")
                self.chat_window.see(tk.END)
                self.chat_window.config(state="disabled")

            except:
                break

    def send_message(self):
        if not self.connected:
            messagebox.showwarning("Not Connected", "Connect to a server first!")
            return

        msg = self.msg_entry.get().strip()
        if msg == "":
            return

        try:
            self.client_socket.send(msg.encode())
            self.msg_entry.delete(0, tk.END)
        except:
            messagebox.showerror("Error", "Failed to send message.")
   
root = tk.Tk()
app = ChatClient(root)
root.mainloop()