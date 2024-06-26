# Network Monitoring Dashboard (MVP)

# Overview
This project aims to create a Minimum Viable Product (MVP) for monitoring network traffic using Python and HTML. The application will monitor UDP and TCP protocols, capturing incoming and outgoing traffic. It will also allow users to filter traffic based on specific requirements to improve system security.

# Features
- Network Traffic Monitoring: Capture and display both UDP and TCP protocol traffic.
- Dashboard Interface: Use HTML to present a user-friendly dashboard for real-time traffic monitoring.
- Traffic Filtering: Allow users to apply custom filters to the captured traffic for detailed analysis.
- Security Enhancements: Provide insights to help users improve their system security based on the monitored traffic.

# Getting Started

Clone the Repository

```sh
git clone https://github.com/vishalkaushikdixit/network-monitoring-dashboard.git
cd network-monitoring-dashboard
```
Install Dependencies

```sh 
pip install -r requirements.txt
```

Run the Application

```sh
python app.py
```
Access the Dashboard
Open your web browser and go to http://localhost:5000 to view the dashboard.

# Requirements
- Python 3.x
- Flask
- Scapy
- Flask-SocketIO
- eventlet
- HTML/CSS for the front-end
# Usage
1. Start Monitoring: Launch the application to begin capturing network traffic.
2. Apply Filters: Use the dashboard to apply filters based on IP addresses, protocols, or ports.
3. Analyze Traffic: Review the filtered traffic to identify potential security threats or unusual patterns.

# Contributing

We welcome contributions! Please fork the repository and submit a pull request for any enhancements or bug fixes.
