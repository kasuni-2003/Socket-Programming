# 🚀 Real-Time Chat Application using Python Socket Programming

A **real-time chat application** developed using **Python Socket Programming**, enabling multiple clients to communicate through a **cloud-hosted server (Microsoft Azure)**.

This project demonstrates practical implementation of **client–server architecture, multithreading, and network communication**.

---

## 🔥 Key Features
- 💬 Real-time messaging between multiple clients  
- 👥 Multi-client support using threading  
- 🌐 Cloud-hosted server (Azure VM)  
- 🖥️ User-friendly **Tkinter GUI**  
- 📡 Broadcast messages to all connected clients  
- ⚠️ Basic error handling for stable communication  

---

## 🛠️ Technologies Used
- **Python**
- **Socket Programming (TCP)**
- **Tkinter GUI**
- **Threading**
- **Microsoft Azure (Cloud VM)**
- **Wireshark (Packet Analysis)**
- **GitHub (Version Control)**

---

## 🌐 System Architecture
- **Server**
  - Hosted on Azure VM  
  - IP: `20.2.140.93`  
  - Port: `5000`  
  - Handles multiple clients using threads  

- **Clients**
  - Run on local machines  
  - Connect using server IP & port  
  - Send and receive messages in real time  

---

## ▶️ How to Run the Application

### 1️⃣ Start the Server
```bash
python server.py
