import os
import time
import random

STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "security_state.txt")

def load_state():
    if not os.path.exists(STATE_FILE):
        return {"locked": False, "level": 2}
    data = {}
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if "=" in line:
                k, v = line.strip().split("=", 1)
                data[k] = v
    return {"locked": data.get("locked", "False") == "True", "level": int(data.get("level", "2"))}

def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        f.write(f"locked={state['locked']}\n")
        f.write(f"level={state['level']}\n")

def bar(pct):
    blocks = pct // 5
    return "█" * blocks + "▒" * (20 - blocks)

def scan():
    print("\nSECURITY SCAN RUNNING...")
    for pct in [10, 33, 58, 81, 100]:
        time.sleep(0.25)
        print(f" [{bar(pct)}] {pct}%")
    print("Scan result:", random.choice(["CLEAR", "CLEAR", "CLEAR", "MINOR ALERT (simulated)"]))

def main():
    os.system("cls" if os.name == "nt" else "clear")
    state = load_state()

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("SECURITY CONSOLE")
        print("----------------")
        print(f"Lock State: {'LOCKED' if state['locked'] else 'UNLOCKED'}")
        print(f"Security Level: {state['level']}")
        print("\n[Buttons]")
        print("1) LOCK SYSTEM")
        print("2) UNLOCK SYSTEM")
        print("3) RUN SECURITY SCAN")
        print("4) INCREASE LEVEL")
        print("5) DECREASE LEVEL")
        print("6) EXIT")

        c = input("\nSelect: ").strip()
        if c == "1":
            state["locked"] = True
            save_state(state)
        elif c == "2":
            state["locked"] = False
            save_state(state)
        elif c == "3":
            scan()
            input("\nPress Enter...")
        elif c == "4":
            state["level"] = min(5, state["level"] + 1)
            save_state(state)
        elif c == "5":
            state["level"] = max(1, state["level"] - 1)
            save_state(state)
        elif c == "6":
            break

    print("Exiting...")
    time.sleep(0.3)

if __name__ == "__main__":
    main()
