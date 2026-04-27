# 🚀 Real-Time Chat Application using Python Socket Programming

A **real-time chat application** developed using **Python Socket Programming**, allowing multiple clients to communicate through a **cloud-hosted server on Microsoft Azure**.

This project demonstrates practical implementation of **client–server architecture, multithreading, GUI development, and network communication**.

---

## 🔥 Key Features
- 💬 Real-time messaging between multiple clients  
- 👥 Multi-client support using threading  
- 🖥️ User-friendly **Tkinter GUI**  
- 🌐 Cloud-hosted server (Azure VM)  
- 📡 Broadcast messages to all connected clients  
- ⚠️ Handles disconnections and basic errors  

---

## 🛠️ Technologies Used
- Python  
- Socket Programming (TCP)  
- Tkinter (GUI)  
- Threading  
- Microsoft Azure (Cloud VM)  
- Wireshark (Network Analysis)  
- GitHub (Version Control)  

---

## 🌐 System Architecture

### 🔹 Server
- Hosted on Azure Virtual Machine  
- IP Address: `20.2.140.93`  
- Port: `5000`  
- Handles multiple clients using threads  
- Broadcasts messages to all connected clients  

### 🔹 Client
- Runs on local machines  
- Built with **Tkinter GUI**  
- Connects using Server IP and Port  
- Sends and receives messages in real time  

---

## ▶️ How to Run the Application (Step-by-Step)

### 🔹 Step 1: Start the Server (Azure VM)
Open terminal in your Azure VM and run:

```bash
python server.py
```
✔ Server will start and listen on Port 5000

### 🔹 Step 2: Run the Client (Local Machine)
Run the client application:

```bash
python client.py
```
✔ A GUI window will open

### 🔹 Step 3: Connect to Server
In the client GUI:

- Enter Server IP → 20.2.140.93
- Enter Port → 5000
- Click Connect

### 🔹 Step 4:  Start Chatting
- Open multiple clients (same PC or different PCs)
- Send messages
- Messages will be broadcast to all connected clients 💬

  ---

  ## 👥 Group Members
- W.N. Kasuni  
- H.G.T. Yashoda  
- N.G.T. Imansa  
- M.N. Hamna

  ---

## 📚 Learning Outcomes
- Understanding of socket programming  
- Hands-on experience with client–server communication  
- Implementation of multithreading  
- Experience with cloud deployment (Azure)  
- Basic packet analysis using Wireshark  
  
