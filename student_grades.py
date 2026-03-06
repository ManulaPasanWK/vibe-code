def get_grade(average):
    if average >= 75:
        return "Grade A"
    elif average >= 60:
        return "Grade B"
    elif average >= 40:
        return "Grade C"
    else:
        return "Fail"

def main():
    while True:
        print("\n--- Student Grade Calculator ---")
        name = input("Enter student's name (or type 'Exit' to quit): ")
        
        if name.strip().lower() == "exit":
            print("Exiting program.")
            break

        try:
            mark1 = float(input("Enter mark for Subject 1: "))
            mark2 = float(input("Enter mark for Subject 2: "))
            mark3 = float(input("Enter mark for Subject 3: "))

            average = (mark1 + mark2 + mark3) / 3
            result = get_grade(average)

            print("-" * 30)
            print(f"Name   : {name}")
            print(f"Average: {average:.1f}")
            print(f"Grade  : {result.split()[-1] if 'Grade' in result else result}")
            print("-" * 30)

        except ValueError:
            print("Invalid input. Please enter numerical values for marks.")

if __name__ == "__main__":
    main()
