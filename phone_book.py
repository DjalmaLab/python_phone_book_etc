import operator
import pickle
#create dictionary to store entries
phone_book = {
        'Andy': '813-468-9137',
    
        'Kayla': '770-468-9132',
    
        'Carl': '325-292-7232'
}

#create variable to store menu
menu = """Electronic Phone Book
========================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Sort entries by name
6. Save entries
7. Load previous entries
8. Quit """

#create empty string to store user input
user_input = ""
blank_line = " "
#create functions for each menu option

def user_input1():
    #ask user for the first name of the contact  
    first_name = raw_input("What is the contact's first name? ")
    if first_name in phone_book:
    #obtain phone number using dictionary key
        print "%s's phone number is: " % first_name + phone_book[first_name]
    else:
        print "Contact does not exist."
    print blank_line
    start()

def user_input2():
    first_name = raw_input("What is the contact's first name? ")
    print blank_line
    phone_num = raw_input("What is the contact's phone number ")
    print blank_line
    phone_book[first_name] = phone_num
    print first_name + " has been added to the phone book."
    print blank_line
    start()

def user_input3():
    first_name = raw_input("What is the contact's first name? ")
    if first_name in phone_book:
        phone_book.pop(first_name)
        print first_name + " has been deleted from the phone book."
    else:
        print blank_line
        print "Contact does not exist. "
    print blank_line
    start()

def user_input4():
    print phone_book
    print blank_line
    start()

def user_input5():
    sorted_phone = sorted(phone_book.items(), key=operator.itemgetter(0))
    print sorted_phone
    print blank_line
    start()

def user_input6():
    saved_book = open('phone_book.pickle', 'w')
    pickle.dump(phone_book, saved_book)
    saved_book.close()
    print "Entries saved."
    print blank_line
    start()

def user_input7():
    restored_book = open('phone_book.pickle', 'r')
    phone_book = pickle.load(restored_book)
    print phone_book
    print blank_line
    start()

def user_input8():
    print "Session Ended"

def start():
    print blank_line
    #print menu
    print menu
    print blank_line
    #collect user's desired action
    user_input = raw_input("What do you want to do (select 1-8)? /n ")
    #if statement for 1 - 5 to determine outcome
    print blank_line
    #if user selects 1, look up entry
    if user_input == "1":
      return user_input1()

    #if user selects 2, set an entry
    if user_input == "2":
      return user_input2()

    #if user selects 3, delete an entry
    if user_input == "3":
      return user_input3()

    #if user selects 4, list all entries
    if user_input == "4":
      return user_input4()

    if user_input == "5":
      return user_input5()

    #if user selects 6, save entries  
    if user_input == "6":
      return user_input6()

    #if user selects 7, load saved entries
    if user_input == "7":
      return user_input7()

    #if user selects 8, quit
      return user_input8()

#start program
start()

