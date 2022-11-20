import random
import time
from hangman_words import words
from hangman_art import logo


chosen_word = random.choice(words).lower()
left = len(chosen_word)+3
print(logo)
print(f'{left} Tries before you hang!')
time.sleep(2)
print("Choose carefully!")
time.sleep(2)

print(chosen_word)
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "—"
print(display)


while "—" in display:
    print(f'you have {left} left')
    guess = input("choose a letter:").lower()
    for index,loop in enumerate(chosen_word):
        letter = chosen_word[index]
        if loop == guess:
            display[index] = letter

        if "—" not in display:
            print("You Win!")
            break

    print(display[0])

    if loop != guess:
        left -= 1


    if left == 0:
        print("you lose")
        print(chosen_word)
        break
    print(f"{' '.join(display)}")
    #     if bookmark == len(chosen_word)+3:
    #         print("you lose")
    #         break