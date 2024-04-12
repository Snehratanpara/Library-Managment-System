
books_name=['harry potter','power','clash of clan']
total_books=[5,7,8]
def display_book():
    for i in range(len(books_name)):
        print(f"{books_name[i]} :{total_books[i]}")
def add_book():
    adding_book=input("Name of the new book :")
    no_of_book=input("Enter total number of books to add :")
    books_name.append(adding_book)
    total_books.append(no_of_book)

def update_book():
    replace_books=input("Enter the book which you want to replace :")

    new_book=input("Enter the new book name :")
    add_no_book=input("Enter total number of books :")
    for i in range(len(books_name)):
        if replace_books== books_name[i]:
            books_name[i]=new_book
            total_books[i]=add_no_book



def delete_book():
    delete_books=input("Enter the book which you want to remove :")

    # for i in range(len(books_name)):
    #     if delete_books==books_name[i]:
    #         books_name.pop(i)
    #         total_books.pop(i)
    #         break

            
    index=books_name.index(delete_books)
    if delete_books in books_name:
        books_name.remove(delete_books)
        total_books.remove(total_books[index])
        


def main():
        
    library_name=input("Enter the library name :")
    print(library_name)

    while True:

        print("1. display the books name and number of books")
        print("2. add books")
        print("3. update the book name and total number of books")
        print("4. delete the books and no of books")
        print("5. exit")

        choice=input("Enter your choice :")

        match choice:
            case '1':
                display_book()
            case '2':
                add_book()
            case '3':
                update_book()
            case '4':
                delete_book()
            case '5':
                break
            case _:
                print("invalid choice")


if __name__ == '__main__':
    main()


