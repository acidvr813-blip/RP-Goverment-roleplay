import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

APPS = [
    ("Records (Case Files 1-10)", os.path.join(ROOT, "RECORDS", "records_app.py")),
    ("Clearance (List/Verify)", os.path.join(ROOT, "CLEARANCE", "clearance_app.py")),
    ("Security Console (Buttons/Menu)", os.path.join(ROOT, "SECURITY", "security_console.py")),
    ("Intake (Create intake files)", os.path.join(ROOT, "INTAKE", "intake_app.py")),
    ("Internal (Source browser)", os.path.join(ROOT, "INTERNAL", "internal_source.py")),
    ("Transport (World routing)", os.path.join(ROOT, "TRANSPORT", "transport_app.py")),
    ("Communications (Random transmissions)", os.path.join(ROOT, "COMMUNICATIONS", "comms_feed.py")),
    ("Reports (Generate quick report)", os.path.join(ROOT, "REPORTS", "reports_app.py")),
    ("Archive (Archive viewer)", os.path.join(ROOT, "ARCHIVE", "archive_app.py")),
    ("Forms (placeholder)", os.path.join(ROOT, "FORMS", "forms_placeholder.py")),
    ("Exit", None),
]

def run_app(path: str):
    if not os.path.exists(path):
        print("Missing app:", path)
        input("Press Enter...")
        return
    subprocess.run([sys.executable, path], check=False)

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("=======================================")
        print("   INTERNAL RECORDS SYSTEM - LAUNCHER")
        print("=======================================\n")

        for i, (name, _) in enumerate(APPS, start=1):
            print(f"{i}. {name}")

        choice = input("\nSelect: ").strip()
        if not choice.isdigit():
            continue

        idx = int(choice) - 1
        if idx < 0 or idx >= len(APPS):
            continue

        name, path = APPS[idx]
        if path is None:
            break

        run_app(path)

if __name__ == "__main__":
    main()
