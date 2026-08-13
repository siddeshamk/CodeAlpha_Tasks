# 🛡️ CodeAlpha - Basic Network Sniffer

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Scapy](https://img.shields.io/badge/Scapy-Network%20Analysis-green)
![Status](https://img.shields.io/badge/Project-Completed-success)

## 📌 Project Overview

This project was developed as part of the **CodeAlpha Cyber Security Internship**.

The application is a Python-based **Network Packet Sniffer** that captures live network traffic and displays useful packet information including:

- Source IP Address
- Destination IP Address
- Protocol
- Source Port
- Destination Port
- Packet Size
- Payload Preview

The captured packet details are also stored in a CSV file for later analysis.

---

# 🎯 Objectives

- Learn how network packets travel.
- Understand packet structure.
- Analyze different network protocols.
- Capture live network traffic.
- Store captured information for future analysis.

---

# 🚀 Features

✅ Live Packet Capture

✅ Source IP Detection

✅ Destination IP Detection

✅ TCP / UDP / ICMP Detection

✅ Source & Destination Ports

✅ Packet Size Information

✅ Payload Preview

✅ CSV Logging

✅ Easy to Use

---

# 🛠️ Technologies Used

- Python
- Scapy
- Colorama

---

# 📂 Project Structure

```
CodeAlpha_BasicNetworkSniffer/
│
├── network_sniffer.py
├── README.md
├── requirements.txt
├── .gitignore
├── reports/
│     └── Project_Report.md
├── screenshots/
└── captured_packets.csv
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/CodeAlpha_BasicNetworkSniffer.git
```

Move into the project directory:

```bash
cd CodeAlpha_BasicNetworkSniffer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Program

Run PowerShell as Administrator and execute:

```bash
python network_sniffer.py
```

---

# 📊 Sample Output

```
Packet Number : 100

Source IP : 192.168.1.15

Destination IP : 142.250.183.110

Protocol : TCP

Source Port : 52341

Destination Port : 443

Packet Size : 72 Bytes
```

---

# 📷 Screenshots

Add screenshots of the running application inside the `screenshots` folder.

---

# 📈 Future Improvements

- GUI Dashboard
- Packet Filtering
- Protocol Statistics
- Save packets to JSON
- Search functionality
- Real-time graphs

---

# 👨‍💻 Author

**Siddesha M K**

CodeAlpha Cyber Security Internship

---

# 📜 License

This project is created for educational purposes under the CodeAlpha Internship Program.