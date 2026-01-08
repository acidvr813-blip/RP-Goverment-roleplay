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
        print("\n1) Generate route")
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

    input("\nPress Enter to return...")

if __name__ == "__main__":
    main()
