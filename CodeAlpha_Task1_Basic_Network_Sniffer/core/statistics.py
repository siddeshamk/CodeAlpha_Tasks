class PacketStatistics:

    def __init__(self):
        self.total = 0
        self.tcp = 0
        self.udp = 0
        self.icmp = 0
        self.other = 0

    def update(self, protocol):

        self.total += 1

        if protocol == "TCP":
            self.tcp += 1

        elif protocol == "UDP":
            self.udp += 1

        elif protocol == "ICMP":
            self.icmp += 1

        else:
            self.other += 1

    def summary(self):

        return {
            "Total": self.total,
            "TCP": self.tcp,
            "UDP": self.udp,
            "ICMP": self.icmp,
            "Other": self.other
        }