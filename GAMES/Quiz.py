# ------------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("------------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ").upper()
        guess = guess.upper().strip()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# ------------------------------


def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
# ------------------------------


def display_score(correct_guesses, guesses):
    print("------------------------------")
    print("RESULTS: ")
    print("------------------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses / len(questions)) * 100)
    print("Your score is: " + str(score) + "%")
# ------------------------------


def play_again():

    response = input("Do you want to play again? (yes or no): ").upper()
    if response == "YES":
        return True
    else:
        return False

# ------------------------------


questions = {
    "What is the capital of France? ": "C",
    "What is 2 + 2? ": "C",
    "What is the largest planet in our solar system? ": "A",
    "Who created Python programming language? ": "B"
}

options = [["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
           ["A. 3", "B. 5", "C. 4", "D. 6"],
           ["A. Jupiter", "B. Saturn", "C. Earth", "D. Mars"],
           ["A. Dennis Ritchie", "B. Guido van Rossum", "C. Bjarne Stroustrup", "D. James Gosling"]]

new_game()

while play_again():
    new_game()

print("Thanks for playing!")
