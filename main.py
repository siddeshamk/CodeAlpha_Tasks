from core.sniffer import start_sniffer, show_summary
from core.colors import Colors
from config import APP_NAME, VERSION, SEPARATOR


def banner():

    print(Colors.TITLE + SEPARATOR)
    print(f"{APP_NAME}  v{VERSION}")
    print(SEPARATOR)
    print("Live Network Packet Analyzer")
    print("Press CTRL + C to stop capturing.")
    print(SEPARATOR)


def main():

    banner()

    try:
        start_sniffer()

    except KeyboardInterrupt:

        print("\nCapture stopped by user.\n")

        show_summary()

    except Exception as e:

        print(f"\nUnexpected Error: {e}")


if __name__ == "__main__":
    main()