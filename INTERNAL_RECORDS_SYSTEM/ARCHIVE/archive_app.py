import os

BASE = os.path.dirname(os.path.abspath(__file__))
ARCH = os.path.join(BASE, "archive_notes")

def ensure():
    os.makedirs(ARCH, exist_ok=True)
    note = os.path.join(ARCH, "archive_note.txt")
    if not os.path.exists(note):
        with open(note, "w", encoding="utf-8") as f:
            f.write("ARCHIVE NOTE\n")
            f.write("This is a local archive folder for your simulator.\n")

def list_archive():
    ensure()
    files = sorted(os.listdir(ARCH))
    print("\nARCHIVE FILES:")
    for fn in files:
        print(" -", fn)

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print("ARCHIVE MODULE")
    print("--------------")
    list_archive()
    input("\nPress Enter to return...")

if __name__ == "__main__":
    main()
