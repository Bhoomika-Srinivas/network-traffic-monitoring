# 🌐 Network Traffic Monitoring

This project monitors real-time network traffic and visualizes packet flow, upload/download speeds, and traffic stats.  
Includes login system, packet capturing, and a dashboard with live graphs.

## 🚀 Features
- User authentication
- Real-time packet capture
- Upload/download speed tracking
- Live dashboard with charts
- Scalable backend with Flask + SQLite

## 🛠️ Tech Stack
- Frontend: HTML, CSS, JavaScript, Chart.js
- Backend: Python Flask, Scapy, Psutil
- Database: SQLite

## Project Results

### Packet Flow Graph
![Packet Flow Graph](screenshots/graph1.png)

### Upload & Download Speed Graph
![Speed Graph](screenshots/graph2.png)

### Packet Flow Rate Very Low
![Very Low Traffic](screenshots/graph3.png)

### Network Traffic Rate Low
![Low Traffic](screenshots/graph4.png)

### Network Traffic Rate Moderate
![Moderate Traffic](screenshots/graph5.png)

### Network Traffic Rate High
![High Traffic](screenshots/graph6.png)

## ▶️ Run Locally
```bash
git clone https://github.com/yourusername/network-traffic-monitoring.git
cd network-traffic-monitoring/backend
pip install -r requirements.txt
python app.py
```
Open `http://localhost:5000` in your browser.

## 📜 License
MIT License
