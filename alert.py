import threading
import os
import logging
from logging.handlers import TimedRotatingFileHandler
from flask import Flask, render_template
from flask_socketio import SocketIO
from scapy.all import *
import datetime
import eventlet  # Import the eventlet package

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet')  # Set the async_mode to 'eventlet'

# Disable Flask development features in production
app.config['DEBUG'] = False

packets = []

@app.route('/')
def index():
    return render_template('index.html')

def packet_callback(packet):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if packet.haslayer(TCP):
        summary = f"[{timestamp}] TCP Packet: {packet.summary()}"
    elif packet.haslayer(UDP):
        summary = f"[{timestamp}] UDP Packet: {packet.summary()}"
    elif packet.haslayer(ICMP):
        summary = f"[{timestamp}] ICMP Packet: {packet.summary()}"
    else:
        summary = f"[{timestamp}] Other Protocol: {packet.summary()}"
    packets.append(summary)
    socketio.emit('packet', summary)

    # Avoid logging sensitive information
    logger.info(f"[{timestamp}] Packet captured")

def start_sniffing():
    # Replace 'eth0' with your desired interface name
    sniff(iface='eth0', prn=packet_callback, store=0)

if __name__ == "__main__":
    # Set up logging to a rotating log file with daily rotation
    log_folder = "logs"
    os.makedirs(log_folder, exist_ok=True)
    log_file = os.path.join(log_folder, "app.log")

    # Configure the logger with a TimedRotatingFileHandler
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[TimedRotatingFileHandler(log_file, when="midnight", interval=1, backupCount=7)])
    
    # Get the logger instance
    logger = logging.getLogger('packet_logger')

    sniffer_thread = threading.Thread(target=start_sniffing)
    sniffer_thread.daemon = True
    sniffer_thread.start()

    # Run the Flask app using Gunicorn or uWSGI with multiple workers for production
    socketio.run(app, host='0.0.0.0', port=5000)

