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

    choice = input("\nOpen which number? (or Enter to exit): ").strip()
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
    input("\nPress Enter to return...")

if __name__ == "__main__":
    main()
