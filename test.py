import csv
import datetime
import os
import pytz

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def store_entry():
    tz = pytz.timezone('Asia/Kathmandu')
    Date = datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')

    print(f"The date is {Date}")
    Entry = input("Enter the Entry: ")
    Description = input("Write your description: ")

    with open('newfile.csv', 'a', newline='') as csvfile:
        fieldnames = ['Date', 'Entry', 'Description']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        data = {'Date': Date, 'Entry': Entry, 'Description': Description}
        csv_writer.writerow(data)

def search_keyword(keyword, filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        
        for line in reader:
            if keyword.lower() in line[1].lower():
                return ', '.join(line)  # Join the entire line using commas

        return None  # Return None if no match is found

def read_entry():
    keyword = input("Enter a keyword to search: ")
    filename = 'newfile.csv'
    found_line = search_keyword(keyword, filename)
    
    if found_line:
        print(f"Matching entry found: {found_line}")
    else:
        print(f"No entry found for the keyword: {keyword}")

def remove_entry(filename, keyword_to_remove):
    temp_file = 'tempfile.csv'
    with open(filename, 'r') as csvfile, open(temp_file, 'w', newline='') as temp_csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames

        writer = csv.DictWriter(temp_csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            if keyword_to_remove.lower() not in row['Entry'].lower():
                writer.writerow(row)

    os.remove(filename)
    os.rename(temp_file, filename)

def edit_entry():
    keyword_to_edit = input("Enter the keyword to edit: ")
    with open('newfile.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        lines = list(reader)

    for i, line in enumerate(lines):
        if keyword_to_edit.lower() in line[1].lower():
            Entry = input("Enter the new Entry: ")
            Description = input("Enter the new Description: ")
            lines[i] = [line[0], Entry, Description]

    with open('newfile.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(lines)
    print("Entry edited successfully.")

def main():
    while True:
        clear_screen()
        print("Personal Diary\n")
        print("Menu:")
        print("1. Store Entry")
        print("2. Read Entry")
        print("3. Remove Entry")
        print("4. Edit Entry")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            store_entry()
        elif choice == "2":
            read_entry()
        elif choice == "3":
            filename = 'newfile.csv'
            keyword_to_remove = input("Enter the keyword to remove: ")
            remove_entry(filename, keyword_to_remove)
        elif choice == "4":
            edit_entry()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
