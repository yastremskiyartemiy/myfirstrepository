questions = ("La la la?", "Be be be?", "Me me me?", "You you you?", "Pe pe pe?")

options = (("a", "b", "c", "d"), ("a", "b", "c", "d"), ("a", "b", "c", "d"), ("a", "b", "c", "d"), ("a", "b", "c", "d"))

answers = ("c", "a", "b", "a", "d")
guesses = []
score = 0
questionNum = 0

for question in question:
    print("-------------------")
    print(question)
    for option in options[questionNum]:
        print(option)
    
    guess = input("Enter (a, b, c, d): ")
    guesses.append(guess)
    if guess == answers[qquestionNum]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"The answer is {answer[questionNum]}")
    questionNum += 1

print("-------------------")
print("------Results------")
print("-------------------")

print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)

print(f"Your score is: {score}%")