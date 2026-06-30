while True:
    print("\nWelcome to the Pattern Generator and Number Analyzer!")
    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        rows = int(input("Enter the number of rows for the pattern: "))
        print("\nPattern:")
        for i in range(1, rows + 1):
             print("*" * i)

    elif choice == '2':
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        total_sum = 0
        
        for num in range(start, end + 1):
            status = "Even" if num % 2 == 0 else "Odd"
            print(f"Number {num} is {status}")
            total_sum += num
            
        print(f"Sum of all numbers from {start} to {end} is: {total_sum}")

    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please try again.")
