import os

BASE = os.path.dirname(os.path.abspath(__file__))
CASE_DIR = os.path.join(os.path.dirname(BASE), "CASE_FILES")

def list_cases():
    if not os.path.exists(CASE_DIR):
        print("CASE_FILES folder missing.")
        return []
    files = sorted([f for f in os.listdir(CASE_DIR) if f.upper().startswith("CASE_")])
    for f in files:
        print(" -", f)
    return files

def verify_case():
    fn = input("Case filename to verify: ").strip()
    path = os.path.join(CASE_DIR, fn)
    if not os.path.exists(path):
        print("Verification failed: NOT FOUND")
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    ok = ("REF:" in content) and ("STATUS:" in content)
    print("Verification:", "PASS" if ok else "FAIL")

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print("CLEARANCE MODULE")
    print("----------------")

    while True:
        print("\n1) List all case files")
        print("2) Verify a case file format")
        print("3) Exit")
        c = input("Select: ").strip()

        if c == "1":
            print("\nCASE FILE INDEX:")
            list_cases()
        elif c == "2":
            verify_case()
        elif c == "3":
            break

    input("\nPress Enter to return...")

if __name__ == "__main__":
    main()
