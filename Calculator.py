current_value = None

print("Welcome to CLI Calculator!")
print("-" * 45)

# A 'while True' loop keeps the calculator running so we can chain operations.
while True:
    
    # --- STEP 1: GET THE FIRST NUMBER ---
    # If we don't have a starting number yet, we ask the user for one.
    if current_value is None:
        try:
            user_input = input("Enter a starting number (or type 'Q' to quit): ").strip()
            
            # Allow the user to quit right away
            if user_input.upper() == 'Q':
                print("Goodbye!")
                break
                
            current_value = float(user_input)
        except ValueError:
            print("-> Error: Please enter a valid number.")
            continue  # Go back to the top of the loop

    # Show the user the current running total
    print(f"\n[ Current Value: {current_value} ]")
    print("Operations: [+] Add  |  [-] Subtract  |  [*] Multiply  |  [/] Divide  |  [C] Clear  |  [Q] Quit")
    
    # --- STEP 2: GET THE OPERATOR ---
    operator = input("Choose an option: ").strip().upper()
    
    # Check if they want to exit or clear the memory before we ask for a second number
    match operator:
        case "Q":
            print("Goodbye! Thank you for calculating.")
            break
        case "C":
            current_value = None
            print("-> Success: Calculator cleared.")
            continue  # Start fresh from the top of the loop

    # If they chose a math operation, we now need a second number to calculate with.
    try:
        next_input = input("Enter next number: ").strip()
        next_num = float(next_input)
    except ValueError:
        print("-> Error: Invalid number. Let's try that operation again.")
        continue

    # --- STEP 3: PERFORM THE CALCULATION ---
    # We use match-case to decide what math to perform on our numbers.
    match operator:
        case "+":
            result = current_value + next_num
            print(f"-> Math: {current_value} + {next_num} = {result}")
            current_value = result  # Save result to memory for chaining
            
        case "-":
            result = current_value - next_num
            print(f"-> Math: {current_value} - {next_num} = {result}")
            current_value = result
            
        case "*":
            result = current_value * next_num
            print(f"-> Math: {current_value} * {next_num} = {result}")
            current_value = result
            
        case "/":
            # Prevent dividing by zero (which would crash Python!)
            if next_num == 0:
                print("-> Error: Cannot divide by zero.")
            else:
                result = current_value / next_num
                print(f"-> Math: {current_value} / {next_num} = {result}")
                current_value = result
                
        case _:
            # This handles anything else they might have typed
            print(f"-> Error: '{operator}' is not a valid operation.")