from scapy.layers.inet import IP, TCP, UDP, ICMP
from config import MAX_PAYLOAD_BYTES


def parse_packet(packet):

    if not packet.haslayer(IP):
        return None

    protocol = "OTHER"
    src_port = "-"
    dst_port = "-"

    if packet.haslayer(TCP):
        protocol = "TCP"
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport

    elif packet.haslayer(UDP):
        protocol = "UDP"
        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport

    elif packet.haslayer(ICMP):
        protocol = "ICMP"

    payload = ""

    try:
        payload = bytes(packet.payload)[:MAX_PAYLOAD_BYTES]
    except Exception:
        payload = b""

    return {
        "src_ip": packet[IP].src,
        "dst_ip": packet[IP].dst,
        "ttl": packet[IP].ttl,
        "protocol": protocol,
        "src_port": src_port,
        "dst_port": dst_port,
        "packet_size": len(packet),
        "payload": payload
    }