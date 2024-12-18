import time

def word_counter_game():
    print("Welcome to the Word Counter Game!")
    print("You will have 10 seconds to type as many words as you can.")
    input("Press Enter to start...")

    # Start the timer
    start_time = time.time()
    end_time = start_time + 10  # 10-second timer
    words = []

    print("\nStart typing words! Press Enter after each word:")
    while time.time() < end_time:
        word = input()
        words.append(word)

    # End the game

    print("\nTime's up!")
    print(f"You typed {len(words)} words.")

    print("Your words were:", ", ".join(words))

# Run the game
word_counter_game() 