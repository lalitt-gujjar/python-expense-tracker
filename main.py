expenses = []  # list of expenses in the form of dictionary 
print("Welcome to expenses tracker :  karcha kam kiya karo ")

while True:
    print("\n====MENU====")
    print("1. Add Expenses")
    print("2. View All The Expenses")
    print("3. View Total Khrcha")
    print("4. To exit")

    choice = input("please enter your choice : ")
    
    # 1. Add Expenses
    if choice == "1":
        date = input("kis date pe kharcha kiya tha? ")
        category = input("is chezz ka karcha kiya hai? ")
        description = input("aur detail dedo: ")
        amount = float(input("kitney ka karcha tha: "))

        expense_item = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense_item)
        print("\nDONE BRO!! expense is added succesfully")

    # 2. View All Expenses
    elif choice == "2":
        if len(expenses) == 0:
            print("\njao aur thoda karcha karo.")
        else:
            print("\n==== ye h apka sara expense ====")
            count = 1
            for eachkharcha in expenses:
                print(f"kharcha number {count} -> "
                      f"Date: {eachkharcha['date']}, "
                      f"Category: {eachkharcha['category']}, "
                      f"Detail: {eachkharcha['description']}, "
                      f"Amount: Rs. {eachkharcha['amount']}"
                )
                count += 1

    # 3. View Total Khrcha
    elif choice == "3":
        total = 0
        for eachkharcha in expenses:
            total = total + eachkharcha["amount"]

        print(f"\nTotal kharcha = Rs. {total}")         

    # 4. Exit
    elif choice == "4":
        print("Thank you apney ye system use kiya!")
        break

    else:
        print("INVALID CHOICE . TRY AGAIN")