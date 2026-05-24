
tasks = []

print("Welcome to your Terminal To-Do List!")
print("-" * 45)

# 2. START THE MAIN LOOP
# A 'while True' loop keeps the program running forever until we explicitly tell it to 'break'.
while True:
    
    # --- DISPLAY SECTION ---
    print("\n=== My Tasks ===")
    
    # Check if the list is empty
    if len(tasks) == 0:
        print("  (No tasks yet! You are all caught up.)")
    else:
        # enumerate() gives us both the index (i) and the task itself
        for i, task in enumerate(tasks):
            # We add 1 to 'i' so the list displays as 1, 2, 3 instead of 0, 1, 2
            print(f"  {i + 1}. {task}")
            
    print("================\n")
    
    # --- INPUT SECTION ---
    print("Options: [A]dd task  |  [D]elete task  |  [C]lear all  |  [Q]uit")
    
    # input() pauses the program and waits for the user to type something and press Enter
    # .strip() removes accidental spaces, and .upper() makes it uppercase so 'a' becomes 'A'
    user_choice = input("What would you like to do? ").strip().upper()
    
    # --- LOGIC SECTION ---
    # We use match-case (switch statement) to figure out what the user typed
    match user_choice:
        case "A":
            new_task = input("Enter the new task: ")
            
            # Make sure they didn't just press Enter without typing anything
            if new_task.strip() != "":
                tasks.append(new_task)
                print(f"-> Success: Added '{new_task}'")
            else:
                print("-> Warning: Task cannot be blank.")
                
        case "D":
            # We use try/except block because the user might type a letter instead of a number
            try:
                task_number = int(input("Enter the number of the task to delete: "))
                
                # Convert the human number (e.g., 1) back to Python's 0-based index (e.g., 0)
                index = task_number - 1
                
                # Check if the index actually exists in our list
                if 0 <= index < len(tasks):
                    # .pop() removes an item at a specific index and returns it
                    removed_task = tasks.pop(index)
                    print(f"-> Success: Deleted '{removed_task}'")
                else:
                    print("-> Error: That task number doesn't exist.")
            except ValueError:
                print("-> Error: Please enter a valid number.")
                
        case "C":
            # .clear() empties the entire list instantly
            tasks.clear()
            print("-> Success: All tasks have been cleared.")
            
        case "Q":
            print("Goodbye! Have a productive day.")
            # 'break' immediately stops the 'while True' loop, ending the program
            break
            
        case _:
            # The default case if they type something like 'Z' or 'Hello'
            print("-> Invalid choice. Please type A, D, C, or Q.")