import os
import random
import textwrap
from datetime import datetime

ROOT = "INTERNAL_RECORDS_SYSTEM"

def write_file(path: str, content: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def now_stamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def build():
    if os.path.exists(ROOT):
        print(f'Folder "{ROOT}" already exists. Delete/rename it and run again.')
        return

    # Folder layout
    folders = [
        "RECORDS",
        "CLEARANCE",
        "SECURITY",
        "FORMS",
        "INTAKE",
        "INTERNAL",
        "TRANSPORT",
        "COMMUNICATIONS",
        "REPORTS",
        "ARCHIVE",
        "CASE_FILES",
    ]

    for folder in folders:
        os.makedirs(os.path.join(ROOT, folder), exist_ok=True)

    # Root README
    write_file(
        os.path.join(ROOT, "README.txt"),
        textwrap.dedent(f"""\
        INTERNAL RECORDS SYSTEM (SIMULATION)
        Created: {now_stamp()}

        This is a local roleplay/test structure that runs only on your computer.
        Run "launcher.py" in the root to open the main menu.
        """)
    )

    # Root launcher
    launcher_py = textwrap.dedent("""\
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
            print("=======================================\\n")

            for i, (name, _) in enumerate(APPS, start=1):
                print(f"{i}. {name}")

            choice = input("\\nSelect: ").strip()
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
    """)
    write_file(os.path.join(ROOT, "launcher.py"), launcher_py)

    # RECORDS app: makes case files 1-10
    records_app = textwrap.dedent("""\
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
                    f.write(f"CASE {i:04d}\\n")
                    f.write(f"REF: {ref}\\n")
                    f.write(f"STATUS: {status}\\n")
                    f.write(f"CREATED: {stamp()}\\n")
                    f.write("\\nNOTES:\\n- Auto-generated local test case.\\n")

    def list_cases():
        files = sorted([p for p in os.listdir(CASE_DIR) if p.upper().startswith("CASE_")])
        if not files:
            print("No case files found.")
            return
        print("\\nCASE FILES:")
        for fn in files:
            print(" -", fn)

    def view_case():
        name = input("Enter case filename (e.g. CASE_0001.txt): ").strip()
        path = os.path.join(CASE_DIR, name)
        if not os.path.exists(path):
            print("Not found.")
            return
        print("\\n" + "="*40)
        with open(path, "r", encoding="utf-8") as f:
            print(f.read())
        print("="*40)

    def main():
        os.system("cls" if os.name == "nt" else "clear")
        print("RECORDS MODULE - CASE FILES")
        print("--------------------------")
        ensure_cases()

        while True:
            print("\\n1) List cases 1-10")
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

        input("\\nPress Enter to return...")

    if __name__ == "__main__":
        main()
    """)
    write_file(os.path.join(ROOT, "RECORDS", "records_app.py"), records_app)

    # CLEARANCE app: "has all the case files" + verify
    clearance_app = textwrap.dedent("""\
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
            print("\\n1) List all case files")
            print("2) Verify a case file format")
            print("3) Exit")
            c = input("Select: ").strip()

            if c == "1":
                print("\\nCASE FILE INDEX:")
                list_cases()
            elif c == "2":
                verify_case()
            elif c == "3":
                break

        input("\\nPress Enter to return...")

    if __name__ == "__main__":
        main()
    """)
    write_file(os.path.join(ROOT, "CLEARANCE", "clearance_app.py"), clearance_app)

    # SECURITY app: "buttons" -> menu actions + optional lock/unlock state
    security_console = textwrap.dedent("""\
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
            f.write(f"locked={state['locked']}\\n")
            f.write(f"level={state['level']}\\n")

    def bar(pct):
        blocks = pct // 5
        return "█" * blocks + "▒" * (20 - blocks)

    def scan():
        print("\\nSECURITY SCAN RUNNING...")
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
            print("\\n[Buttons]")
            print("1) LOCK SYSTEM")
            print("2) UNLOCK SYSTEM")
            print("3) RUN SECURITY SCAN")
            print("4) INCREASE LEVEL")
            print("5) DECREASE LEVEL")
            print("6) EXIT")

            c = input("\\nSelect: ").strip()
            if c == "1":
                state["locked"] = True
                save_state(state)
            elif c == "2":
                state["locked"] = False
                save_state(state)
            elif c == "3":
                scan()
                input("\\nPress Enter...")
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
    """)
    write_file(os.path.join(ROOT, "SECURITY", "security_console.py"), security_console)

    # FORMS placeholder (you said you'll do these)
    forms_placeholder = textwrap.dedent("""\
    import os

    def main():
        os.system("cls" if os.name == "nt" else "clear")
        print("FORMS MODULE")
        print("------------")
        print("Placeholder file. You said you'd build this one. 😄")
        print("\\nIdeas:")
        print("- Form picker")
        print("- Auto-fill demo fields")
        print("- Save forms as .txt")
        input("\\nPress Enter to return...")

    if __name__ == "__main__":
        main()
    """)
    write_file(os.path.join(ROOT, "FORMS", "forms_placeholder.py"), forms_placeholder)

    # INTAKE app: creates intake files
    intake_app = textwrap.dedent("""\
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
            f.write("INTAKE FILE\\n")
            f.write(f"ID: {n}\\n")
            f.write(f"TIME: {stamp()}\\n")
            f.write("STATUS: RECEIVED\\n")
            f.write("\\nNOTES:\\n- Local test intake entry.\\n")
        print("Created:", path)

    def list_intake():
        if not os.path.exists(INTAKE_DIR):
            print("No intake files yet.")
            return
        files = sorted(os.listdir(INTAKE_DIR))
        print("\\nINTAKE FILES:")
        for fn in files:
            print(" -", fn)

    def main():
        os.system("cls" if os.name == "nt" else "clear")
        print("INTAKE MODULE")
        print("-------------")
        while True:
            print("\\n1) Create new intake file")
            print("2) List intake files")
            print("3) Exit")
            c = input("Select: ").strip()
            if c == "1":
                new_intake()
            elif c == "2":
                list_intake()
            elif c == "3":
                break
        input("\\nPress Enter to return...")

    if __name__ == "__main__":
        main()
    """)
    write_file(os.path.join(ROOT, "INTAKE", "intake_app.py"), intake_app)

    # INTERNAL app: "source code" vibes - shows files + prints snippets
    internal_source = textwrap.dedent("""\
    import os

    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def list_py_files():
        py_files = []
        for dirpath, _, filenames in os.walk(ROOT):
            for fn in filenames:
                if fn.endswith(".py"):
                    py_files.append(os.path.join(dirpath, fn))
        return sorted(py_files)

    def main():
        os.system("cls" if os.name == "nt" else "clear")
        print("INTERNAL MODULE - SOURCE VIEW")
        print("----------------------------")
        files = list_py_files()
        if not files:
            print("No python files found.")
            input("Press Enter...")
            return

        for i, p in enumerate(files, start=1):
            rel = os.path.relpath(p, ROOT)
            print(f"{i:02d}) {rel}")

        choice = input("\\nOpen which number? (or Enter to exit): ").strip()
        if not choice:
            return
        if not choice.isdigit():
            return
        idx = int(choice) - 1
        if idx < 0 or idx >= len(files):
            return

        path = files[idx]
        os.system("cls" if os.name == "nt" else "clear")
        print("OPEN:", os.path.relpath(path, ROOT))
        print("=" * 60)
        with open(path, "r", encoding="utf-8") as f:
            print(f.read())
        print("=" * 60)
        input("\\nPress Enter to return...")

    if __name__ == "__main__":
        main()
    """)
    write_file(os.path.join(ROOT, "INTERNAL", "internal_source.py"), internal_source)

    # TRANSPORT app: world routing / destinations
    transport_app = textwrap.dedent("""\
    import os
    import random
    import time

    CITIES = [
        "New York", "London", "Tokyo", "Sydney", "Berlin", "Toronto",
        "São Paulo", "Cape Town", "Dubai", "Singapore", "Los Angeles", "Paris"
    ]
    MODES = ["AIR", "SEA", "RAIL", "GROUND"]
    STATUS = ["EN ROUTE", "DELAYED", "CLEARED", "HOLD"]

    def main():
        os.system("cls" if os.name == "nt" else "clear")
        print("TRANSPORT MODULE")
        print("---------------")

        while True:
            print("\\n1) Generate route")
            print("2) Generate 5 random shipments")
            print("3) Exit")
            c = input("Select: ").strip()

            if c == "1":
                a, b = random.sample(CITIES, 2)
                mode = random.choice(MODES)
                st = random.choice(STATUS)
                print(f"Route: {a} -> {b} | Mode: {mode} | Status: {st}")
            elif c == "2":
                for _ in range(5):
                    a, b = random.sample(CITIES, 2)
                    mode = random.choice(MODES)
                    st = random.choice(STATUS)
                    ident = f"TR-{random.randint(1000,9999)}"
                    print(f"{ident}: {a} -> {b} | {mode} | {st}")
                    time.sleep(0.05)
            elif c == "3":
                break

        input("\\nPress Enter to return...")

    if __name__ == "__main__":
        main()
    """)
    write_file(os.path.join(ROOT, "TRANSPORT", "transport_app.py"), transport_app)

    # COMMUNICATIONS app: random comms feed
    comms_feed = textwrap.dedent("""\
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
        print("Ctrl+C to stop.\\n")

        # short randomized burst each open
        for _ in range(random.randint(8, 14)):
            print(line())
            time.sleep(random.uniform(0.05, 0.20))

        print("\\n--- LIVE ---\\n")
        while True:
            print(line())
            time.sleep(random.uniform(0.25, 1.2))

    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            print("\\n[SESSION CLOSED]")
    """)
    write_file(os.path.join(ROOT, "COMMUNICATIONS", "comms_feed.py"), comms_feed)

    # REPORTS app
    reports_app = textwrap.dedent("""\
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
            f.write("SYSTEM REPORT\\n")
            f.write(f"TIME: {stamp()}\\n\\n")
            f.write(f"Summary Score: {random.randint(70, 99)}\\n")
            f.write(f"Items Reviewed: {random.randint(10, 60)}\\n")
            f.write(f"Flags Raised: {random.randint(0, 5)}\\n")
        print("Generated:", path)

    def main():
        os.system("cls" if os.name == "nt" else "clear")
        print("REPORTS MODULE")
        print("--------------")
        while True:
            print("\\n1) Generate report")
            print("2) Exit")
            c = input("Select: ").strip()
            if c == "1":
                gen_report()
            elif c == "2":
                break
        input("\\nPress Enter to return...")

    if __name__ == "__main__":
        main()
    """)
    write_file(os.path.join(ROOT, "REPORTS", "reports_app.py"), reports_app)

    # ARCHIVE app
    archive_app = textwrap.dedent("""\
    import os

    BASE = os.path.dirname(os.path.abspath(__file__))
    ARCH = os.path.join(BASE, "archive_notes")

    def ensure():
        os.makedirs(ARCH, exist_ok=True)
        note = os.path.join(ARCH, "archive_note.txt")
        if not os.path.exists(note):
            with open(note, "w", encoding="utf-8") as f:
                f.write("ARCHIVE NOTE\\n")
                f.write("This is a local archive folder for your simulator.\\n")

    def list_archive():
        ensure()
        files = sorted(os.listdir(ARCH))
        print("\\nARCHIVE FILES:")
        for fn in files:
            print(" -", fn)

    def main():
        os.system("cls" if os.name == "nt" else "clear")
        print("ARCHIVE MODULE")
        print("--------------")
        list_archive()
        input("\\nPress Enter to return...")

    if __name__ == "__main__":
        main()
    """)
    write_file(os.path.join(ROOT, "ARCHIVE", "archive_app.py"), archive_app)

    # A couple top-level example case files can live in CASE_FILES already:
    # (Records app will create them if missing, but we can pre-create one)
    write_file(
        os.path.join(ROOT, "CASE_FILES", "CASE_0001.txt"),
        "CASE 0001\nREF: 1234-5678\nSTATUS: ACTIVE\n\nNOTES:\n- Starter case file.\n"
    )

    print(f"✅ Built: {ROOT}")
    print("Next: open the folder and run: python launcher.py")

if __name__ == "__main__":
    build()
