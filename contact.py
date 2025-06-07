# cont = {}

# def add_no():
#     while True:
#         user_input = input("can you add more number (yes / no) =")
#         if user_input == "no":
#             print("do not add number")
#             print(cont)
#             break
#         elif user_input == "yes":
#             name = input("enter you name")
#             number = int(input("enter a number"))
#             cont[name] = number
#             print(cont)
#         else :
#             print("your input is worng")
# add_no()

# def search_no():
#     while True:
#         user_input = input("Do you want to search for a number? (yes / no): ").strip().lower()
#         if user_input == "yes":
#             name_to_search = input("Enter the name to search for: ").strip()
#             if name_to_search in cont:
#                 print(f"This is your number {name_to_search} => {cont[name_to_search]}")
#             else:
#                 print("Your number is not found in the list.")
#         elif user_input == "no":
#             print("Exiting search.")
#             break
#         else:
#             print("Your input is wrong. Please enter 'yes' or 'no'.")

# search_no()


# def delete():
#     while True:
#         print("\nCurrent Contacts:", cont)
#         user_input = input("Which contact do you want to delete? (or type 'exit' to stop): ").strip()

#         if user_input.lower() == "exit":
#             print("Exiting delete function.")
#             break

#         if user_input in cont:
#             removed = cont.pop(user_input)
#             print(f"Deleted contact: {user_input} => {removed}")
#         else:
#             print("Contact not found.")

# delete()


