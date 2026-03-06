def main():
    print("--- Monthly Budget Manager ---")
    
    try:
        # Ask for total monthly budget
        total_budget = float(input("Enter your total monthly budget: "))
        
        expenses = []
        while True:
            entry = input("Enter an expense (or type 'done' to finish): ").strip().lower()
            if entry == "done":
                break
            try:
                expense = float(entry)
                expenses.append(expense)
            except ValueError:
                print("Invalid input. Please enter a numerical value or 'done'.")
            
        # Subtract expenses from total budget
        total_expenses = sum(expenses)
        remaining_balance = total_budget - total_expenses
        
        # Display remaining balance
        print("\n" + "-" * 30)
        print(f"Total Budget      : {total_budget:.2f}")
        print(f"Total Expenses    : {total_expenses:.2f}")
        print(f"Remaining Balance : {remaining_balance:.2f}")
        print("-" * 30)
        
        if remaining_balance < 0:
            print("Warning: You have exceeded your budget!")
        elif remaining_balance < 500:
            print("Warning: Low Funds")
        else:
            print("Good job! You are within your budget.")

    except ValueError:
        print("Invalid input. Please enter numerical values for budget and expenses.")

if __name__ == "__main__":
    main()
