# Questions divided by category
quiz_data = {
    "General Knowledge": [
        {
            "question": "What is the capital of Bangladesh?",
            "options": ["A. Chattogram", "B. Khulna", "C. Dhaka", "D. Sylhet"],
            "answer": "C"
        },
        {
            "question": "From which direction does the sun rise?",
            "options": ["A. West", "B. North", "C. South", "D. East"],
            "answer": "D"
        },
        {
            "question": "What is the largest river in the world?",
            "options": ["A. Nile", "B. Amazon", "C. Mississippi", "D. Ganga"],
            "answer": "A"
        }
    ],
    
    "Math": [
        {
            "question": "What is the value of 2 + 2 * 3?",
            "options": ["A. 12", "B. 8", "C. 10", "D. 6"],
            "answer": "B"
        },
        {
            "question": "What is the value of √81?",
            "options": ["A. 7", "B. 8", "C. 9", "D. 10"],
            "answer": "C"
        },
        {
            "question": "What is the approximate value of π?",
            "options": ["A. 2.12", "B. 3.14", "C. 3.41", "D. 4.13"],
            "answer": "B"
        }
    ],
    
    "English": [
        {
            "question": "Choose the correct spelling:",
            "options": ["A. Enviroment", "B. Environment", "C. Environmant", "D. Envaironment"],
            "answer": "B"
        },
        {
            "question": "Synonym of 'Happy'?",
            "options": ["A. Sad", "B. Angry", "C. Joyful", "D. Tired"],
            "answer": "C"
        },
        {
            "question": "Fill in the blank: He ___ to school every day.",
            "options": ["A. go", "B. goes", "C. going", "D. gone"],
            "answer": "B"
        }
    ],
    
    "Science": [
        {
            "question": "Which organ purifies blood in the human body?",
            "options": ["A. Heart", "B. Liver", "C. Kidney", "D. Lungs"],
            "answer": "C"
        },
        {
            "question": "How many days does it take the Earth to orbit the Sun once?",
            "options": ["A. 30 days", "B. 180 days", "C. 365 days", "D. 400 days"],
            "answer": "C"
        },
        {
            "question": "What is the chemical formula of Water?",
            "options": ["A. CO2", "B. H2O", "C. O2", "D. NaCl"],
            "answer": "B"
        }
    ],
    
    "Technology": [
        {
            "question": "Who are the founders of Google?",
            "options": ["A. Larry Page and Sergey Brin", "B. Steve Jobs and Bill Gates", "C. Jeff Bezos and Elon Musk", "D. Mark Zuckerberg and Jack Dorsey"],
            "answer": "A"
        },
        {
            "question": "What is the full form of HTML?",
            "options": ["A. Hyper Trainer Markup Language", "B. Hyper Text Makeup Language", "C. Hyper Text Markup Language", "D. Highlevel Text Markup Language"],
            "answer": "C"
        },
        {
            "question": "Which is known as the brain of the computer?",
            "options": ["A. Hard Disk", "B. RAM", "C. CPU", "D. Monitor"],
            "answer": "C"
        }
    ]
}


# Quiz logic for one category
def run_quiz(questions):
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        
        user_answer = input("Give Your Answer (A/B/C/D): ").upper()
        
        if user_answer == q["answer"]:
            print("✅ Correct Answer!")
            score += 1
        else:
            print(f"❌ Wrong Answer! The Correct Answer is: {q['answer']}")
            
    return score


# Main quiz game with category selection
def quiz_game():
    print('\n')
    print('----------------------------------------------------------')
    print("------------------ Welcome to the Quiz Game! -------------")
    print('----------------------------------------------------------')
    
    while True:
        print("\nAvailable Categories:")
        for i, category in enumerate(quiz_data.keys(), start=1):
            print(f"{i}. {category}")
        print("0. Exit")
        
        choice = input("Choose a category (0 to exit): ")
        
        if choice == "0":
            print("Thanks for playing! Goodbye 👋")
            break
        
        try:
            category_list = list(quiz_data.keys())
            selected_category = category_list[int(choice) - 1]
        except (IndexError, ValueError):
            print("⚠️ Invalid choice! Please try again.")
            continue
        
        print(f"\n--- You selected: {selected_category} ---")
        questions = quiz_data[selected_category]
        
        final_score = run_quiz(questions)
        print("\n--------------------")
        print("Quiz End!")
        print(f"Your Total Score: {final_score}/{len(questions)}")
        print("--------------------")


if __name__ == "__main__":
    quiz_game()
