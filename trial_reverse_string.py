# 1. SETUP POINTERS
# Where does the left index start? (Usually 0)
Set left_index = 0

# Where does the right index start? (Think about the length of the array)
Set right_index = 4 

# 2. THE LOOP
# We want to keep going as long as the left finger is to the left of the right finger
While (left_index < right_index):

    // A. THE SWAP (The 3-step dance)
    
    # Step 1: Save the value at the left index so we don't lose it
    Create temp_variable = s[left_index]
    
    # Step 2: Overwrite the left index with the value from the right
    s[left_index] = __________________
    
    # Step 3: Put the saved value (from temp) into the right index
    s[right_index] = __________________
    
    
    # B. MOVE POINTERS
    // Move left finger towards the middle (increment)
    left_index = left_index + 1
    
    // Move right finger towards the middle (decrement)
    right_index = __________________