# Define a list of questions, choices, and correct answers
questions = [
    {
        "question": "Which is the capital of India?",
        "choices": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Who wrote the national anthem of India?",
        "choices": ["A. Rabindranath Tagore", "B. Bankim Chandra Chatterjee", "C. Mahatma Gandhi", "D. Subhas Chandra Bose"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "Who is known as the Father of the Nation in India?",
        "choices": ["A. Jawaharlal Nehru", "B. Sardar Patel", "C. Mahatma Gandhi", "D. B. R. Ambedkar"],
        "answer": "C"
    }
]

# Define the prize money for each question
prize_money = [1000, 5000, 10000, 50000]

# Function to play the game
def play_kbc():
    total_amount = 0

    for i, question in enumerate(questions):
        print(f"Question {i + 1}: {question['question']}")
        for choice in question['choices']:
            print(choice)
        
        user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()

        if user_answer == question['answer']:
            total_amount += prize_money[i]
            print(f"Correct! You've won {prize_money[i]} INR.")
        else:
            print("Incorrect answer. Game over!")
            break

        print(f"Total amount so far: {total_amount} INR\n")

    print(f"Game over! You are taking home {total_amount} INR.")

# Start the game
play_kbc()
