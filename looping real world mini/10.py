def main():
    print("--- Mini Project 10: Multiplication Table and Number Analyzer ---")
    
    # 1. Inputs and Validation (Rule 49: Validate that start is not greater than end)
    while True:
        try:
            table_num = int(input("Enter a positive integer for the multiplication table: "))
            if table_num <= 0:
                print("Please enter a number greater than 0.")
                continue
                
            start = int(input("Enter the start of the number range: "))
            end = int(input("Enter the end of the number range: "))
            
            if start > end:
                print("Error: Start value cannot be greater than the end value. Please try again.\n")
                continue
            
            break # Exit loop if all validation checks pass
        except ValueError:
            print("Invalid input. Please enter valid integers.\n")

    # 2. Multiplication Table (Rule 45: Use a loop to print the table from 1 to 10)
    print(f"\n--- Multiplication Table for {table_num} ---")
    for i in range(1, 11):
        print(f"{table_num} x {i} = {table_num * i}")

    # 3. Number Range Analysis (Rule 46: Use another loop to process every integer)
    # Concepts practiced: counter, accumulator
    even_count = 0      # Counter for even numbers
    odd_count = 0       # Counter for odd numbers
    range_sum = 0       # Accumulator for the sum

    # Loop includes the 'end' number
    for num in range(start, end + 1):
        range_sum += num  # Rule 48: Calculate the sum of the range
        
        # Rule 47: Count even and odd numbers
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    # 4. Expected Output Results
    print(f"\n--- Range Analysis Results ({start} to {end}) ---")
    print(f"Even count: {even_count}")
    print(f"Odd count : {odd_count}")
    print(f"Sum of range: {range_sum}")

if __name__ == "__main__":
    main()