import os
import random
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
INTAKE_DIR = os.path.join(BASE, "intake_files")

def stamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def new_intake():
    os.makedirs(INTAKE_DIR, exist_ok=True)
    n = random.randint(1000, 9999)
    path = os.path.join(INTAKE_DIR, f"INTAKE_{n}.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write("INTAKE FILE\n")
        f.write(f"ID: {n}\n")
        f.write(f"TIME: {stamp()}\n")
        f.write("STATUS: RECEIVED\n")
        f.write("\nNOTES:\n- Local test intake entry.\n")
    print("Created:", path)

def list_intake():
    if not os.path.exists(INTAKE_DIR):
        print("No intake files yet.")
        return
    files = sorted(os.listdir(INTAKE_DIR))
    print("\nINTAKE FILES:")
    for fn in files:
        print(" -", fn)

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print("INTAKE MODULE")
    print("-------------")
    while True:
        print("\n1) Create new intake file")
        print("2) List intake files")
        print("3) Exit")
        c = input("Select: ").strip()
        if c == "1":
            new_intake()
        elif c == "2":
            list_intake()
        elif c == "3":
            break
    input("\nPress Enter to return...")

if __name__ == "__main__":
    main()
