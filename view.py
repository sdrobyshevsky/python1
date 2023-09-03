import text
from model import Contact, PhoneBook 

def main_menu():
    for i, item in enumerate(text.menu):  
        if i == 0:
            print(item)
        else:
            print(f'\t{i}. {item}') 
    while True:
        choice = input(text.input_menu) 
        if choice.isdigit() and 0 < int(choice) < len(text.menu):
            return int(choice)
        else:
            print(text.input_menu_error)
         
def print_message(msg: str):
    print('\n' + '=' * len(msg))
    print(msg) 
    print('=' * len(msg) + '\n')
    
def show_book(book: PhoneBook, msg: str):
    if book:
       print('\n' + '*' * (PhoneBook.max_len("name") + PhoneBook.max_len("phone") + PhoneBook.max_len("comment") + 8))    
       for i, contact in book.phone_book.items():   
           print(f'{i:>3}. {contact.name:<{book.max_len("name")}}' 
                f'{contact.phone:<{book.max_len("phone")}}' 
                f'{contact.comment:<{book.max_len("comment")}}') 
           print('*' * (PhoneBook.max_len("name") + PhoneBook.max_len("phone") + PhoneBook.max_len("comment") + 8) + '\n')    
    else: 
        print_message(msg)
        
def input_contact(msg: list[str]) -> list[str]:
    contact = []
    for input_text in msg: 
        contact.append(input(input_text)) 
    return contact 
 
def input_request(msg: str) -> str:
    return input(msg)       
     