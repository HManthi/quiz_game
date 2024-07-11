questions = [
    {
        "prompt" : "What is the capital of France?",
        "options" : ["A. Paris", "B. London", "C.Berlin", "D. Colombo"],
        "answer" : "A"
    },
    {
        "prompt" : "Which language is primarily spoken in Brazil",
        "options" : ["A. Spanish", "B. Portuguese", "C. English", "D. French"],
        "answer" : "B"
    },
    { 
        "prompt" : "Which language is most widely spoken in Latin America?", 
        "options" : ["A. Portuguese", "B. English", "C. Spanish", "D. French"], 
        "answer" : "C" 
    },
    { 
        "prompt" : "Which planet in our solar system is known as the 'Red Planet'?", 
        "options" : ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"], 
        "answer" : "B" 
    },
    { 
        "prompt" : "Which famous painting by Leonardo da Vinci is also known as 'La Gioconda'?", 
        "options" : ["A. The Last Supper", "B. The Mona Lisa", "C. Starry Night", "D. The Scream"], 
        "answer" : "B" 
    },
    { 
        "prompt" : "Which American inventor is credited with developing the light bulb?", 
        "options" : ["A. Thomas Edison", "B. Alexander Graham Bell", "C. Nikola Tesla", "D. Benjamin Franklin"], 
        "answer" : "A" 
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A,B,C or D): ")
        if answer.upper() == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is", question["answer"])
    print("Your final score is", score, "/", len(questions))

run_quiz(questions)