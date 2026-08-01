from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime
import csv
import os

CSV_FILE = "captured_packets.csv"

# Create CSV file if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Timestamp",
            "Source IP",
            "Destination IP",
            "Protocol",
            "Source Port",
            "Destination Port",
            "Packet Size"
        ])

packet_count = 0


def detect_protocol(packet):
    if packet.haslayer(TCP):
        return "TCP"
    elif packet.haslayer(UDP):
        return "UDP"
    elif packet.haslayer(ICMP):
        return "ICMP"
    else:
        return "OTHER"


def process_packet(packet):
    global packet_count

    if not packet.haslayer(IP):
        return

    packet_count += 1

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    src_ip = packet[IP].src
    dst_ip = packet[IP].dst
    protocol = detect_protocol(packet)
    packet_size = len(packet)

    src_port = "-"
    dst_port = "-"

    if packet.haslayer(TCP):
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport

    elif packet.haslayer(UDP):
        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport

    print("=" * 70)
    print(f"Packet Number     : {packet_count}")
    print(f"Timestamp         : {timestamp}")
    print(f"Source IP         : {src_ip}")
    print(f"Destination IP    : {dst_ip}")
    print(f"Protocol          : {protocol}")
    print(f"Source Port       : {src_port}")
    print(f"Destination Port  : {dst_port}")
    print(f"Packet Size       : {packet_size} Bytes")

    try:
        payload = bytes(packet.payload)[:40]
        print(f"Payload Preview   : {payload}")
    except:
        print("Payload Preview   : N/A")

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            timestamp,
            src_ip,
            dst_ip,
            protocol,
            src_port,
            dst_port,
            packet_size
        ])


def main():

    print("=" * 70)
    print("          CODEALPHA BASIC NETWORK SNIFFER")
    print("=" * 70)
    print("Capturing packets...")
    print("Press CTRL + C to stop.\n")

    try:
        sniff(prn=process_packet, store=False)

    except KeyboardInterrupt:
        print("\n")
        print("=" * 70)
        print("Packet Capture Stopped")
        print(f"Total Packets Captured : {packet_count}")
        print(f"Packet Log Saved       : {CSV_FILE}")
        print("=" * 70)


if __name__ == "__main__":
    main()