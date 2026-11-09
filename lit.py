import matplotlib.pyplot as plt

expenses = []  # list of expenses in the form of dictionary 
print("Welcome to expenses tracker :  karcha kam kiya karo ")

while True:
    print("\n====MENU====")
    print("1. Add Expenses")
    print("2. View All The Expenses")
    print("3. View Total Khrcha")
    print("4. View Expense Graph")
    print("5. To exit")

    choice = input("please enter your choice : ")
    
    # 1. Add Expenses
    if choice == "1":
        date = input("kis date pe kharcha kiya tha? ")
        category = input("is chezz ka karcha kiya hai? (e.g. Food, Travel): ")
        description = input("aur detail dedo: ")
        
        try:
            amount = float(input("kitney ka karcha tha: "))
        except ValueError:
            print("Invalid amount! Please enter a valid number.")
            continue

        expense_item = {
            "date": date,
            "category": category.strip().capitalize(),
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
        total = sum(item["amount"] for item in expenses)
        print(f"\nTotal kharcha = Rs. {total}")         

    # 4. View Expense Graph (Matplotlib)
    elif choice == "4":
        if len(expenses) == 0:
            print("\nKoi kharcha hi nahi hai bhai, graph kya dikhau? Pehle kharcha add karo!")
        else:
            category_totals = {}
            for item in expenses:
                cat = item["category"]
                amt = item["amount"]
                category_totals[cat] = category_totals.get(cat, 0) + amt

            categories = list(category_totals.keys())
            amounts = list(category_totals.values())

            plt.figure(figsize=(8, 5))
            plt.bar(categories, amounts, color=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
            plt.xlabel("Categories")
            plt.ylabel("Amount (Rs.)")
            plt.title("Category-wise Expense Breakdown")
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            
            print("\nGraph open ho raha hai... Check your taskbar/screen pop-up!")
            plt.show()

    # 5. Exit
    elif choice == "5":
        print("Thank you apney ye system use kiya!")
        break

    else:
        print("INVALID CHOICE . TRY AGAIN")