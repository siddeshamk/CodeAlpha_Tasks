"""
NetSentinel IDS Alert Analyzer

Reads Suricata EVE JSON alerts and generates
a human-readable security summary.
"""

import json
from collections import Counter
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
EVE_FILE = BASE_DIR / "logs" / "eve.json"
REPORT_FILE = BASE_DIR / "reports" / "IDS_Alert_Report.md"


def load_alerts():
    """Load alert events from Suricata EVE JSON."""

    alerts = []

    if not EVE_FILE.exists():
        print(f"[ERROR] EVE file not found: {EVE_FILE}")
        return alerts

    with EVE_FILE.open("r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            try:
                event = json.loads(line)

                if event.get("event_type") == "alert":
                    alerts.append(event)

            except json.JSONDecodeError:
                continue

    return alerts


def build_report(alerts):
    """Create a Markdown security report."""

    if not alerts:
        return """# IDS Alert Report

## Result

No Suricata alerts were found in `logs/eve.json`.

Run Suricata with the configured rules and generate test traffic first.
"""

    signatures = Counter(
        alert.get("alert", {}).get("signature", "Unknown")
        for alert in alerts
    )

    protocols = Counter(
        alert.get("proto", "Unknown")
        for alert in alerts
    )

    sources = Counter(
        alert.get("src_ip", "Unknown")
        for alert in alerts
    )

    destinations = Counter(
        alert.get("dest_ip", "Unknown")
        for alert in alerts
    )

    severities = Counter(
        alert.get("alert", {}).get("severity", "Unknown")
        for alert in alerts
    )

    lines = [
        "# NetSentinel IDS Alert Report",
        "",
        "## Executive Summary",
        "",
        f"Total alerts detected: **{len(alerts)}**",
        "",
        "## Detection Signatures",
        "",
    ]

    for signature, count in signatures.items():
        lines.append(f"- **{signature}** — {count} alert(s)")

    lines.extend([
        "",
        "## Protocols",
        "",
    ])

    for protocol, count in protocols.items():
        lines.append(f"- **{protocol}** — {count}")

    lines.extend([
        "",
        "## Source IPs",
        "",
    ])

    for source, count in sources.most_common():
        lines.append(f"- `{source}` — {count}")

    lines.extend([
        "",
        "## Destination IPs",
        "",
    ])

    for destination, count in destinations.most_common():
        lines.append(f"- `{destination}` — {count}")

    lines.extend([
        "",
        "## Severity",
        "",
    ])

    for severity, count in sorted(severities.items(), key=lambda x: str(x[0])):
        lines.append(f"- Severity `{severity}` — {count}")

    lines.extend([
        "",
        "## Sample Alerts",
        "",
    ])

    for alert in alerts[:10]:
        alert_data = alert.get("alert", {})

        timestamp = alert.get("timestamp", "Unknown")
        source = alert.get("src_ip", "Unknown")
        destination = alert.get("dest_ip", "Unknown")
        protocol = alert.get("proto", "Unknown")
        signature = alert_data.get("signature", "Unknown")
        severity = alert_data.get("severity", "Unknown")

        lines.extend([
            f"### {timestamp}",
            "",
            f"- Source: `{source}`",
            f"- Destination: `{destination}`",
            f"- Protocol: `{protocol}`",
            f"- Signature: **{signature}**",
            f"- Severity: `{severity}`",
            "",
        ])

    lines.extend([
        "## Assessment",
        "",
        "Suricata successfully detected traffic matching the configured "
        "local IDS rule and recorded the events in EVE JSON format.",
        "",
        "The alerts should be reviewed by a security analyst to determine "
        "whether the detected traffic is expected or suspicious.",
        "",
    ])

    return "\n".join(lines)


def main():
    print("=" * 70)
    print("        NETSENTINEL IDS ALERT ANALYZER")
    print("=" * 70)

    alerts = load_alerts()

    print(f"\nAlerts found: {len(alerts)}")

    report = build_report(alerts)

    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    REPORT_FILE.write_text(report, encoding="utf-8")

    print(f"Report created: {REPORT_FILE}")


if __name__ == "__main__":
    main()