book_name={'harry potter':9,'power':2,'clash of clans':10}

def display_book():
            for book in book_name:
                 print(f"{book}:{book_name[book]}")

def add_book():
    adding_book=input("Name of the new book :")
    no_of_book=int(input("Enter total number of books to add :"))
    book_name[adding_book]=no_of_book
    
def lend_book(dict1):
    
    user_name=(input("Enter your name :"))
    borrow_book=(input("Enter which book you want to borrow :"))
    if borrow_book in book_name and book_name[borrow_book] > 0:
        if borrow_book not in dict1:
            book_name[borrow_book] -=1
            dict1[borrow_book]=[user_name]
        else:
            book_name[borrow_book] -=1
            dict1[borrow_book].append(user_name)

    else :
        yes=input("do you want to know who took the book (y/n) :")
        if yes=='y' and borrow_book in dict1:
            print(f"{', '.join(dict1[borrow_book])} has taken {borrow_book} book")
         
def return_book(dict1):
    user_name = input("Enter your name :")
    ret_book=input("Enter which book you want to return :")
    if ret_book in book_name:
        book_name[ret_book] +=1
        dict1[ret_book].remove(user_name)
        
def update_book():
    replace_books=input("Enter the book which you want to replace :")
    new_book=input("Enter the new book name :")
    add_no_book=int(input("Enter total number of books :"))
    new_dict={new_book:add_no_book}
    book_name.pop(replace_books)
    book_name.update(new_dict)
    book_name[new_book]=add_no_book
    
def delete_book():
    delete_books=input("Enter the book which you want to remove :")
    del book_name[delete_books]

def main():
        
    library_name=input("Enter the library name :")
    print(library_name)
    dict1={}
    while True:

        print("1. display the books name and number of books")
        print("2. add books")
        print("3. update the book name and total number of books")
        print("4. delete the books and no of books")
        print("5. lend book")
        print("6. return book")
        print("7. exit")

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
                  lend_book(dict1)
            case '6':
                  return_book(dict1)
            case '7':
                break
            case _:
                print("invalid choice")
main()