score = 0  # to keep track of correct answers

questions = [
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Actor", "Astronaut", "Plumber", 1],
    ["What is the capital of France?", "Berlin", "Madrid", "Paris", "Lisbon", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 1],
    ["Who invented the light bulb?", "Albert Einstein", "Thomas Edison", "Isaac Newton", "Nikola Tesla", 1],
    ["Which language is used to create web pages?", "Python", "HTML", "C++", "Java", 1],
    ["How many continents are there?", "5", "6", "7", "8", 2],
    ["Which gas do plants absorb?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen", 2],
    ["What is the national animal of India?", "Lion", "Tiger", "Elephant", "Leopard", 1],
    ["Which country is known as the Land of the Rising Sun?", "China", "South Korea", "Japan", "Thailand", 2],
    ["Who painted the Mona Lisa?", "Picasso", "Leonardo da Vinci", "Van Gogh", "Michelangelo", 1],
    ["Which is the longest river in the world?", "Amazon", "Ganga", "Nile", "Yangtze", 2],
    ["What is the boiling point of water?", "90°C", "80°C", "100°C", "120°C", 2],
    ["Who wrote 'Romeo and Juliet'?", "Shakespeare", "Mark Twain", "J.K. Rowling", "Charles Dickens", 0],
    ["What is the currency of Japan?", "Yen", "Won", "Dollar", "Peso", 0],
    ["Which is the smallest prime number?", "0", "1", "2", "3", 2]
]

for question in questions:
    print("\n" + question[0])
    print(f"A. {question[1]}")
    print(f"B. {question[2]}")
    print(f"C. {question[3]}")
    print(f"D. {question[4]}")

    try:
        a = int(input("Enter your answer (1 for A, 2 for B, 3 for C, 4 for D): ")) - 1
        if question[5] == a:
            print("✅ Correct!\n")
            score += 1
        else:
            correct_letter = ["A", "B", "C", "D"][question[5]]
            correct_answer = question[question[5]+1]
            print(f"❌ Wrong! Correct answer: {correct_letter}. {correct_answer}\n")
    except:
        print("⚠️ Invalid input. Skipping this question.\n")

print(f"🎯 Quiz complete! You scored {score} out of {len(questions)}.")
