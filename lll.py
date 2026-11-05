books={"101":"Rich people","102":"Poor People"}
while(True):
    print("========LIBRARY MANAGEMENT SYSTEM========")
    print("1. Add Books")
    print("2. View Books")
    print("3. Search Books")
    print("4. Exit")
    choice=input("Choose option:")
    if choice=="1":
        book_id=input("Enter Book ID:")
        book_title=input("Enter Book Title:")
        if book_id in books:
            print("Already Exists")
        else:
            books[book_id]=book_title
            print("Book Added")
    elif choice=="2":
        if len(books)==0:
            print("No Books Available")
        else:
            print("Books Available:")
            for i,j in books.items():
                print(i,":",j)
    elif choice=="3":
        book_id=input("Enter Book ID:")
        if book_id in books:
            print("Book Found")
            print("Book ID:",book_id)
            print("Book Title:",books[book_id])
        else:
            print("Book Not Found")
    elif choice=="4":
        print("Thank You for Using Library Management System")
        break
    else:
        print("Invalid Choice")


print("hi good morning")
