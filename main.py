def quiz():
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A. Chennai", "B. Chandigarh", "C. Delhi", "D. Hyderabad"],
            "correct": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
            "correct": "B"
        },
        {
            "question": "Who wrote the famous book 'A Brief History of Time'?",
            "options": ["A. Isaac Newton", "B. Stephen Hawking", "C. Albert Einstein", "D. Nikola Tesla"],
            "correct": "B"
        }
    ]
    
    score = 0  
    
    def ask_question(question_data):
        nonlocal score
        print("\n" + question_data["question"])
        for option in question_data["options"]:
            print(option)
        
        while True:
            answer = input("Your answer (A, B, C, or D): ").strip().upper()
            if answer in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid input. Please enter A, B, C, or D.")
        
        if answer == question_data["correct"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {question_data['correct']}.")
    
    for question in questions:
        ask_question(question)
    
    print(f"\nYour final score is {score}/{len(questions)}.")
    
quiz()
