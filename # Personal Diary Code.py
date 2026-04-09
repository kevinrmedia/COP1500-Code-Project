# Personal Diary Code 
# Marlon Campbell and Kevin Rodriguez - COP 1500

import datetime  # Used to get current date and time

# List to store all diary entries
diary_entries = []

# LOAD ENTRIES FROM FILE
def load_entries():
    try:
        with open("diary.txt", "r") as file:
            for line in file:
                date, entry = line.strip().split("|")
                diary_entries.append({"date": date, "entry": entry})
        print("Entries loaded successfully.\n")
    except FileNotFoundError:
        print("No previous diary found. Starting fresh.\n")

# SAVE ENTRIES TO FILE
def save_entries():
    with open("diary.txt", "w") as file:
        for item in diary_entries:
            file.write(item["date"] + "|" + item["entry"] + "\n")

# WRITE ENTRY
def write_entry():
    print("\n--- Write Entry ---")
    entry = input("Enter your diary entry: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    diary_entries.append({"date": date, "entry": entry})
    save_entries()
    
    print("Entry saved successfully!")

# VIEW ENTRIES
def view_entries():
    print("\n--- View Entries ---")
    
    if not diary_entries:
        print("No entries found.")
    else:
        for i, item in enumerate(diary_entries):
            print(f"\nEntry {i+1}")
            print("Date:", item["date"])
            print("Text:", item["entry"])

# DELETE ENTRY
def delete_entry():
    print("\n--- Delete Entry ---")
    
    view_entries()
    
    try:
        choice = int(input("\nEnter entry number to delete: "))
        
        if 0 < choice <= len(diary_entries):
            removed = diary_entries.pop(choice - 1)
            save_entries()
            print("\nDeleted:", removed["entry"])
        else:
            print("Invalid entry number.")
    
    except ValueError:
        print("Error: Please enter a valid number.")

# SEARCH ENTRIES
def search_entries():
    print("\n--- Search Entries ---")
    keyword = input("Enter keyword to search: ").lower()
    
    found = False
    
    for item in diary_entries:
        if keyword in item["entry"].lower():
            print("\nDate:", item["date"])
            print("Text:", item["entry"])
            found = True
    
    if not found:
        print("No matching entries found.")


# MAIN PROGRAM

def main():
    load_entries()
    
    while True:
        print("\n===== PERSONAL DIARY MENU =====")
        print("1. Write Entry")
        print("2. View Entries")
        print("3. Delete Entry")
        print("4. Search Entries")
        print("5. Exit")
        
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
            print("\nExiting diary... Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

# RUN PROGRAM
main()