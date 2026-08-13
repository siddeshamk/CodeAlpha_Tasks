\# Task 4 — Network Intrusion Detection System



\## Project: NetSentinel IDS



\### 1. Objective



The objective of this project is to implement a network-based Intrusion Detection System (IDS) capable of monitoring network traffic, detecting traffic matching configured security rules, generating alerts, and recording those alerts for analysis.



\### 2. Technology Used



\- Suricata 8.0.6

\- Npcap

\- Windows

\- Python

\- PowerShell

\- Suricata EVE JSON

\- Custom Suricata detection rules



\### 3. System Architecture



```text

Network Traffic

&#x20;      |

&#x20;      v

&#x20;    Npcap

&#x20;      |

&#x20;      v

&#x20; Suricata IDS

&#x20;      |

&#x20;      v

&#x20;Detection Rules

&#x20;      |

&#x20;      v

&#x20;   Alerts

&#x20;   /   \\

&#x20;  v     v

eve.json fast.log

&#x20;  |

&#x20;  v

Python Alert Analyzer

&#x20;  |

&#x20;  v

IDS Alert Report

