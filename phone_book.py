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
5. Quit """

#create empty string to store user input
user_input = ""

#create functions for each menu option

def user_input1():
    #ask user for the first name of the contact  
    first_name = raw_input("What is the contact's first name? ")
    #obtain phone number using dictionary key
    print "%s's phone number is: " % first_name + phone_book[first_name]
    start()

def user_input2():
    first_name = raw_input("What is the contact's first name? ")
    phone_num = raw_input("What is the contact's phone number ")
    phone_book[first_name] = phone_num
    print first_name + " has been added to the phone book."
    start()

def user_input3():
    first_name = raw_input("What is the contact's first name? ")
    phone_book.pop(first_name)
    print first_name + " has been deleted from the phone book."
    start()

def user_input4():
    print phone_book
    start()

def user_input5():
    print "Session Ended"

def start():
    #print menu
    print menu
    #collect user's desired action
    user_input = raw_input("What do you want to do (select 1-5)? ")
    #if statement for 1 - 5 to determine outcome

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

    #if user selects 5, quit  
    if user_input == "5":
      return user_input5()

#start program
start()

