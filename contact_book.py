contacts={
   "Ashif" :8877878908
}
while True:
 print("\-----Contact Book Menu -----")
 print("1. Add Contact")
 print("2. Search Contact")
 print("3. View Contacts")
 print("4. Exit")

 choice=input("Select your option (1-4):")

 if choice == "1":
    name=input("Enter name name : ")
    number=input("Enter a number : ")
    contacts[name]=number
    print("Success: ",name,"'s contact has been saved successfully")
 elif choice == "2":
    search_name=input("Enter a name : ")
    if search_name in contacts:
        print("Number : ",contacts[search_name])
    else:
        print("Error: This name is not in the contact list.")
 elif choice == "3":
    for key,value in contacts.items():
        print(key,":",value)
 elif choice == "4":
    print("Closing Contact Book. Goodbye!")
    break
 else:
    print("Invalid choice! Please select a number from 1 to 4.")




