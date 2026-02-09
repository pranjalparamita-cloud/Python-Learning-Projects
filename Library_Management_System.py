print("----------------------- LIBRARY MANAGEMENT SYSTEM -----------------------")

def book_catalog(books):
    if not books:
        print("No books in the catalog.")
        return
    print("\n----- Book Catalog -----")
    for book in books:
        status="Available" if book['available'] else "Not Available"
        print(f"Title: {book['title']}, Author: {book['author']}, Status: {status}")


def add_book(books):
    title = input("Enter the title of the book: ").strip()
    author = input("Enter the author of the book: ").strip()

    for book in books:
        if book['title'].lower() == title.lower():
            print("This book already exists in the catalog.")
            return

    books.append({"title": title, "author": author, "available": True})
    print("Book added successfully!")


def borrow_book(books):
    book_title=input("Enter the title of the book you want to borrow: ").strip()

    for book in books:
        if book["title"].lower()==book_title.lower():
            if book["available"]:
                book["available"]=False
                print(f"You have borrowed '{book['title']}' by {book['author']}.")
            else:
                print("Sorry, this book is currently not available.")
            return

    print("Book not found in the catalog.")


def return_book(books):
    book_title=input("Enter the title of the book you want to return: ").strip()

    for book in books:
        if book["title"].lower()==book_title.lower():
            if not book["available"]:
                book["available"]=True
                try:
                    days_late=int(input("Enter the number of days late: "))
                except ValueError:
                    print("Invalid input for days. Assuming 0 days late.")
                    days_late=0

                fine=fine_calculation(days_late)
                if fine > 0:
                    print(f"You have a fine of ${fine}.")
                else:
                    print("Book returned on time. No fine.")
            else:
                print("This book was not borrowed.")
            return

    print("Book not found in the catalog.")


def user_registration(users):
    name=input("Enter your name: ").strip()
    email=input("Enter your email: ").strip()
    phone=input("Enter your phone number: ").strip()

    users.append({"name": name, "email": email, "phone": phone})
    print("User registered successfully!")


def fine_calculation(days_late):
    fine_per_day=1
    return days_late * fine_per_day


def main():
    books=[]
    users=[]

    while True:
        print("\n1. Register User")
        print("2. Add Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Book Catalog")
        print("6. Exit")

        choice=input("Enter your choice: ").strip()

        if choice=="1":
            user_registration(users)

        elif choice=="2":
            add_book(books)

        elif choice=="3":
            borrow_book(books)

        elif choice=="4":
            return_book(books)

        elif choice=="5":
            book_catalog(books)

        elif choice=="6":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__=="__main__":
    main()