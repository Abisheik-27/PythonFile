books={101:"Rich Dad", 102: "Rich Mom"}
while True:
    print("\n1. Add Books")
    print("2. View Books")
    print("3. Search Books")
    print("4. Exit")
    choice=input("Choose option:")
    if choice=="1":
        book_id=int(input("Enter Book ID:"))
        title=input("Enter Book Title:")
        if book_id in books:
            print("Book already exists")
        else:
            books[book_id]=title
            print("Book added successfully")
    elif choice=="2":
        if len(books)==0:
            print("No Books available")
        else:
            print("Book available")
