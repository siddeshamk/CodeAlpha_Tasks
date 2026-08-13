\# CodeAlpha Task 3 — Secure Coding Review



\## Project



\*\*Application:\*\* CodeAlpha Network Sniffer / NetSentinel  

\*\*Language:\*\* Python  

\*\*Security Tool:\*\* Bandit  

\*\*Review Type:\*\* Manual Code Review + Static Analysis



\## Objective



Perform a security-focused code review of a Python network packet

analyzer and identify vulnerabilities, security weaknesses, and

recommended remediation steps.



\## Scope



The review covers:



\- `main.py`

\- `config.py`

\- `core/sniffer.py`

\- `core/parser.py`

\- `core/logger.py`

\- `core/statistics.py`



\## Security Testing



Bandit was used for automated Python security analysis.



Command:



```powershell

py -m bandit -r .\\core .\\main.py .\\config.py -f txt

