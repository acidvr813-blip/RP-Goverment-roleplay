import os
import random
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "generated_reports")

def stamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def gen_report():
    os.makedirs(OUT, exist_ok=True)
    n = random.randint(100, 999)
    path = os.path.join(OUT, f"REPORT_{n}.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write("SYSTEM REPORT\n")
        f.write(f"TIME: {stamp()}\n\n")
        f.write(f"Summary Score: {random.randint(70, 99)}\n")
        f.write(f"Items Reviewed: {random.randint(10, 60)}\n")
        f.write(f"Flags Raised: {random.randint(0, 5)}\n")
    print("Generated:", path)

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print("REPORTS MODULE")
    print("--------------")
    while True:
        print("\n1) Generate report")
        print("2) Exit")
        c = input("Select: ").strip()
        if c == "1":
            gen_report()
        elif c == "2":
            break
    input("\nPress Enter to return...")

if __name__ == "__main__":
    main()
