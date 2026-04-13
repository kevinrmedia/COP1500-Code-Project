# Personal Diary Project Final Version 
# Name: Marlon Campbell and Kevin Rodriguez
# Course: COP 1500 - Intro to Computer Science
# Description:
# This program allows users to write, view, delete, and search
# diary entries. Entries are saved to a file so they are not lost.
# ============================================================

import datetime

# Global list to store diary entries
diary_entries = []

# -----------------------------
# LOAD ENTRIES FROM FILE
# -----------------------------
def load_entries():
    try:
        with open("diary.txt", "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 2:
                    date, entry = parts
                    diary_entries.append({"date": date, "entry": entry})
        print("Entries loaded successfully.\n")
    except FileNotFoundError:
        print("No previous diary found. Starting fresh.\n")

# -----------------------------
# SAVE ENTRIES TO FILE
# -----------------------------
def save_entries():
    with open("diary.txt", "w") as file:
        for item in diary_entries:
            file.write(item["date"] + "|" + item["entry"] + "\n")

# -----------------------------
# GET CURRENT DATE
# -----------------------------
def get_current_date():
    return datetime.datetime.now().strftime("%B %d, %Y - %I:%M %p")

# -----------------------------
# WRITE ENTRY
# -----------------------------
def write_entry():
    print("\n--- Write Entry ---")
    entry = input("Enter your diary entry: ").strip()

    if entry == "":
        print("Entry cannot be empty.")
        return

    date = get_current_date()
    diary_entries.append({"date": date, "entry": entry})
    save_entries()

    print("Entry saved successfully!")

# -----------------------------
# VIEW ENTRIES
# -----------------------------
def view_entries():
    print("\n--- View Entries ---")

    if not diary_entries:
        print("No entries found.")
        return

    for i, item in enumerate(diary_entries):
        print(f"\nEntry {i+1}")
        print("Date:", item["date"])
        print("Text:", item["entry"])

# -----------------------------
# DELETE ENTRY
# -----------------------------
def delete_entry():
    print("\n--- Delete Entry ---")

    if not diary_entries:
        print("No entries to delete.")
        return

    view_entries()

    try:
        choice = int(input("\nEnter entry number to delete: "))

        if 0 < choice <= len(diary_entries):
            removed = diary_entries.pop(choice - 1)
            save_entries()
            print("Deleted:", removed["entry"])
        else:
            print("Invalid entry number.")

    except ValueError:
        print("Please enter a valid number.")

# -----------------------------
# SEARCH ENTRIES
# -----------------------------
def search_entries():
    print("\n--- Search Entries ---")

    keyword = input("Enter keyword: ").lower()

    if keyword == "":
        print("Keyword cannot be empty.")
        return

    found = False

    for item in diary_entries:
        if keyword in item["entry"].lower():
            print("\nDate:", item["date"])
            print("Text:", item["entry"])
            found = True

    if not found:
        print("No matching entries found.")

# -----------------------------
# COUNT ENTRIES
# -----------------------------
def count_entries():
    print("\nTotal entries:", len(diary_entries))

# -----------------------------
# CLEAR ALL ENTRIES
# -----------------------------
def clear_entries():
    confirm = input("Are you sure you want to delete ALL entries? (yes/no): ").lower()

    if confirm == "yes":
        diary_entries.clear()
        save_entries()
        print("All entries deleted.")
    else:
        print("Operation cancelled.")

# -----------------------------
# MENU DISPLAY
# -----------------------------
def display_menu():
    print("\n===== PERSONAL DIARY MENU =====")
    print("1. Write Entry")
    print("2. View Entries")
    print("3. Delete Entry")
    print("4. Search Entries")
    print("5. Count Entries")
    print("6. Clear All Entries")
    print("7. Exit")

# -----------------------------
# MAIN PROGRAM
# -----------------------------
def main():
    load_entries()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            write_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            delete_entry()
        elif choice == "4":
            search_entries()
        elif choice == "5":
            count_entries()
        elif choice == "6":
            clear_entries()
        elif choice == "7":
            print("\nExiting diary... Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

# -----------------------------
# RUN PROGRAM
# -----------------------------
if __name__ == "__main__":
    main()

# SAMPLE INPUT AND OUTPUT DEMONSTRATIONS

# Example 1:
# Input:
# Choose an option: 1
# Enter your diary entry: Today I finished my Python project
# Output:
# Entry saved successfully!

# Example 2:
# Input:
# Choose an option: 2
# Output:
# Entry 1
# Date: April 10, 2026 - 02:30 PM
# Text: Today I finished my Python project

# Example 3:
# Input:
# Choose an option: 4
# Enter keyword: Python
# Output:
# Date: April 10, 2026 - 02:30 PM
# Text: Today I finished my Python project

# Example 4:
# Input:
# Choose an option: 3
# Enter entry number to delete: 1
# Output:
# Deleted: Today I finished my Python project

# Example 5:
# Input:
# Choose an option: 7
# Output:
# Exiting diary... Goodbye!

# ============================================================
# END OF PROGRAM (200+ LINES)
# ============================================================