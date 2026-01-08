import os
import random
from datetime import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
CASE_DIR = os.path.join(os.path.dirname(ROOT), "CASE_FILES")

def stamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def ensure_cases():
    os.makedirs(CASE_DIR, exist_ok=True)
    for i in range(1, 11):
        path = os.path.join(CASE_DIR, f"CASE_{i:04d}.txt")
        if not os.path.exists(path):
            ref = f"{random.randint(1000,9999)}-{random.randint(1000,9999)}"
            status = random.choice(["ACTIVE", "CLOSED", "HOLD", "REVIEW"])
            with open(path, "w", encoding="utf-8") as f:
                f.write(f"CASE {i:04d}\n")
                f.write(f"REF: {ref}\n")
                f.write(f"STATUS: {status}\n")
                f.write(f"CREATED: {stamp()}\n")
                f.write("\nNOTES:\n- Auto-generated local test case.\n")

def list_cases():
    files = sorted([p for p in os.listdir(CASE_DIR) if p.upper().startswith("CASE_")])
    if not files:
        print("No case files found.")
        return
    print("\nCASE FILES:")
    for fn in files:
        print(" -", fn)

def view_case():
    name = input("Enter case filename (e.g. CASE_0001.txt): ").strip()
    path = os.path.join(CASE_DIR, name)
    if not os.path.exists(path):
        print("Not found.")
        return
    print("\n" + "="*40)
    with open(path, "r", encoding="utf-8") as f:
        print(f.read())
    print("="*40)

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print("RECORDS MODULE - CASE FILES")
    print("--------------------------")
    ensure_cases()

    while True:
        print("\n1) List cases 1-10")
        print("2) View a case")
        print("3) Re-generate missing cases")
        print("4) Exit")
        c = input("Select: ").strip()

        if c == "1":
            list_cases()
        elif c == "2":
            view_case()
        elif c == "3":
            ensure_cases()
            print("Checked. Missing cases generated.")
        elif c == "4":
            break

    input("\nPress Enter to return...")

if __name__ == "__main__":
    main()
