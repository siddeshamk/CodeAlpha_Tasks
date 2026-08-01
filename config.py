"""
Application configuration
"""

import os

# Application Info
APP_NAME = "CodeAlpha Network Sniffer"
VERSION = "2.0"

# Output Folder
LOG_FOLDER = "logs"

# Output Files
CSV_FILE = os.path.join(LOG_FOLDER, "captured_packets.csv")
PCAP_FILE = os.path.join(LOG_FOLDER, "capture.pcap")
LOG_FILE = os.path.join(LOG_FOLDER, "sniffer.log")

# Packet Capture
MAX_PAYLOAD_BYTES = 64

# Console
SEPARATOR = "=" * 80