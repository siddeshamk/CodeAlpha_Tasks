from datetime import datetime

from scapy.all import sniff

from core.parser import parse_packet
from core.logger import log_packet, log_event, save_pcap
from core.statistics import PacketStatistics
from core.colors import Colors

stats = PacketStatistics()


def process_packet(packet):

    parsed = parse_packet(packet)

    if parsed is None:
        return

    parsed["time"] = datetime.now().strftime("%H:%M:%S")

    stats.update(parsed["protocol"])

    # Save packet
    log_packet(parsed)

    # Save PCAP
    save_pcap(packet)

    # Event log
    log_event(
        f'{parsed["protocol"]} Packet {parsed["src_ip"]} -> {parsed["dst_ip"]}'
    )

    # Choose color
    color = Colors.OTHER

    if parsed["protocol"] == "TCP":
        color = Colors.TCP

    elif parsed["protocol"] == "UDP":
        color = Colors.UDP

    elif parsed["protocol"] == "ICMP":
        color = Colors.ICMP

    print(color + "=" * 80)

    print(
        f'[{stats.total}] '
        f'{parsed["protocol"]} | '
        f'{parsed["src_ip"]}:{parsed["src_port"]} '
        f'→ '
        f'{parsed["dst_ip"]}:{parsed["dst_port"]}'
    )

    print(f"TTL      : {parsed['ttl']}")
    print(f"Size     : {parsed['packet_size']} Bytes")
    print(f"Payload  : {parsed['payload']}")


def start_sniffer():

    log_event("Packet capture started.")

    sniff(
        prn=process_packet,
        store=False
    )


def show_summary():

    summary = stats.summary()

    print("\n")
    print("=" * 80)
    print("Capture Summary")
    print("=" * 80)

    for key, value in summary.items():
        print(f"{key:10}: {value}")

    print("=" * 80)