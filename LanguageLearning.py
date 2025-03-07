from finnishwords import words
import random


def quiz_user(words):
    score = 0
    words_list = list(words.keys())
    random.shuffle(words_list)
    

    for word in words_list:
        while True:
            print(f"What is the meaning of {word} in English")
            answer = input("Answer: ").strip().lower()
            correct_answer = words[word]

            if not str:  # No answer given - could use "if not answer"
                print("Please provide an answer to the question.")
            else:
                if answer == correct_answer:
                    score += 1
                    print(f"\nCongrats you got it right - {score}\n")
                else:
                    print(f"\nGod your almost as stupid as Arron - {correct_answer}\n")
            
                break

    print(f"Well done, your score was {score}/{len(words)}")

if __name__ == "__main__":
    quiz_user(words)