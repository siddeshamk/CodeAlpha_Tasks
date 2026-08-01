import csv
import logging
import os
from scapy.all import wrpcap

from config import CSV_FILE, LOG_FILE

# Create logs folder if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Configure logger
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# Create CSV if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Time",
            "Source IP",
            "Destination IP",
            "Protocol",
            "Source Port",
            "Destination Port",
            "Packet Size",
            "TTL"
        ])


def log_packet(data):
    """Save packet information into CSV."""

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            data["time"],
            data["src_ip"],
            data["dst_ip"],
            data["protocol"],
            data["src_port"],
            data["dst_port"],
            data["packet_size"],
            data["ttl"]
        ])


def log_event(message):
    logging.info(message)


def save_pcap(packet, filename="logs/capture.pcap"):
    """
    Append packet to a PCAP file.
    """

    if os.path.exists(filename):
        wrpcap(filename, packet, append=True)
    else:
        wrpcap(filename, packet)