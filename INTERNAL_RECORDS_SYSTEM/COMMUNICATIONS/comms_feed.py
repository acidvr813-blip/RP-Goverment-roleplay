import os
import random
import time
from datetime import datetime

LINES = [
    "Signal stabilized. Monitoring channel.",
    "Static burst detected. Reacquiring lock...",
    "Relay online. Routing traffic.",
    "Packet received. Archiving.",
    "Low-power beacon detected. Triangulation pending.",
    "Channel interference rising. Adjusting gain.",
    "Handshake complete. Link stable.",
    "Multiple sources detected. Prioritizing strongest.",
    "Checksum mismatch. Discarding frame.",
    "Heartbeat acknowledged.",
]

CALLSIGNS = ["ECHO-7", "ORBIT", "LANTERN", "RAVEN", "NOVA", "EMBER", "CIPHER"]
CHANNELS = ["CH-1", "CH-2", "CH-3", "CH-7", "CH-9", "CH-12"]

def stamp():
    return datetime.now().strftime("%H:%M:%S")

def line():
    cs = random.choice(CALLSIGNS)
    ch = random.choice(CHANNELS)
    msg = random.choice(LINES)
    strength = random.randint(20, 99)
    return f"[{stamp()}] COMMS/{ch} ({cs}) SIG:{strength}% :: {msg}"

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print("COMMUNICATIONS MODULE - RADIO FEED")
    print("---------------------------------")
    print("Ctrl+C to stop.\n")

    # short randomized burst each open
    for _ in range(random.randint(8, 14)):
        print(line())
        time.sleep(random.uniform(0.05, 0.20))

    print("\n--- LIVE ---\n")
    while True:
        print(line())
        time.sleep(random.uniform(0.25, 1.2))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[SESSION CLOSED]")
