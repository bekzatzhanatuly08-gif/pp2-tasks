from connect import connect

def show_all():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook;")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def search():
    pattern = input("Enter search: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_phonebook(%s);", (pattern,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL upsert_contact(%s, %s);", (name, phone))
    conn.commit()

    cur.close()
    conn.close()


def delete_contact():
    value = input("Enter name or phone to delete: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL delete_contact(%s);", (value,))
    conn.commit()

    cur.close()
    conn.close()


def menu():
    while True:
        print("\n1. Show all")
        print("2. Search")
        print("3. Add/Update")
        print("4. Delete")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            show_all()
        elif choice == "2":
            search()
        elif choice == "3":
            add_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "0":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()