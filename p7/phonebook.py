import psycopg2
import csv


def con():
    return psycopg2.connect(
        host='localhost',
        user='postgres',
        dbname='phonebook_db',
        password='Bekzat240908',
        port='5432'
    )


def create_table():
    c = con()
    cur = c.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL
        )
    """)

    c.commit()
    cur.close()
    c.close()
    print("Table is created")


def insert_from_console():
    c = con()
    cur = c.cursor()

    name = input("Name: ")
    phone = input("Phone: ")

    cur.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    c.commit()
    cur.close()
    c.close()
    print("Data added")


def insert_from_csv():
    c = con()
    cur = c.cursor()

    filename = input("Name of your csv file: ")

    with open(filename, 'r', encoding='utf-8') as file:
        r = csv.reader(file)
        for row in r:
            if len(row) >= 2:
                name = row[0]
                phone = row[1]

                cur.execute(
                    "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                    (name, phone)
                )

    c.commit()
    cur.close()
    c.close()
    print("Data from csv file added")


def update_data():
    c = con()
    cur = c.cursor()

    print("What are you going to update?")
    print("1 - update the name")
    print("2 - update the number")

    ch = input("Your choice: ")

    if ch == "1":
        old_name = input("Print old name: ")
        new_name = input("Print new name: ")

        cur.execute(
            "UPDATE phonebook SET name = %s WHERE name = %s",
            (new_name, old_name)
        )
        print("Name updated.")

    elif ch == "2":
        name = input("Print your name: ")
        new_phone = input("Print new phone number: ")

        cur.execute(
            "UPDATE phonebook SET phone = %s WHERE name = %s",
            (new_phone, name)
        )
        print("Phone number updated.")

    else:
        print("Incorrect choice")
        cur.close()
        c.close()
        return

    c.commit()
    cur.close()
    c.close()
    print("Your data is updated")


def query_data():
    c = con()
    cur = c.cursor()

    print("Search filters:")
    print("1 - show all")
    print("2 - find by name")
    print("3 - find by phone")
    print("4 - find part of name")

    ch = input("Your choice: ")

    if ch == "1":
        cur.execute("SELECT * FROM phonebook")

    elif ch == "2":
        name = input("Your name: ")
        cur.execute(
            "SELECT * FROM phonebook WHERE name = %s",
            (name,)
        )

    elif ch == "3":
        phone = input("Your phone number: ")
        cur.execute(
            "SELECT * FROM phonebook WHERE phone = %s",
            (phone,)
        )

    elif ch == "4":
        part = input("Part of your name: ")
        cur.execute(
            "SELECT * FROM phonebook WHERE name ILIKE %s",
            ('%' + part + '%',)
        )

    else:
        print("Wrong choice")
        cur.close()
        c.close()
        return

    rows = cur.fetchall()

    if rows:
        for row in rows:
            print(f"id: {row[0]}, name: {row[1]}, phone: {row[2]}")
    else:
        print("Nothing found.")

    cur.close()
    c.close()


def delete_data():
    c = con()
    cur = c.cursor()

    print("Delete options:")
    print("1 - by name")
    print("2 - by phone")

    choice = input("Your choice: ")

    if choice == "1":
        name = input("Enter name to delete: ")
        cur.execute(
            "DELETE FROM phonebook WHERE name = %s",
            (name,)
        )
        print("Deletion by name completed.")

    elif choice == "2":
        phone = input("Enter phone to delete: ")
        cur.execute(
            "DELETE FROM phonebook WHERE phone = %s",
            (phone,)
        )
        print("Deletion by phone completed.")

    else:
        print("Invalid choice.")
        cur.close()
        c.close()
        return

    c.commit()
    cur.close()
    c.close()


def menu():
    create_table()

    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1 - Add from console")
        print("2 - Load from CSV")
        print("3 - Update data")
        print("4 - Show / search data")
        print("5 - Delete data")
        print("0 - Exit")

        choice = input("Choose an action: ")

        if choice == "1":
            insert_from_console()
        elif choice == "2":
            insert_from_csv()
        elif choice == "3":
            update_data()
        elif choice == "4":
            query_data()
        elif choice == "5":
            delete_data()
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, try again.")


menu()