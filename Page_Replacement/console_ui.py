"""Small console helpers used by the project launcher."""


def show_menu():
    print("\nPAGE REPLACEMENT SIMULATOR")
    print("1. FIFO")
    print("2. LRU")
    print("3. Optimal")
    print("0. Exit")


def read_choice():
    while True:
        choice = input("Choose an algorithm: ").strip()
        if choice in {"0", "1", "2", "3"}:
            return choice
        print("Invalid choice. Enter 0, 1, 2, or 3.")
